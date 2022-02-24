from .base_tag import HTMLTagBuilder


class HTMLEmphasis(HTMLTagBuilder):

    def __init__(self, *children, **kwargs):
        super().__init__("em", children=children, **kwargs)
