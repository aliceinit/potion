import pytest
from potion.html_doc import HTMLDocBuilder
from potion.html_tag import TAG
from potion.styles import CSSBlock
from bs4 import BeautifulSoup


@pytest.mark.active
def test_basic_page_from_flask(app):
    page_title = "LIVE PAGE TEST 1"

    @app.route("/")
    def test_page():
        page = HTMLDocBuilder(page_title)
        page.add_to_body(
            TAG.p("paragraph: ",
                  TAG.em("the very first"),
                  " paragraph"),
            TAG.br(),
            TAG.p("paragraph 2"),
            TAG.hr()
        )
        return page.build()

    client = app.test_client()

    soup = BeautifulSoup(client.get("/").get_data(), "html5lib")
    assert soup.find("title").text.strip() == page_title


@pytest.mark.active
def test_page_with_global_css(app):
    page_title = "LIVE PAGE TEST 2"

    @app.route("/static/global.css")
    def test_css():
        def build_css():
            return CSSBlock(".test-class", color="red").build()

        return app.response_class(build_css(), mimetype="text/css")

    @app.route("/")
    def test_page():
        page = HTMLDocBuilder(page_title)
        page.add_to_body(TAG.p("This is a paragraph", html_class="test-class"))
        page.add_stylesheet("/static/global.css")
        return page.build()

    client = app.test_client()

    soup = BeautifulSoup(client.get("/").get_data(), "html5lib")
    assert soup.find("title").text.strip() == page_title
