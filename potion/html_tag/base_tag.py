import random
import string
from potion.jquery.jquery import JQuerySelector


class HTMLTagBuilder:
    __slots__ = ("name", "is_container", "children", "html_class", "id", "xml_prop_names",
                 "functions", "styles")

    def __init__(self, name, is_container=True, children=None, id=None,
                 html_class=None, on_click=None, **kwargs):
        self.name = name
        self.is_container = is_container
        self.functions = []
        self.styles = []
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

        self.id = id or (self.name + "-" + "".join([random.choice(string.ascii_letters) for _ in range(10)]))
        self.xml_prop_names = []
        if on_click:
            self.on_click(on_click)

    def build_xml_props(self):
        props = ""
        if self.html_class:
            props += f"class=\"{' '.join(self.html_class)}\""
        if self.id:
            props += f"id=\"{self.id}\""

        for prop_name in self.xml_prop_names:
            try:
                prop_value = self.__getattribute__(prop_name)
                if prop_value:
                    props += f"{prop_name}=\"{prop_value}\""
            except AttributeError:
                pass

        return props

    def build(self):

        # Collect jquery & styles tied to element IDs
        functions_by_id = self.functions
        styles_by_id = self.styles

        if not self.is_container:
            tag = f"<{self.name} {self.build_xml_props()}/>"
        else:
            tag = f"<{self.name} {self.build_xml_props()}>"
            for child in self.children:
                if isinstance(child, str):
                    tag += child
                elif isinstance(child, HTMLTagBuilder):
                    child_tag, child_functions, child_styles = child.build()
                    tag += child_tag
                    functions_by_id += [f for f in child_functions if f is not None]
                    styles_by_id += child_styles
                else:
                    raise ValueError(f"{self.name}.{self.id}: Cannot add child of type {type(child)}: {child}")
            tag += f"</{self.name}>"

        return tag, functions_by_id, styles_by_id

    def add_child(self, child):
        self.children.append(child)

    def on_click(self, partial_fn):
        self.functions.append(partial_fn("click", f"#{self.id}"))
        print(self.functions)
