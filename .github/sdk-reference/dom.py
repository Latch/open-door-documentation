"""Tiny stdlib DOM for Dokka's HTML: enough to find elements by tag and class and read their text."""
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class Node:
    def __init__(self, tag, attrs, parent=None):
        self.tag, self.attrs, self.parent, self.children = tag, dict(attrs), parent, []

    @property
    def classes(self):
        return set((self.attrs.get("class") or "").split())

    def find_all(self, tag=None, cls=None, **attrs):
        for child in self.children:
            if isinstance(child, Node):
                if (tag is None or child.tag == tag) and (cls is None or cls in child.classes) and all(
                        child.attrs.get(k.replace("_", "-")) == v for k, v in attrs.items()):
                    yield child
                yield from child.find_all(tag, cls, **attrs)

    def find(self, tag=None, cls=None, **attrs):
        return next(self.find_all(tag, cls, **attrs), None)

    def text(self):
        return "".join(c if isinstance(c, str) else ("\n" if c.tag == "br" else c.text()) for c in self.children)


class _Builder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = self.current = Node("#root", [])

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.current)
        self.current.children.append(node)
        if tag not in VOID:
            self.current = node

    def handle_endtag(self, tag):
        node = self.current
        while node is not self.root and node.tag != tag:
            node = node.parent
        if node is not self.root:
            self.current = node.parent

    def handle_data(self, data):
        self.current.children.append(data)


def parse(path):
    builder = _Builder()
    builder.feed(open(path, encoding="utf-8").read())
    return builder.root
