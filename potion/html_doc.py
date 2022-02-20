from potion.html_tag import HTMLTagBuilder, TAG
from potion.jquery import JQuery, JQueryFunctionBuilder
from bs4 import BeautifulSoup


class HTMLDocBuilder:
    def __init__(self, title=None):
        self.head = HTMLTagBuilder("head")
        self.body = HTMLTagBuilder("body")

        if title:
            self.add_title(title)
        self.add_to_head(TAG.script(src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"))

    def build(self):
        # Build body and collect attached jquery and styles
        body_content, functions_by_id, styles_by_id = self.body.build()

        # Add jquery to document_ready function
        document_ready_fn: JQueryFunctionBuilder = JQuery.document_ready()
        document_ready_fn.add_steps(*functions_by_id)
        self.add_to_head(TAG.script(document_ready_fn.build()))

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
        self.add_to_head(TAG.link(rel="stylesheet",
                                  href=href,
                                  type="text/css"))

    def add_to_head(self, *children):
        for child in children:
            self.head.add_child(child)

    def add_to_body(self, *children):
        for child in children:
            self.body.add_child(child)
