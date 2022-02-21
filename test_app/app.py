from flask import Flask
from potion.html_doc import HTMLDocBuilder
from potion.html_tag import Tag
from blueprints import (test_global_css,
                        test_hyperlink_click,
                        test_jquery_hide_show,
                        test_hide_show_by_type)

app = Flask(__name__)
app.register_blueprint(test_global_css.test_api)
app.register_blueprint(test_hyperlink_click.test_api)
app.register_blueprint(test_jquery_hide_show.test_api)
app.register_blueprint(test_hide_show_by_type.test_api)


@app.route("/")
def test_pages():
    doc = HTMLDocBuilder("Test Page Index")

    test_links = [test_global_css.test_url,
                  test_hyperlink_click.test_urls[0],
                  test_jquery_hide_show.test_url,
                  test_hide_show_by_type.test_url]

    doc.add_to_body(
        Tag.UL(
            *[Tag.LI(Tag.A(link, href=link))
              for link in test_links]
        ))

    return doc.build()


if __name__ == "__main__":
    app.run()
    # url_for('static', filename='styles.css')
