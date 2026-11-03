#!/usr/bin/env python3
"""Build the iOS API reference pages from an OpenDOOR iOS SDK release.

Inputs come from the public Latch/opendoor-sdk-spm tag:
  --archive    OpenDOORCore.doccarchive (DocC JSON: descriptions)
  --interface  arm64-apple-ios.swiftinterface (exact public declarations)

Writes one page per public type, plus index.md and _order.yaml, into --out.
"""
import argparse
import glob
import json
import os
import re
import sys

PREFIX = "ios-ref-"
SKIP_GROUPS = {"Default Implementations"}
KINDS = {"struct": "struct", "enum": "enum", "protocol": "protocol", "class": "class"}
QUALIFIERS = re.compile(r"\b(?:OpenDOORCore|Swift|Foundation|Combine|_Concurrency|UIKit|CoreData)\.")


def slug(title):
    return PREFIX + re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


class Archive:
    def __init__(self, path):
        root = os.path.join(path, "data", "documentation")
        modules = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
        if len(modules) != 1:
            sys.exit(f"expected one module in {root}, found {modules}")
        self.root = root
        self.module_dir = os.path.join(root, modules[0])
        self.types = {}
        for path in sorted(glob.glob(os.path.join(self.module_dir, "*.json"))):
            data = json.load(open(path))
            self.types[data["metadata"]["title"]] = data

    def load(self, identifier):
        rel = identifier.split("/documentation/", 1)[1].lower()
        path = os.path.join(self.root, rel + ".json")
        return json.load(open(path)) if os.path.exists(path) else None


def link(title, types):
    return f"[{title}](doc:{slug(title)})" if title in types else f"`{title}`"


def inline(nodes, refs, types):
    out = []
    for node in nodes or []:
        kind = node.get("type")
        if kind == "text":
            out.append(node["text"])
        elif kind == "codeVoice":
            out.append(f"`{node['code']}`")
        elif kind == "emphasis":
            out.append(f"*{inline(node.get('inlineContent'), refs, types)}*")
        elif kind == "strong":
            out.append(f"**{inline(node.get('inlineContent'), refs, types)}**")
        elif kind in ("newTerm", "inlineHead"):
            out.append(inline(node.get("inlineContent"), refs, types))
        elif kind == "reference":
            ref = refs.get(node["identifier"], {})
            title = ref.get("title") or node["identifier"].rsplit("/", 1)[-1]
            path = node["identifier"].split("/documentation/", 1)[-1].split("/")
            if len(path) == 2 and title in types:
                out.append(link(title, types))
            elif ref.get("type") == "link" and ref.get("url"):
                out.append(f"[{title}]({ref['url']})")
            else:
                out.append(f"`{title}`")
        elif kind != "image":
            out.append(node.get("text", ""))
    return "".join(out)


def blocks(nodes, refs, types, level):
    out = []
    for block in nodes or []:
        kind = block.get("type")
        if kind == "paragraph":
            out.append(inline(block.get("inlineContent"), refs, types))
        elif kind == "heading":
            out.append("#" * min(6, level + block.get("level", 2) - 2) + " " + block.get("text", ""))
        elif kind == "codeListing":
            out.append(f"```{block.get('syntax') or 'swift'}\n" + "\n".join(block.get("code", [])) + "\n```")
        elif kind in ("unorderedList", "orderedList"):
            items = []
            for number, item in enumerate(block.get("items", []), 1):
                bullet = f"{number}. " if kind == "orderedList" else "- "
                items.append(bullet + blocks(item.get("content"), refs, types, level).replace("\n", "\n  "))
            out.append("\n".join(items))
        elif kind == "aside" and block.get("name") == "Throws":
            # The contract's "- Throws:" line lists error types by name; link the ones we document.
            text = blocks(block.get("content"), refs, types, level)
            out.append("**Throws:** " + re.sub(r"\b[A-Z]\w+\b", lambda m: link(m.group(0), types) if m.group(0) in types else m.group(0), text))
        elif kind == "aside":
            text = blocks(block.get("content"), refs, types, level).replace("\n", "\n> ")
            out.append(f"> **{block.get('name') or block.get('style', 'Note').title()}:** {text}")
        elif kind == "termList":
            out.append("\n".join(
                f"- **{inline(item['term']['inlineContent'], refs, types)}** — {blocks(item['definition']['content'], refs, types, level)}"
                for item in block.get("items", [])))
    return "\n\n".join(part for part in out if part.strip())


def declaration(data):
    for section in data.get("primaryContentSections", []):
        if section.get("kind") == "declarations":
            return "".join(token["text"] for token in section["declarations"][0]["tokens"])
    return ""


def content_sections(data, refs, types, level):
    out = []
    for section in data.get("primaryContentSections", []):
        kind = section.get("kind")
        if kind == "parameters":
            out.append("#" * level + " Parameters\n\n" + "\n".join(
                f"- `{p['name']}`: {blocks(p.get('content'), refs, types, level + 1)}" for p in section.get("parameters", [])))
        elif kind == "content":
            out.append(blocks(section.get("content"), refs, types, level))
    return "\n\n".join(part for part in out if part.strip())


