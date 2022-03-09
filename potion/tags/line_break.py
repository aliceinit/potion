from .base_tag import HTMLTagBuilder


class HTMLLineBreak(HTMLTagBuilder):

    def __init__(self, *children, **kwargs):
        super().__init__("br", is_container=False, children=children, **kwargs)
