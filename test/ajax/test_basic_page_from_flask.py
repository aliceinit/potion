import pytest
from flask import url_for
from potion.html_doc import HTMLDocBuilder
from potion.html_tag import TAG
from bs4 import BeautifulSoup


@pytest.mark.active
def test_basic_page_from_flask(app):
    page_title = "LIVE PAGE TEST 1"

    @app.route("/")
    def test_page():
        page = HTMLDocBuilder(page_title)
        page.add_tags([
            TAG.p(["paragraph: ",
                   TAG.em(["the very first"]),
                   " paragraph"]),
            TAG.br(),
            TAG.p("paragraph 2"),
            TAG.hr()])
        return page.build()

    client = app.test_client()

    soup = BeautifulSoup(client.get("/").get_data(), "html5lib")
    assert soup.find("title").text.strip() == page_title


@pytest.mark.active
def test_second_page_from_flask(app):
    page_title = "LIVE PAGE TEST 2"

    @app.route("/")
    def test_page():
        page = HTMLDocBuilder(page_title)
        page.add_to_body(TAG.p("Test a second page"))
        return page.build()

    client = app.test_client()

    soup = BeautifulSoup(client.get("/").get_data(), "html5lib")
    assert soup.find("title").text.strip() == page_title
