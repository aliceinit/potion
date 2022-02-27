from flask import Flask
from potion.html_doc import HTMLDocBuilder
from potion.html_tag import Tag
from playground import playground
from test_pages import (test_global_css,
                        test_hyperlink_click,
                        test_jquery_hide_show,
                        test_hide_show_by_type,
                        test_jquery_fade)

app = Flask(__name__)
app.register_blueprint(playground.playground_api)
app.register_blueprint(test_global_css.test_api)
app.register_blueprint(test_hyperlink_click.test_api)
app.register_blueprint(test_jquery_hide_show.test_api)
app.register_blueprint(test_hide_show_by_type.test_api)
app.register_blueprint(test_jquery_fade.test_api)


@app.route("/")
def test_pages():
    doc = HTMLDocBuilder("Test Page Index")

    test_links = {"Playground": "/playground",
                  "External Stylesheets": test_global_css.test_url,
                  "Hyperlink Navigation": test_hyperlink_click.test_urls[0],
                  "JQuery Hide/Show": test_jquery_hide_show.test_url,
                  "JQuery Multi-Selectors": test_hide_show_by_type.test_url,
                  "JQuery Fades": test_jquery_fade.test_url}

    doc.add_to_body(
        Tag.UL(
            *[Tag.LI(Tag.A(name, href=link))
              for name, link in test_links.items()]
        ))

    return doc.build()


if __name__ == "__main__":
    app.run()
