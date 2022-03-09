from potion.tags import Tag

CONTENT_CONTAINER_ID = "content-container"


def get_content_container():
    return Tag.DIV(get_content_text("0"),
                   id=CONTENT_CONTAINER_ID,
                   style={"flex": "1",
                          "border": "black solid 1px",
                          "padding": "1em"})


def get_content_text(selection: str):
    content_text = {"0": "hello",
                    "1": "another peice of text and stuff",
                    "2": "more text is here",
                    "3": "last but not least"}
    return Tag.P(content_text.get(selection, "Bad selection..."))

