from .base_tag import HTMLTagBuilder


class HTMLStyle(HTMLTagBuilder):

    def __init__(self, *children, **kwargs):
        super().__init__("style", children=children, **kwargs)