from .base_tag import HTMLTagBuilder


class HTMLLink(HTMLTagBuilder):
    rel_values = ["alternate",
                  "author",
                  "dns-prefetch",
                  "help",
                  "icon",
                  "license",
                  "next",
                  "pingback",
                  "preconnect",
                  "prefetch",
                  "preload",
                  "prerender",
                  "prev",
                  "search",
                  "stylesheet"]

    def __init__(self, *children, **kwargs):
        self.rel = kwargs.get("rel")
        if self.rel not in self.rel_values:
            raise AttributeError(f"Invalid value for rel: '{self.rel}'")
        super().__init__("link", is_container=False)
        self.href = kwargs.get("href")
        self.type = kwargs.get("type")
        self.xml_prop_names += ["href", "type", "rel"]


class HTMLHyperlink(HTMLTagBuilder):

    def __init__(self, *children, **kwargs):
        super().__init__("a", is_container=True, children=children, **kwargs)
        self.href = kwargs.get("href")
        self.xml_prop_names += ["href"]
