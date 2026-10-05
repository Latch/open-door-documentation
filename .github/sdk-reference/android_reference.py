#!/usr/bin/env python3
"""Build the Android API reference pages from an OpenDOOR Android SDK release.

Input is the Dokka HTML inside the release's -javadoc.jar on Maven Central
(com.door:opendoor.android:<version>), unzipped into --dokka.

Writes one page per public type, plus index.md and _order.yaml, into --out.
"""
import argparse
import glob
import os
import re
import sys

from dom import Node, parse

PREFIX = "android-ref-"
PACKAGE_PREFIX = "com.door.opendoor.android.core.api"
GROUPS = [  # index sections, by package
    ("Client", PACKAGE_PREFIX),
    ("Models and events", PACKAGE_PREFIX + ".model"),
    ("Listeners", PACKAGE_PREFIX + ".listeners"),
    ("Exceptions", PACKAGE_PREFIX + ".exceptions"),
]
# Members every data class, enum or exception gets from Kotlin itself.
SYNTHETIC = {"copy", "equals", "hashCode", "toString", "entries", "valueOf", "values", "name", "ordinal",
             "cause", "message", "value"}


def slug(title):
    return PREFIX + re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def squash(text):
    return re.sub(r"\s+", " ", text.replace("​", "")).strip()


class Reference:
    """The Dokka HTML tree: top-level types by name, and which page belongs to which type."""

    def __init__(self, root):
        packages = [p for p in glob.glob(os.path.join(root, "*", PACKAGE_PREFIX + "*")) if os.path.isdir(p)]
        if not packages:
            sys.exit(f"no {PACKAGE_PREFIX}* packages under {root}")
        self.types = {}  # title -> (package, index.html path)
        for package_dir in sorted(packages):
            package = os.path.basename(package_dir)
            for page in sorted(glob.glob(os.path.join(package_dir, "*", "index.html"))):
                title = squash(parse(page).find("h1").text())
                self.types[title] = (package, page)
        self.dir_to_type = {os.path.dirname(page): title for title, (_, page) in self.types.items()}

    def type_for_href(self, page, href):
        """The top-level type a link points at, if it is one of ours."""
        if not href or href.startswith(("http", "#")):
            return None
        target = os.path.normpath(os.path.join(os.path.dirname(page), href.split("#")[0]))
        return self.dir_to_type.get(os.path.dirname(target)) if target.endswith("index.html") else None


def inline(node, page, ref):
    """Text of a Dokka node, with code spans and links to our own types kept."""
    if isinstance(node, str):
        return node
    if node.tag == "code":
        return f"`{squash(node.text())}`"
    if node.tag == "a":
        text = squash(node.text())
        title = ref.type_for_href(page, node.attrs.get("href"))
        return f"[{text}](doc:{slug(title)})" if title and text == title else text
    if node.tag == "br":
        return "\n"
    return "".join(inline(child, page, ref) for child in node.children)


def prose(nodes, page, ref):
    """Paragraphs, lists and code samples, as markdown blocks."""
    out = []
    for node in nodes:
        if isinstance(node, str) or node.tag in ("h4",) or "symbol" in node.classes or "table" in node.classes:
            continue
        if node.tag == "p":
            out.append(squash(inline(node, page, ref)))
        elif node.tag in ("ul", "ol"):
            items = [squash(inline(li, page, ref)) for li in node.children if isinstance(li, Node) and li.tag == "li"]
            out.append("\n".join((f"{n}. " if node.tag == "ol" else "- ") + item for n, item in enumerate(items, 1)))
        elif "sample-container" in node.classes or node.tag == "pre":
            out.append("```kotlin\n" + node.text().strip() + "\n```")
        else:
            nested = prose(node.children, page, ref)
            if nested:
                out.append(nested)
    return "\n\n".join(part for part in out if part.strip())


def split_symbols(content):
    """One (signature, blocks) pair per declaration in a Dokka content div; overloads share a page."""
    groups = []
    for child in content.children:
        if isinstance(child, Node) and "symbol" in child.classes:
            groups.append((child, []))
        elif groups:
            groups[-1][1].append(child)
    return groups


def tables(blocks):
    """The Parameters / Throws / Return tables that follow a signature, by heading."""
    found, heading = {}, None
    for node in blocks:
        if isinstance(node, str):
            continue
        if node.tag == "h4":
            heading = squash(node.text())
        elif "table" in node.classes and heading:
            found[heading] = node
            heading = None
    return found


def table_rows(table, page, ref):
    rows = []
    for row in table.find_all("div", "table-row"):
        subrow = row.find("div", "main-subrow")
        cells = [c for c in (subrow.children if subrow else []) if isinstance(c, Node)]
        paragraph = row.find("p", "paragraph")
        rows.append((squash(cells[0].text()) if cells else "", squash(inline(paragraph, page, ref)) if paragraph else ""))
    return rows


