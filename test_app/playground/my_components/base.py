from potion.html_doc import HTMLDocBuilder
from potion.styles import CSSBlock
from .header import get_page_header


def get_doc_builder(title):
    """Set up global defaults for my app"""
    doc = HTMLDocBuilder(title=title)
    doc.add_style(
        CSSBlock(
            "body",
            font_family="'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif",
            background_size="cover",
            color="red",
            padding=0,
            margin=0,
            display="flex",
            flex_direction="column"
        )
    )
    return doc


def get_doc_with_header(title):
    doc = get_doc_builder(title)
    doc.add_to_body(get_page_header())
    return doc
