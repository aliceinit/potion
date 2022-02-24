from .base_tag import HTMLTagBuilder


class HTMLHeading1(HTMLTagBuilder):

    def __init__(self, *children, **kwargs):
        super().__init__("h1", children=children, **kwargs)


class HTMLHeading2(HTMLTagBuilder):

    def __init__(self, *children, **kwargs):
        super().__init__("h1", children=children, **kwargs)


class HTMLHeading3(HTMLTagBuilder):

    def __init__(self, *children, **kwargs):
        super().__init__("h1", children=children, **kwargs)


class HTMLHeading4(HTMLTagBuilder):

    def __init__(self, *children, **kwargs):
        super().__init__("h1", children=children, **kwargs)


class HTMLHeading5(HTMLTagBuilder):

    def __init__(self, *children, **kwargs):
        super().__init__("h1", children=children, **kwargs)


class HTMLHeading6(HTMLTagBuilder):

    def __init__(self, *children, **kwargs):
        super().__init__("h1", children=children, **kwargs)
