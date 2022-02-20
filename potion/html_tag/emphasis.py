from .base_tag import HTMLTagBuilder


class HTMLEmphasis(HTMLTagBuilder):
    def __init__(self, children=None):
        super().__init__("em", children=children)
