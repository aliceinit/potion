from potion.html_tag import Tag
from potion.jquery import JQuery
from .theme import Theme


def get_numbered_menu_item(number, title):
    return Tag.DIV(Tag.P(str(number), html_class="menu-number", style={"font-size": "2em"}),
                   Tag.P(f" : {title}", html_class="menu-title",
                         style={"font-size": "2rem", "min-width": "15%"}),
                   style={"display": "flex"})


def get_menu():
    menu_items = ["Sample menu item",
                  "Another menu",
                  "???",
                  "also a menu"]
    menu = Tag.DIV(
        Tag.DIV(*[get_numbered_menu_item(n, title) for n, title in enumerate(menu_items)],
                id="side-menu-items"),
        Tag.BUTTON(">>",
                   on_click=[
                       JQuery.animate("#side-menu-panel", {"width": "20%"}, speed=300,
                                      callback=JQuery.show(".menu-title")),
                       JQuery.hide("this"),
                       JQuery.show("#side-menu-collapse-button")
                       # JQuery.show(".menu-title")
                   ],
                   id="side-menu-expand-button",
                   style={"display": "none"}),
        Tag.BUTTON("<<",
                   on_click=[
                       JQuery.animate("#side-menu-panel", {"width": "5%"}, speed=300),
                       JQuery.hide("this"),
                       JQuery.hide(".menu-title"),
                       JQuery.show("#side-menu-expand-button")
                   ],
                   id="side-menu-collapse-button"),
        id="side-menu-panel")

    menu.add_style(width="20%",
                   display="flex",
                   flex_direction="row",
                   justify_content="space-between",
                   padding="1em",
                   background_color="orange")
    menu.add_style("#side-menu-items",
                   display="flex",
                   flex_direction="column")
    menu.add_style("button",
                   height="4vh",
                   font_size="2rem",
                   background_color="orangered",
                   border="none"),
    menu.add_style("button:hover",
                   background_color="yellow")
    return menu
