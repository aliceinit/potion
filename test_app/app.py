from flask import Flask
from potion.html_doc import HTMLDocBuilder
from potion.html_tag import TAG
from blueprints import test_global_css

app = Flask(__name__)
app.register_blueprint(test_global_css.test_api)


@app.route("/")
def test_pages():
    doc = HTMLDocBuilder("Test Page Index")
    doc.add_tags([
        TAG.a(test_global_css.test_url, href=test_global_css.test_url)
    ])
    return doc.build()


if __name__ == "__main__":
    app.run()
    # url_for('static', filename='styles.css')
