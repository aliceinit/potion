import typing
from .jquery import JQueryFunctionBuilder, JQueryAction


class JQueryToggleClass(JQueryFunctionBuilder):
    def __init__(self, event: str, source: str, target: str, class_name: str):
        super().__init__(event, source)
        self.steps = [JQueryAction(target, "toggleClass", f'"{class_name}"')]


def jquery_toggle_class_partial(target_selector: str, class_name):
    def partial(event: str, source: str) -> JQueryToggleClass:
        return JQueryToggleClass(event, source, target_selector, class_name)

    return partial
