from flask import Blueprint
from potion.tags import Tag
from potion.dom import HTMLDocBuilder
from potion.jquery import JQuery
from test_utils.driver import Driver
import time

test_api = Blueprint("test-ajax-fade", __name__)
test_url = "/test/ajax/fades/"


@test_api.route(test_url)
def dashboard():
    doc = HTMLDocBuilder(title="Testing JQuery Hide & Show Functions")

    doc.add_to_body(
        Tag.P("A paragraph", style={"background-color": "darkblue", "color": "white"}),
        Tag.P("Another paragraph", style={"background-color": "darkgreen", "color": "white"}),
        Tag.BUTTON("fade in",
                   id="in",
                   on_click=JQuery.fade_in("p")),
        Tag.BUTTON("fade out",
                   id="out",
                   on_click=JQuery.fade_out("p")),
        Tag.BUTTON("toggle fade",
                   id="toggle",
                   on_click=JQuery.fade_toggle("p")),
        Tag.BUTTON("half-fade",
                   id="to",
                   on_click=JQuery.fade_to("p", speed=0, opacity=.5))
    )
    return doc.build()


def get_visible_paragraphs(_driver):
    return [e for e in _driver.find_by_css("p") if e.is_displayed()]


def get_paragraph_opacity(_driver):
    return float(get_visible_paragraphs(_driver)[0].value_of_css_property("opacity"))


def test_jquery_fade_out_in(_driver: Driver):
    _driver.navigate(test_url)
    assert len(get_visible_paragraphs(_driver)) == 2

    _driver.click("#out")
    time.sleep(.5)
    assert len(get_visible_paragraphs(_driver)) == 0

    _driver.click("#in")
    _driver.click("#in")
    time.sleep(.5)
    assert len(get_visible_paragraphs(_driver)) == 2


def test_jquery_fade_toggle(_driver: Driver):
    _driver.navigate(test_url)
    assert len(get_visible_paragraphs(_driver)) == 2

    _driver.click("#toggle")
    time.sleep(.5)
    assert len(get_visible_paragraphs(_driver)) == 0

    _driver.click("#toggle")

    time.sleep(.5)
    assert len(get_visible_paragraphs(_driver)) == 2


def test_jquery_fade_to(_driver: Driver):
    _driver.navigate(test_url)
    assert get_paragraph_opacity(_driver) == 1

    _driver.click("#to")
    assert get_paragraph_opacity(_driver) == .5
