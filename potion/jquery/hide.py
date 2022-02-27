import typing

from .jquery import JQueryFunctionBuilder, JQueryAction


class JQueryHide(JQueryFunctionBuilder):

    def __init__(self, event: str, source: str, target: str,
                 speed: typing.Union[str, int] = None):
        super().__init__(event, source)

        args = []
        if speed:
            args.append(self.format_speed_arg(speed))
        self.steps = [JQueryAction(target, "hide", *args)]


def jquery_hide_partial(target_selector: str, speed=None):
    def partial(event: str, source: str) -> JQueryHide:
        return JQueryHide(event, source, target_selector, speed)

    return partial


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


class JQueryToggle(JQueryFunctionBuilder):
    def __init__(self, event: str, source: str, target: str,
                 speed: typing.Union[str, int] = None):
        super().__init__(event, source)
        args = []
        if speed:
            args.append(self.format_speed_arg(speed))
        self.steps = [JQueryAction(target, "toggle", *args)]


def jquery_toggle_partial(target_selector: str, speed=None):
    def partial(event: str, source: str) -> JQueryToggle:
        return JQueryToggle(event, source, target_selector, speed)

    return partial
