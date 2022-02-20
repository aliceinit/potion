from potion.html_tag import HTMLTagBuilder, TAG
from bs4 import BeautifulSoup


class HTMLDocBuilder:
    def __init__(self, title=None):
        self.root: HTMLTagBuilder = HTMLTagBuilder("html")
        self.head = HTMLTagBuilder("head")
        self.body = HTMLTagBuilder("body")

        self.root.add_child(self.head)
        self.root.add_child(self.body)
        if title:
            self.add_title(title)

    def build(self):
        page = f"<!DOCTYPE html>\n{self.root.build()}"
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

