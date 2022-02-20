from .jquery import JQueryFunctionBuilder, JQueryAction


class JQueryShow(JQueryFunctionBuilder):
    def __init__(self, event: str, source: str, target: str):
        super().__init__(event, source)
        self.steps = [JQueryAction(target_selector=target,
                                   jqeuery_action="show")]


def jquery_show_partial(target_selector: str):
    def partial(event: str, source: str) -> JQueryShow:
        return JQueryShow(event, source, target_selector)

    return partial
