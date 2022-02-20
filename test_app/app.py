from flask import Flask
from potion.html_doc import HTMLDocBuilder
from potion.html_tag import TAG
from blueprints import test_global_css, test_hyperlink_click

app = Flask(__name__)
app.register_blueprint(test_global_css.test_api)
app.register_blueprint(test_hyperlink_click.test_api)


@app.route("/")
def test_pages():
    doc = HTMLDocBuilder("Test Page Index")
    doc.add_to_body(
        TAG.ul(
            *[TAG.li(TAG.a(link, href=link))
              for link in [test_global_css.test_url,
                           test_hyperlink_click.test_urls[0]]]
        ))
    return doc.build()


if __name__ == "__main__":
    app.run()
    # url_for('static', filename='styles.css')
