from potion.html_doc import HTMLDocBuilder
from potion.html_tag import Tag
from potion.styles import CSSBlock
from test_utils.driver import Driver

def header_button(title, link):
    pass


def get_page_header():
    menu = {"Sample Link": "/playground/sample",
            "Sample 2": "/playground/sample2"}
    header = Tag.DIV(
        Tag.A(Tag.H1("Potion Playground"), href="/playground"),
        Tag.UL(
            *[Tag.LI(Tag.A(title, href=path)) for title, path in menu.items()]
        )
    )
    header.add_style(background_color="lightblue",
                     display="flex",
                     flex_direction="column",
                     align_items="center")
    return header
