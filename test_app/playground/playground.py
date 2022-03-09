from flask import Blueprint
from potion.tags import Tag

from .my_components.base import get_doc_with_header
from .my_components.side_menu import get_menu
from .my_components.content_container import get_content_text, get_content_container

playground_api = Blueprint("playground", __name__)


@playground_api.route("/playground")
def playground():
    """
    Not part of tests
    A place to play & experiment with new library functions for manual testing
    """
    doc = get_doc_with_header("Playground")
    doc.add_to_body(
        Tag.DIV(get_menu(),
                get_content_container(),
                style={"display": "flex",
                       "flex": "1"})
    )
    return doc.build()


@playground_api.route("/playground/sample")
def sample1():
    doc = get_doc_with_header("Sample 1")
    doc.add_to_body(
        Tag.H2("Sample 1")
    )
    return doc.build()


@playground_api.route("/playground/sample2")
def sample2():
    doc = get_doc_with_header("Sample 2")
    doc.add_to_body(
        Tag.H2("Sample 2")
    )
    return doc.build()


@playground_api.route("/playground/menu/<menu_selection>")
def get_content(menu_selection: str):
    return get_content_text(menu_selection).build()[0]
