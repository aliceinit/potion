from .base_tag import HTMLTagBuilder


class HTMLParagraph(HTMLTagBuilder):

    def __init__(self, *children, **kwargs):
        super().__init__("p", is_container=True, children=children, **kwargs)
