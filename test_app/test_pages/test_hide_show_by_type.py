from flask import Blueprint, url_for
from potion.tags import Tag
from potion.dom import HTMLDocBuilder
from potion.jquery import JQuery
from test_utils.driver import Driver
import time

test_api = Blueprint("test-ajax-page-functions", __name__)
test_url = "/test/ajax/page-functions/"


@test_api.route(test_url)
def dashboard():
    doc = HTMLDocBuilder(title="Testing JQuery Hide & Show Functions")

    doc.add_to_body(
        Tag.P("A paragraph", id="click-me"),
        Tag.P("Another paragraph"),
        *[Tag.BUTTON(f"refresh-{i + 1}", html_class="refresh-button") for i in range(10)]
    )
    doc.add_stylesheet(href=url_for("static", filename="styles.css"))
    doc.add_function(source="p",
                     event="click",
                     jquery_partial=JQuery.hide("this", speed=1000))
    doc.add_function(source=".refresh-button",
                     event="click",
                     jquery_partial=JQuery.show("p"))

    return doc.build()


def get_visible_paragraphs(_driver):
    return [e for e in _driver.find_by_css("p") if e.is_displayed()]


def test_jquery_hide_show_by_type(_driver: Driver):
    _driver.navigate(test_url)
    assert len(get_visible_paragraphs(_driver)) == 2

    _driver.click("#click-me")
    time.sleep(1)
    assert len(get_visible_paragraphs(_driver)) == 1

    _driver.click("button")
    assert len(get_visible_paragraphs(_driver)) == 2
