from potion.tags import Tag
from potion.jquery import JQuery
from .content_container import CONTENT_CONTAINER_ID


def get_menu_items(menu_titles, selected_index=0):
    items = []
    for number, title in enumerate(menu_titles):

        menu_item = Tag.DIV(
            Tag.P(str(number), html_class="menu-number"),
            Tag.P(f" : {title}", html_class="menu-title"),
            on_click=[JQuery.toggle_class(".side-menu-selected", "side-menu-unselected"),
                      JQuery.toggle_class(".side-menu-selected", "side-menu-selected"),
                      JQuery.toggle_class("this", "side-menu-selected"),
                      JQuery.toggle_class("this", "side-menu-unselected"),
                      JQuery.load(f"#{CONTENT_CONTAINER_ID}",
                                  f"/playground/menu/{number}")],
            style={"font-size": "1.5em",
                   "display": "flex",
                   "padding": "0 .75rem",
                   "margin": "0 .75rem",
                   "border-color": "orangered",
                   "border-width": "0 5px 0 0"},
            html_class="side-menu-item")
        menu_item.add_style(":hover",
                            color="orangered")
        if number == selected_index:
            menu_item.add_class("side-menu-selected")
        else:
            menu_item.add_class("side-menu-unselected")
        items.append(menu_item)
    side_menu = Tag.DIV(*items,
                        id="side-menu-items")
    side_menu.add_style(display="flex",
                        flex_direction="column")
    side_menu.add_style(".side-menu-unselected",
                        border_style="hidden")
    side_menu.add_style(".side-menu-selected",
                        color="orangered",
                        border_style="solid")
    return side_menu


def get_menu(selection=0):
    menu_items = ["Sample menu item",
                  "Another menu",
                  "???",
                  "also a menu"]
    menu = Tag.DIV(
        get_menu_items(menu_items, selection),
        Tag.BUTTON(">>",
                   on_click=[
                       JQuery.animate("#side-menu-panel", {"width": "20%"}, speed=300,
                                      callback=JQuery.show(".menu-title")),
                       JQuery.hide("this"),
                       JQuery.show("#side-menu-collapse-button")
                   ],
                   id="side-menu-expand-button",
                   style={"display": "none"}),
        Tag.BUTTON("<<",
                   on_click=[
                       JQuery.animate("#side-menu-panel", {"width": "6%"}, speed=300),
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
                   background_color="gold")
    menu.add_style("button",
                   height="4vh",
                   font_size="2rem",
                   background_color="orangered",
                   border="none"),
    menu.add_style("button:hover",
                   background_color="yellow")
    return menu
