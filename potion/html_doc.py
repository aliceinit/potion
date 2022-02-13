from potion.html_tag import HTMLTagBuilder
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

    def add_to_head(self, html_tag: HTMLTagBuilder):
        self.head.add_child(html_tag)

    def add_to_body(self, html_tag: HTMLTagBuilder):
        self.body.add_child(html_tag)

    def add_tags(self, html_tags: list):
        for tag in html_tags:
            self.add_to_body(tag)
