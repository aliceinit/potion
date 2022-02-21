import typing
from .jquery import JQueryFunctionBuilder, JQueryAction


class JQueryShow(JQueryFunctionBuilder):
    def __init__(self, event: str, source: str, target: str,
                 speed: typing.Union[str, int] = None):
        super().__init__(event, source)
        args = []
        if speed:
            args.append(self.format_speed_arg(speed))
        self.steps = [JQueryAction(target, "show", *args)]


def jquery_show_partial(target_selector: str, speed=None):
    def partial(event: str, source: str) -> JQueryShow:
        return JQueryShow(event, source, target_selector, speed)

    return partial
