from .base_tag import HTMLTagBuilder


class HTMLButton(HTMLTagBuilder):
    __slots__ = ()

    def __init__(self, *children, **kwargs):
        super().__init__("button", children=children, **kwargs)
