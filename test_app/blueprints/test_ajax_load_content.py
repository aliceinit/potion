from flask import Blueprint, url_for
from potion.html_tag import TAG
from potion.html_doc import HTMLDocBuilder
from potion.jquery import JQuery, JQuerySelector
from test_utils.driver import Driver

test_api = Blueprint("test-ajax-load-content", __name__)
test_url = "/test/ajax/load-content/"


@test_api.route(test_url)
def dashboard():
    doc = HTMLDocBuilder(title="Testing Global CSS")
    doc.add_to_body(
        TAG.p("A paragraph"),
        TAG.p("Another paragraph"),
        TAG.button(
            "hide paragraphs",
            id="hide-button",
            on_click=JQuery.hide("p")
        )
    )

    doc.add_stylesheet(href=url_for("static", filename="styles.css"))

    return doc.build()


def test_jquery_hide_elements(_driver: Driver):
    def get_visible_paragraphs():
        return [e for e in _driver.find_by_css("p") if e.is_displayed()]
    _driver.navigate(test_url)
    assert len(get_visible_paragraphs()) == 2

    _driver.click("hide-button")
    assert len(get_visible_paragraphs()) == 0
