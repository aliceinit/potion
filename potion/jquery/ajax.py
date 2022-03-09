import typing
from .jquery import JQueryFunctionBuilder, JQueryAction


class JQueryLoad(JQueryFunctionBuilder):
    def __init__(self, event: str, source: str, target: str, url: str):
        super().__init__(event, source)
        self.steps = [JQueryAction(target, "load", f'"{url}"')]


def jquery_load_partial(target_selector: str, url: str):
    # TODO: support request params & callback
    def partial(event: str, source: str) -> JQueryLoad:
        return JQueryLoad(event, source, target_selector, url)

    return partial
