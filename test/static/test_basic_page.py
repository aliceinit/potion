import pytest
from potion.dom import HTMLDocBuilder
from potion.tags import Tag
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
    page.add_to_body(
        Tag.P(["paragraph: ",
               Tag.EM(["the very first"]),
               " paragraph"]),
        Tag.BR(),
        Tag.P("paragraph 2"),
        Tag.HR()
    )
