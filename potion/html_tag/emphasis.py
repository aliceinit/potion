from .base_tag import HTMLTagBuilder


class HTMLEmphasis(HTMLTagBuilder):
    __slots__ = ()

    def __init__(self, *children, **kwargs):
        super().__init__("em", children=children, **kwargs)
