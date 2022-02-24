from flask import Blueprint, url_for
from potion.html_tag import Tag

from .my_components.base import get_doc_with_header

playground_api = Blueprint("playground", __name__)


@playground_api.route("/playground")
def playground():
    """
    Not part of tests
    A place to play & experiment with new library functions for manual testing
    """
    doc = get_doc_with_header("Playground")
    doc.add_to_body(
        Tag.H2("Playground Main Page"),
        Tag.P("This is a place to play with the potion library")
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
