from .base_tag import HTMLTagBuilder


class HTMLScript(HTMLTagBuilder):

    def __init__(self, *children, **kwargs):
        super().__init__("script", children=children, **kwargs)
        self.src = kwargs.get("src")
        self.xml_prop_names += ["src"]
