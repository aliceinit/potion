import typing
from .jquery import JQueryFunctionBuilder, JQueryAction


class JQueryCSS(JQueryFunctionBuilder):
    def __init__(self, event: str, source: str, target: str, *params):
        super().__init__(event, source)
        self.steps = [JQueryAction(target, "css", *params)]


def jquery_css_partial(target_selector: str, *params):
    def partial(event: str, source: str) -> JQueryCSS:
        return JQueryCSS(event, source, target_selector, *params)

    return partial
