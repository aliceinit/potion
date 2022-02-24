from .base_tag import HTMLTagBuilder


class HTMLDivision(HTMLTagBuilder):

    def __init__(self, *children, **kwargs):
        super().__init__("div", children=children, **kwargs)
