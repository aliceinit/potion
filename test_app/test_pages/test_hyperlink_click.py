from flask import Blueprint, url_for
from potion.tags import Tag
from potion.dom import HTMLDocBuilder
from test_utils.driver import Driver

test_api = Blueprint("test-hyperlink-click", __name__)
test_urls = ["/test/hyperlink/source", "/test/hyperlink/dest"]


@test_api.route(test_urls[0])
def source():
    doc = HTMLDocBuilder(title="Testing Global CSS")
    doc.add_to_body(
        Tag.A("link text",
              href=test_urls[1],
              id="link"),
    )
    return doc.build()


@test_api.route(test_urls[1])
def destination():
    doc = HTMLDocBuilder(title="Hyperlink Destination")
    doc.add_to_body(
        Tag.P("DONE", id="done")
    )
    return doc.build()


def test_pass_static_css_to_page_builder(_driver: Driver):
    _driver.navigate(test_urls[0])
    _driver.click("#link")
    assert _driver.find_by_id("done") is not None
