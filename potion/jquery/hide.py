from .jquery import JQueryFunctionBuilder, JQueryAction, JQuerySelector


class JQueryHide(JQueryFunctionBuilder):

    def __init__(self, event:str, source:str, target:str):
        super().__init__(event, source)
        self.steps = [JQueryAction(target_selector=target,
                                   jqeuery_action="hide")]


def jquery_hide_partial(target_selector: str):
    def partial(event: str, source: str) -> JQueryHide:
        return JQueryHide(event, source, target_selector)

    return partial
