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

    def __init__(self, rel, href=None, type=None):
        if rel not in self.rel_values:
            raise AttributeError(f"Invalid value for rel: '{rel}'")
        super().__init__("link", is_container=False)
        self.rel = rel
        self.href = href
        self.type = type
        self.xml_prop_names += ["rel", "href", "type"]
