import pytest
from potion.html_doc import HTMLDocBuilder
from potion.html_tag import TAG
from bs4 import BeautifulSoup


@pytest.mark.active
def test_basic_empty_page():
    page_title = "Test Page Title"
    page = HTMLDocBuilder(page_title)
    soup = BeautifulSoup(page.build(), 'html5lib')
    assert soup.find("title").string.strip() == page_title


@pytest.mark.active
def test_empty_tags():
    page = HTMLDocBuilder("test_empty_tags")
    page.add_tags([
        TAG.p(["paragraph: ",
               TAG.em(["the very first"]),
               " paragraph"]),
        TAG.br(),
        TAG.p("paragraph 2"),
        TAG.hr()
    ])
