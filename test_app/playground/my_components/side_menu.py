from flask import url_for, request
from potion.html_tag import Tag
from potion.jquery import JQuery
from .theme import Theme


def get_menu():
    menu = Tag.DIV(
        Tag.DIV(Tag.P("Menu Item 1"),
                Tag.P("Menu Item 2"),
                Tag.P("Menu Item 3"),
                id="side-menu-items"),
        Tag.BUTTON(">>",
                   on_click=JQuery.animate("#side-menu-panel", {"width": "20%"}, speed=700),
                   id="side-menu-expand-button",
                   style={"display": "none"}),
        Tag.BUTTON("<<",
                   on_click=JQuery.animate("#side-menu-panel", {"width": "5%"}, speed=700),
                   id="side-menu-collapse-button"),
        id="side-menu-panel")

    menu.add_style(width="20%",
                   display="flex",
                   flex_direction="row",
                   justify_content="space-between",
                   background_color="orange")
    menu.add_style("#side-menu-items",
                   display="flex",
                   flex_direction="column")
    menu.add_style("button",
                   height="3vh",
                   background_color="orangered",
                   border="none")
    menu.add_style("button:hover",
                   background_color="yellow")
    return menu
