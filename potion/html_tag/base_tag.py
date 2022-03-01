import random
import string
import typing

from potion.styles import CSSBlock
from potion.jquery import JQuery


class HTMLTagBuilder:

    def __init__(self, name, is_container=True, children=None, id=None,
                 html_class=None, style=None, on_click=None, **kwargs):
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
        if style:
            self.add_style(**style)
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

    def add_style(self, selector=None, **kwargs):
        block_selector = f"#{self.id}"
        if selector and selector.startswith(":"):
            block_selector += selector
        elif selector:
            block_selector += f" {selector}"
        self.styles.append(CSSBlock(block_selector, **kwargs))

    def on_click(self, partial):
        """
        Takes a partial function OR a list of partial functions
        and calls them with the 'click' event and the current tag's id
        Adds the resulting JQuery functions to the Tag class's function list
        :param partial: A function or list of functions that return JQueryFunctions
        :return: None
        """

        partial_list = [partial] if callable(partial) else partial

        for fun in partial_list:
            self.functions.append(fun("click", f"#{self.id}"))
