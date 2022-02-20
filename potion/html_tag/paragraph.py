from .base_tag import HTMLTagBuilder


class HTMLParagraph(HTMLTagBuilder):
    def __init__(self, children=None, html_class=None, id=None):
        super().__init__("p", children=children, html_class=html_class, id=id)
