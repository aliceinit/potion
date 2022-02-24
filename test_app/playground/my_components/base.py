from flask import url_for
from .theme import Theme
from potion.html_doc import HTMLDocBuilder
from potion.styles import CSSBlock
from .header import get_page_header


def get_doc_builder(title):
    """Set up global defaults for my app"""
    doc = HTMLDocBuilder(title=title)
    doc.add_favicon(href=url_for("static", filename=Theme.favicon_filename))
    doc.add_style("body",
                  font_family="'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif",
                  padding=0,
                  margin=0)
    return doc


def get_doc_with_header(title):
    doc = get_doc_builder(title)
    doc.add_to_body(get_page_header())
    return doc
