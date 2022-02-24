from flask import url_for


class Colors:
    PRIMARY_MAIN = "#67B600"
    PRIMARY_LIGHT = "#DCEEC8"
    PRIMARY_DARK = "#437600"
    ACCENT_A_MAIN = ""
    ACCENT_A_DARK = ""
    ACCENT_A_LIGHT = ""
    ACCENT_B_MAIN = ""
    ACCENT_B_DARK = ""
    ACCENT_B_LIGHT = ""


class Theme:
    colors = Colors
    favicon_link = ""
    logo_link = "playground/images/logo.png"

    theme = None
    favicon_filename = "flask_potion_64.png"
    logo_filename = "flask_potion_256.png"
