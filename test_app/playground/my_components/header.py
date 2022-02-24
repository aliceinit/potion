from flask import url_for
from potion.html_doc import HTMLDocBuilder
from potion.html_tag import Tag
from potion.styles import CSSBlock
from test_utils.driver import Driver
from .theme import Theme


def header_button(title, link):
    pass


def get_page_header():
    menu = {"Sample Link": "/playground/sample",
            "Sample 2": "/playground/sample2"}
    header = Tag.DIV(
        Tag.DIV(Tag.IMAGE(src=url_for('static', filename=Theme.logo_filename),
                          alt="Potion Logo",
                          width=100,
                          height=100,
                          id="header-logo"),
                Tag.A(Tag.H1("Potion Playground"),
                      href="/playground",
                      id="main-page-link"),
                style={"display": "flex", "padding": "0 100px 0 0"}),
        Tag.UL(*[Tag.LI(Tag.A(title, href=path)) for title, path in menu.items()]),
        id="header"
    )

    header.add_style(background_color=Theme.colors.PRIMARY_LIGHT,
                     display="flex",
                     flex_direction="column",
                     align_items="center")
    header.add_style("h1",
                     color=Theme.colors.PRIMARY_MAIN,
                     font_weight="bolder",
                     font_family="'Monotype Corsiva','Apple Chancery','ITC Zapf Chancery','URW Chancery L',cursive",
                     font_size="3rem")
    header.add_style("a",
                     color=Theme.colors.PRIMARY_LIGHT,
                     text_decoration="none")
    header.add_style("li",
                     list_style_type="none",
                     background_color=Theme.colors.PRIMARY_DARK)
    header.add_style("ul",
                     display="flex",
                     flex_direction="row",
                     align_items="space-between",
                     padding=0)

    return header
