from flask import url_for
from potion.html_doc import HTMLDocBuilder
from potion.html_tag import Tag
from potion.styles import CSSBlock
from test_utils.driver import Driver
from .theme import Theme


def header_button(title, href, button_id):
    a = Tag.A(
        title,
        href=href,
        id=button_id,
        style={"padding": ".5rem",
               "margin": "1px",
               "border_radius": ".5rem .5rem 0 0 ",
               "background_color": Theme.colors.ACCENT_A_MAIN,
               "color": Theme.colors.ACCENT_A_LIGHT}
    )
    a.add_style(":hover",
                background_color=Theme.colors.ACCENT_A_LIGHT,
                color=Theme.colors.ACCENT_A_DARK)
    return a


def get_page_header():
    menu_buttons = [("Sample Link", "/playground/sample", "menu-a-sample-1"),
                    ("Sample 2", "/playground/sample2", "menu-a-sample-2")]
    header = Tag.DIV(
        Tag.DIV(
            Tag.IMAGE(src=url_for('static', filename=Theme.logo_filename),
                      alt="Potion Logo",
                      width=100,
                      height=100,
                      id="header-logo"),
            Tag.A(
                Tag.H1("Potion Playground"),
                href="/playground",
                id="main-page-link"),
            style={"display": "flex", "padding": "1rem 100px 0 0"},
            id="header-title-div"),
        Tag.UL(*[Tag.LI(header_button(title, href, button_id))
                 for title, href, button_id in menu_buttons]),
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
                     text_decoration="none")
    header.add_style("li",
                     display="flex")
    header.add_style("ul",
                     list_style_type="none",
                     display="flex",
                     flex_direction="row",
                     padding=0,
                     margin=0)

    return header
