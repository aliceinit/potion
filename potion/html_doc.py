from potion.html_tag import HTMLTagBuilder, Tag
from potion.jquery import JQuery, JQueryFunctionBuilder
from potion.styles import CSSBlock
from bs4 import BeautifulSoup


class HTMLDocBuilder:
    def __init__(self, title=None):
        self.head = HTMLTagBuilder("head")
        self.body = HTMLTagBuilder("body")
        self.functions = []
        self.styles = []
        if title:
            self.add_title(title)
        self.add_to_head(Tag.SCRIPT(src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"))

    def build(self):
        # Build body and collect attached jquery and styles
        body_content, functions_by_id, styles_by_id = self.body.build()

        # Add jquery to document_ready function
        document_ready_fn: JQueryFunctionBuilder = JQuery.document_ready()
        document_ready_fn.add_steps(*self.functions, *functions_by_id)
        self.add_to_head(Tag.SCRIPT(document_ready_fn.build()))

        # Add css statements to styles in head
        self.add_to_head(Tag.STYLE("\n".join(style.build() for style in
                                             self.styles + styles_by_id)))

        # Build head
        head_content, _, _ = self.head.build()

        # Add head and body to a root tag and build the page
        root = HTMLTagBuilder("html")
        root.add_child(head_content)
        root.add_child(body_content)
        page_content, _, _ = root.build()

        page = f"<!DOCTYPE html>\n{page_content}"
        soup = BeautifulSoup(page, 'html5lib')
        return soup.prettify()

    def add_title(self, title):
        title_tag = HTMLTagBuilder("title", children=title)
        self.head.add_child(title_tag)

    def add_stylesheet(self, href):
        self.add_to_head(Tag.LINK(rel="stylesheet",
                                  href=href,
                                  type="text/css"))

    def add_favicon(self, href):
        self.add_to_head(Tag.LINK(rel="icon",
                                  type="image/x-icon",
                                  href=href))

    def add_function(self, source: str, event: str, jquery_partial=JQueryFunctionBuilder):
        self.functions.append(jquery_partial(event, source))

    def add_style(self, selector, **kwargs):
        self.styles.append(CSSBlock(selector, **kwargs))

    def add_to_head(self, *children):
        for child in children:
            self.head.add_child(child)

    def add_to_body(self, *children):
        for child in children:
            self.body.add_child(child)