def sections(page_root):
    """Member tables of a type page, keyed by Dokka's CONSTRUCTOR / TYPE / PROPERTY / FUNCTION / ENTRY."""
    body = page_root.find("div", "tabs-section-body")
    found = {}
    for group in (body.children if body else []):
        if isinstance(group, Node) and group.attrs.get("data-togglable"):
            found[group.attrs["data-togglable"]] = group.find("div", "table")
    entries = page_root.find_all("div", "table-row", data_togglable="ENTRY")
    return found, list(entries)


def own_rows(table, page, declared=()):
    """Rows for members declared on this type; Dokka links inherited ones to another type's folder.

    `declared` holds the constructor's properties, which stay even when Kotlin also generates
    a member of that name (a data class field called `name` or `message`).
    """
    rows = []
    for row in table.find_all("div", "table-row") if table else []:
        link = row.find("a")
        href = link.attrs.get("href", "") if link else ""
        if not link or href.startswith(("http", "../")):
            continue
        name = squash(link.text())
        if (name in SYNTHETIC and name not in declared) or re.fullmatch(r"component\d+", name):
            continue
        signature = row.find("div", "symbol")
        brief = row.find("div", "brief")
        rows.append((name, href, squash(signature.text()) if signature else "", brief))
    return rows


def pretty_signature(signature):
    """Put each constructor parameter of a long class signature on its own line, as the source does."""
    match = re.match(r"^((?:data |sealed |open |abstract )*class \w+)\((.*)\)(.*)$", signature)
    if not match or len(signature) <= 100:
        return signature
    params = re.split(r", (?=(?:val |var )?\w+: )", match.group(2))
    return match.group(1) + "(\n" + "".join(f"    {p},\n" for p in params) + ")" + match.group(3)


def render_function(name, member_page, ref):
    """## name(params) sections for one function page; each overload gets its own section."""
    content = parse(member_page).find("div", "main-content").find("div", "content")
    out = []
    for symbol, blocks in split_symbols(content):
        signature = squash(symbol.text()).replace("abstract ", "")
        params = re.findall(r"[(,]\s*(?:vararg\s+)?(\w+):", signature)
        lines = [f"## {name}({', '.join(params)})", ""]
        description = prose(blocks, member_page, ref)
        if description:
            lines += [description, ""]
        found = tables(blocks)
        bullets = [f"- **`{param}`** — {text}" for param, text in table_rows(found["Parameters"], member_page, ref)] if "Parameters" in found else []
        for heading in ("Return", "Returns"):
            if heading in found:
                bullets += [f"- **Returns:** {text}" for _, text in table_rows(found[heading], member_page, ref)]
        if "Throws" in found:
            for exception, text in table_rows(found["Throws"], member_page, ref):
                target = exception if exception in ref.types else None
                label = f"[{exception}](doc:{slug(target)})" if target else f"`{exception}`"
                bullets.append(f"- **Throws:** {label}" + (f" {text}" if text else ""))
        if bullets:
            lines += bullets + [""]
        out.append(("\n".join(lines).rstrip(), signature))
    return out