def interface_blocks(path):
    """Top-level declarations of the swiftinterface, keyed by the type they declare or extend."""
    blocks_by_type = {}
    lines = open(path).read().split("\n")
    index = 0
    while index < len(lines):
        line = lines[index]
        match = re.match(r"^(?:@\S+\s+)*(?:public |open )?(?:final )?(?:struct|enum|protocol|class|extension) ([\w.]+)", line)
        if not match:
            index += 1
            continue
        start = index
        depth = line.count("{") - line.count("}")
        while depth > 0:
            index += 1
            depth += lines[index].count("{") - lines[index].count("}")
        name = match.group(1).split(".")[-1]
        text = QUALIFIERS.sub("", "\n".join(lines[start:index + 1]))
        text = re.sub(r"^(?:@\w+(?:\([^)]*\))?\s+)+", "", text)
        blocks_by_type.setdefault(name, []).append(text)
        index += 1
    return blocks_by_type


def render_type(title, data, archive, interface, version):
    refs = data.get("references", {})
    types = archive.types
    kind = KINDS.get(data["metadata"].get("symbolKind"), data["metadata"].get("symbolKind", "type"))
    decl_text = "\n".join(interface.get(title, [])) or declaration(data)
    lines = [
        "---",
        f"title: {title}",
        f"excerpt: OpenDOOR iOS SDK {version} {kind} reference.",
        "hidden: false",
        "---",
        "",
        f"[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **{version}** (`OpenDOORCore`)",
        "",
    ]
    abstract = inline(data.get("abstract"), refs, types)
    if abstract:
        lines += [abstract, ""]
    overview = content_sections(data, refs, types, 3)
    if overview:
        lines += [overview, ""]
    lines += ["## Declaration", "", "```swift", decl_text, "```", ""]

    members = []
    for group in data.get("topicSections", []):
        if group.get("title") in SKIP_GROUPS:
            continue
        members += [m for m in (archive.load(i) for i in group.get("identifiers", [])) if m]
    for member in sorted(members, key=lambda m: m["metadata"]["title"].lower()):
        member_refs = member.get("references", {})
        lines += [f"## {member['metadata']['title']}", "", "```swift", declaration(member), "```", ""]
        summary = inline(member.get("abstract"), member_refs, types)
        if summary:
            lines += [summary, ""]
        body = content_sections(member, member_refs, types, 3)
        if body:
            lines += [body, ""]

    related = sorted({name for name in re.findall(r"\b[A-Z]\w+\b", decl_text) if name in types and name != title})
    if related:
        lines += ["## Related types", "", " · ".join(link(name, types) for name in related), ""]
    return kind, "\n".join(lines).rstrip() + "\n"


def render_index(kinds, version, tag):
    rows = "\n".join(f"| {link(title, kinds)} | {kind} |" for title, kind in sorted(kinds.items(), key=lambda kv: kv[0].lower()))
    return f"""---
title: iOS API Reference
excerpt: Public OpenDOOR iOS SDK {version} API reference.
hidden: false
---

This reference describes the public API of **OpenDOOR iOS SDK {version}**, imported as `OpenDOORCore`.

Start with [OpenDOOR](doc:ios-ref-opendoor) to obtain a [DOORClient](doc:ios-ref-doorclient), then authenticate with `setupWithToken(token:includeAllLocks:)`.

The declarations below match the [{version} release](https://github.com/Latch/opendoor-sdk-spm/tree/{tag}). Use the [iOS SDK guide](doc:ios-docs) for installation and integration examples.

## Types

| Type | Kind |
| --- | --- |
{rows}
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--archive", required=True)
    parser.add_argument("--interface", required=True)
    parser.add_argument("--version", required=True, help="SDK version shown on the pages, e.g. 2.3.0")
    parser.add_argument("--tag", help="opendoor-sdk-spm tag the inputs came from (defaults to --version)")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    archive = Archive(args.archive)
    interface = interface_blocks(args.interface)
    os.makedirs(args.out, exist_ok=True)
    for stale in glob.glob(os.path.join(args.out, PREFIX + "*.md")):
        os.remove(stale)
    kinds = {}
    for title, data in archive.types.items():
        kinds[title], page = render_type(title, data, archive, interface, args.version)
        open(os.path.join(args.out, slug(title) + ".md"), "w").write(page)
    open(os.path.join(args.out, "index.md"), "w").write(render_index(kinds, args.version, args.tag or args.version))
    open(os.path.join(args.out, "_order.yaml"), "w").write("".join(f"- {slug(t)}\n" for t in sorted(kinds, key=str.lower)))
    print(f"iOS reference: {len(kinds)} types -> {args.out}")


if __name__ == "__main__":
    main()
