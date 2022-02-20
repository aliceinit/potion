from .base_tag import HTMLTagBuilder


class HTMLOrderedList(HTMLTagBuilder):
    __slots__ = ()

    def __init__(self, *children, **kwargs):
        super().__init__("ol", is_container=True, children=children, **kwargs)


class HTMLUnorderedList(HTMLTagBuilder):
    __slots__ = ()

    def __init__(self, *children, **kwargs):
        super().__init__("ul", is_container=True, children=children, **kwargs)


class HTMLListItem(HTMLTagBuilder):
    __slots__ = ()

    def __init__(self, *children, **kwargs):
        super().__init__("li", is_container=True, children=children, **kwargs)
