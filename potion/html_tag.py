class HTMLTagBuilder:
    def build(self):
        if not self.is_container:
            return f"<{self.name} />"
        else:
            tag = f"<{self.name}>"
            for child_tag in self.children:
                if isinstance(child_tag, str):
                    tag += child_tag
                elif isinstance(child_tag, HTMLTagBuilder):
                    tag += child_tag.build()
                else:
                    raise ValueError(f"Cannot render HTML Tag Child of type {type(child_tag)}: {child_tag}")
            tag += f"</{self.name}>"
            return tag

    def __init__(self, name, is_container=True, children=None):
        self.name = name
        self.is_container = is_container
        if isinstance(children, str):
            self.children = [children]
        elif children is not None:
            self.children = [c for c in children]  # Check that children is iterable
        else:
            self.children = []

    def add_child(self, child):
        self.children.append(child)


class LineBreak(HTMLTagBuilder):
    def __init__(self, children=None):
        super().__init__("br", is_container=False, children=children)


class HorizontalRule(HTMLTagBuilder):
    def __init__(self, children=None):
        super().__init__("hr", is_container=False, children=children)


class Paragraph(HTMLTagBuilder):
    def __init__(self, children=None):
        super().__init__("p", children=children)


class Emphasis(HTMLTagBuilder):
    def __init__(self, children=None):
        super().__init__("em", children=children)


class TAG:
    # Empty Tags
    br = LineBreak
    hr = HorizontalRule
    # Container Tags
    p = Paragraph
    em = Emphasis
