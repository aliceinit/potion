from .base_tag import HTMLTagBuilder


class HTMLHorizontalRule(HTMLTagBuilder):
    __slots__ = ()

    def __init__(self, *children, **kwargs):
        super().__init__("hr", is_container=False, children=children, **kwargs)
