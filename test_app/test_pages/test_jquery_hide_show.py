from flask import Blueprint, url_for
from potion.tags import Tag
from potion.dom import HTMLDocBuilder
from potion.jquery import JQuery
from test_utils.driver import Driver
import time

test_api = Blueprint("test-ajax-show-hide", __name__)
test_url = "/test/ajax/load-content/"


@test_api.route(test_url)
def dashboard():
    doc = HTMLDocBuilder(title="Testing JQuery Hide & Show Functions")

    doc.add_to_body(
        Tag.P("A paragraph"),
        Tag.P("Another paragraph"),
        Tag.BUTTON("hide paragraphs",
                   id="hide-button",
                   on_click=JQuery.hide("p")),
        Tag.BUTTON("show paragraphs",
                   id="show-button",
                   on_click=JQuery.show("p")),
        Tag.BUTTON("hide very slowly",
                   id="hide-very-slow",
                   on_click=JQuery.hide("p", speed=2000)),
        Tag.BUTTON("show fast",
                   id="show-fast",
                   on_click=JQuery.show("p", speed="fast")),
        Tag.BUTTON("toggle",
                   id="toggle",
                   on_click=JQuery.toggle("p"))
    )
    doc.add_stylesheet(href=url_for("static", filename="styles.css"))

    return doc.build()


def get_visible_paragraphs(_driver):
    return [e for e in _driver.find_by_css("p") if e.is_displayed()]


def test_jquery_hide_show_elements(_driver: Driver):
    _driver.navigate(test_url)
    assert len(get_visible_paragraphs(_driver)) == 2

    _driver.click("#hide-button")
    assert len(get_visible_paragraphs(_driver)) == 0

    _driver.click("#show-button")
    assert len(get_visible_paragraphs(_driver)) == 2


def test_jquery_hide_show_with_speed(_driver: Driver):
    _driver.navigate(test_url)
    assert len(get_visible_paragraphs(_driver)) == 2

    _driver.click("#hide-very-slow")
    assert len(get_visible_paragraphs(_driver)) == 2
    time.sleep(2)
    assert len(get_visible_paragraphs(_driver)) == 0

    _driver.click("#show-fast")
    assert len(get_visible_paragraphs(_driver)) == 2


def test_jquery_toggle(_driver: Driver):
    _driver.navigate(test_url)
    assert len(get_visible_paragraphs(_driver)) == 2

    _driver.click("#toggle")
    assert len(get_visible_paragraphs(_driver)) == 0

    _driver.click("#toggle")
    assert len(get_visible_paragraphs(_driver)) == 2
