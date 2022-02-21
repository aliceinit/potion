from .base_tag import HTMLTagBuilder


class HTMLHeading1(HTMLTagBuilder):
    __slots__ = ()

    def __init__(self, *children, **kwargs):
        super().__init__("h1", children=children, **kwargs)


class HTMLHeading2(HTMLTagBuilder):
    __slots__ = ()

    def __init__(self, *children, **kwargs):
        super().__init__("h1", children=children, **kwargs)


class HTMLHeading3(HTMLTagBuilder):
    __slots__ = ()

    def __init__(self, *children, **kwargs):
        super().__init__("h1", children=children, **kwargs)


class HTMLHeading4(HTMLTagBuilder):
    __slots__ = ()

    def __init__(self, *children, **kwargs):
        super().__init__("h1", children=children, **kwargs)


class HTMLHeading5(HTMLTagBuilder):
    __slots__ = ()

    def __init__(self, *children, **kwargs):
        super().__init__("h1", children=children, **kwargs)


class HTMLHeading6(HTMLTagBuilder):
    __slots__ = ()

    def __init__(self, *children, **kwargs):
        super().__init__("h1", children=children, **kwargs)
