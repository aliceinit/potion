from flask import Blueprint, url_for
from potion.html_tag import TAG
from potion.html_doc import HTMLDocBuilder
from test_utils.driver import Driver

test_api = Blueprint("test-global-css", __name__)
test_url = "/test/css/global_css/"


@test_api.route(test_url)
def dashboard():
    doc = HTMLDocBuilder(title="Testing Global CSS")
    doc.add_to_body(
        TAG.p("This paragraph is red and white",
              html_class="global-colour",
              id="first-paragraph"),
        TAG.em(TAG.p("another paragraph, emphasized"),
               TAG.p("and another"))
    )
    doc.add_stylesheet(href=url_for("static", filename="styles.css"))
    return doc.build()


def test_pass_static_css_to_page_builder(_driver: Driver):
    _driver.navigate(test_url)
    paragraphs = _driver.find_by_css("#first-paragraph")
    first_paragraph = paragraphs[0]
    color = first_paragraph.value_of_css_property("color")
    background_color = first_paragraph.value_of_css_property("background-color")
    # color = white
    assert color == "rgb(255, 255, 255)"
    # background_color = red
    assert background_color == "rgb(255, 0, 0)"
