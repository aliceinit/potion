from .base_tag import HTMLTagBuilder


class HTMLHyperlink(HTMLTagBuilder):
    def __init__(self, children=None, href=None):
        super().__init__("a", is_container=True, children=children)
        self.href = href
        self.xml_prop_names += ["href"]
