from .base_tag import HTMLTagBuilder


class HTMLStyle(HTMLTagBuilder):
    __slots__ = ()

    def __init__(self, *children, **kwargs):
        super().__init__("style", children=children, **kwargs)