def render_type(title, package, page, ref, version):
    root = parse(page)
    main = root.find("div", "main-content")
    cover = main.find("div", "cover")
    content = cover.find("div", "content")
    signature = squash(content.find("div", "symbol").text())
    description = prose([c for c in content.children if not (isinstance(c, Node) and c.tag == "h4")], page, ref)
    found, entries = sections(main)

    kind = "enum" if signature.startswith("enum ") else "interface" if " interface " in f" {signature}" else "class"
    lines = ["---", f"title: {title}", f"excerpt: OpenDOOR Android SDK {version} API reference", "hidden: false", "---", "",
             "[Android API Reference](doc:android-api-reference)", "", f"OpenDOOR Android SDK **{version}** ({version} release).", ""]
    if description:
        lines += [description, ""]

    # Dokka lists properties alphabetically; the page follows the constructor order instead.
    order = {name: i for i, name in enumerate(re.findall(r"(?:val|var) (\w+):", signature))}
    properties = own_rows(found.get("PROPERTY"), page, order)
    documented = sorted(((name, squash(inline(brief, page, ref))) for name, _, _, brief in properties if brief),
                        key=lambda item: order.get(item[0], len(order)))
    if documented and kind != "interface":
        lines += [f"- **`{name}`** — {text}" for name, text in documented] + [""]

    members, declaration_lines = [], []
    if kind == "enum":
        names = [squash(row.find("a").text()) for row in entries if row.find("a")]
        header = re.sub(r"^enum (\w+).*$", r"enum class \1", signature)
        declaration = header + " {\n" + "".join(f"\n    {n}," for n in names) + "\n}"
        for row in entries:
            brief = row.find("div", "brief")
            members.append((squash(row.find("a").text()), [squash(inline(brief, page, ref))] if brief else []))
    else:
        for name, href, member_signature, _ in own_rows(found.get("TYPE"), page):
            nested_page = os.path.normpath(os.path.join(os.path.dirname(page), href))
            nested_content = parse(nested_page).find("div", "cover").find("div", "content")
            nested_signature = squash(nested_content.find("div", "symbol").text())
            nested_found, _ = sections(parse(nested_page).find("div", "main-content"))
            # A companion object that only holds private helpers has nothing to document.
            if name == "Companion" and not any(own_rows(nested_found.get(kind), nested_page) for kind in ("PROPERTY", "FUNCTION")):
                continue
            declaration_lines.append(nested_signature)
            text = prose([c for c in nested_content.children if not (isinstance(c, Node) and c.tag == "h4")], nested_page, ref)
            nested_declared = re.findall(r"(?:val|var) (\w+):", nested_signature)
            bullets = [f"- **`{n}`** — {squash(inline(b, nested_page, ref))}"
                       for n, _, _, b in own_rows(nested_found.get("PROPERTY"), nested_page, nested_declared) if b]
            members.append((name, [part for part in [text, "\n".join(bullets)] if part]))
        for name, href, member_signature, _ in own_rows(found.get("FUNCTION"), page):
            for section, full_signature in render_function(name, os.path.normpath(os.path.join(os.path.dirname(page), href)), ref):
                declaration_lines.append(full_signature)
                members.append((None, [section]))
        if kind == "interface":
            declaration_lines += [signature_of for _, _, signature_of, _ in properties]
        body = "".join(f"\n    {line}" for line in declaration_lines)
        declaration = pretty_signature(signature.replace("abstract ", "")) + (f" {{{body}\n}}" if body else "")

    lines += ["## Declaration", "", "```kotlin", declaration, "```", ""]
    for name, parts in members:
        if name is not None:
            lines += [f"## {name}", ""]
        lines += [part for part in parts for part in (part, "")]

    linked = set(re.findall(r"\(doc:(android-ref-[a-z0-9-]+)\)", "\n".join(lines)))
    related = sorted(t for t in ref.types if t != title and (
        slug(t) in linked or re.search(rf"\b{re.escape(t)}\b", declaration)))
    if related:
        lines += ["## Related types", ""] + [f"- [{t}](doc:{slug(t)})" for t in related] + [""]
    lines += [f"Package: `{package}`."]
    return "\n".join(lines).rstrip() + "\n"


def render_index(ref, version):
    sections_md = []
    for heading, package in GROUPS:
        titles = sorted(t for t, (p, _) in ref.types.items() if p == package)
        if titles:
            sections_md.append(f"## {heading}\n\n" + "\n".join(f"- [{t}](doc:{slug(t)})" for t in titles))
    return f"""---
title: Android API Reference
excerpt: Public API for OpenDOOR Android SDK {version}
hidden: false
---

Reference for **OpenDOOR Android SDK {version}**, the published Android artifact for SDK {version}.

```kotlin
implementation("com.door:opendoor.android:{version}")
```

Start with [OpenDOOR](doc:android-ref-opendoor) and [DoorClient](doc:android-ref-doorclient). Authenticate the shared client with `setupWithToken`, then retrieve locks and observe unlock events.

{chr(10).join(sections_md)}

This reference covers the public `core.api` surface of the release artifact. Nested event variants and exception reasons appear on their parent type pages.
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dokka", required=True, help="unzipped Dokka HTML from the -javadoc.jar")
    parser.add_argument("--version", required=True, help="SDK version shown on the pages, e.g. 2.3")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    ref = Reference(args.dokka)
    os.makedirs(args.out, exist_ok=True)
    for stale in glob.glob(os.path.join(args.out, PREFIX + "*.md")):
        os.remove(stale)
    for title, (package, page) in ref.types.items():
        open(os.path.join(args.out, slug(title) + ".md"), "w").write(render_type(title, package, page, ref, args.version))
    open(os.path.join(args.out, "index.md"), "w").write(render_index(ref, args.version))
    open(os.path.join(args.out, "_order.yaml"), "w").write("".join(f"- {slug(t)}\n" for t in sorted(ref.types, key=str.lower)))
    print(f"Android reference: {len(ref.types)} types -> {args.out}")


if __name__ == "__main__":
    main()
