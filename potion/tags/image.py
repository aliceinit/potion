from .base_tag import HTMLTagBuilder


class HTMLImage(HTMLTagBuilder):

    def __init__(self, **kwargs):
        super().__init__("image", is_container=False, **kwargs)
        self.src = kwargs.get("src")
        if not self.src:
            raise AttributeError("Missing required parameter 'src'")
        self.alt = kwargs.get("alt")
        if not self.alt:
            raise AttributeError("Missing required parameter 'alt")

        self.width = kwargs.get("width")
        self.height = kwargs.get("height")

        self.xml_prop_names += ["alt", "src", "width", "height"]
