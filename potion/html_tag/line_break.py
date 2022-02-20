from .base_tag import HTMLTagBuilder


class HTMLLineBreak(HTMLTagBuilder):
    def __init__(self, children=None):
        super().__init__("br", is_container=False, children=children)
