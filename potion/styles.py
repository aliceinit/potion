class CSSBlock:

    def __init__(self, selector, **kwargs):
        self.selector = selector
        self.declaration = {k.replace("_", "-"): v for k, v in kwargs.items()}

    def build(self):
        print("HELLO??")
        css_block = f"{self.selector} {{"
        for property, value in self.declaration.items():
            css_block += f" {property}: {value};"
        css_block += " }"

        return css_block
