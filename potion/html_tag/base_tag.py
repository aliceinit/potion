class HTMLTagBuilder:
    __slots__ = ("name", "is_container", "children", "html_class", "id", "xml_prop_names")

    def __init__(self, name, is_container=True, children=None, id=None,
                 html_class=None, **kwargs):
        self.name = name
        self.is_container = is_container
        if isinstance(children, str):
            self.children = [children]
        elif children is not None:
            self.children = [c for c in children]  # Check that children is iterable
        else:
            self.children = []

        self.html_class = set()
        if isinstance(html_class, str):
            for str_class in html_class.split():
                self.html_class.add(str_class)
        elif html_class is not None:
            for c in html_class:
                self.html_class.add(c)

        self.id = id
        self.xml_prop_names = []

    def build_xml_props(self):
        props = ""
        if self.html_class:
            props += f"class=\"{' '.join(self.html_class)}\""
        if self.id:
            props += f"id=\"{self.id}\""

        for prop_name in ["rel", "href", "type"]:
            try:
                prop_value = self.__getattribute__(prop_name)
                if prop_value:
                    props += f"{prop_name}=\"{prop_value}\""
            except AttributeError:
                pass

        return props

    def build(self):

        if not self.is_container:
            return f"<{self.name} {self.build_xml_props()}/>"
        else:
            tag = f"<{self.name} {self.build_xml_props()}>"
            for child_tag in self.children:
                if isinstance(child_tag, str):
                    tag += child_tag
                elif isinstance(child_tag, HTMLTagBuilder):
                    tag += child_tag.build()
                else:
                    raise ValueError(f"Cannot render HTML Tag Child of type {type(child_tag)}: {child_tag}")
            tag += f"</{self.name}>"
            return tag

    def add_child(self, child):
        self.children.append(child)
