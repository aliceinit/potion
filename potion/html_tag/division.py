from .base_tag import HTMLTagBuilder


class HTMLDivision(HTMLTagBuilder):
    __slots__ = ()

    def __init__(self, *children, **kwargs):
        super().__init__("button", children=children, **kwargs)
