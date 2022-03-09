from flask import url_for
from .theme import Theme
from potion.dom import HTMLDocBuilder
from .header import get_page_header


def get_doc_builder(title):
    """Set up global defaults for my app"""
    doc = HTMLDocBuilder(title=title)
    doc.add_favicon(href=url_for("static", filename=Theme.favicon_filename))
    doc.add_style("body",
                  font_family="'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif",
                  padding=0,
                  margin=0,
                  height="100vh",
                  width="100vw",
                  display="flex",
                  flex_direction="column")
    return doc


def get_doc_with_header(title):
    doc = get_doc_builder(title)
    doc.add_to_body(get_page_header())
    return doc
