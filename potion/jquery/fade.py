import typing
from .jquery import JQueryFunctionBuilder, JQueryAction


class JQueryFadeIn(JQueryFunctionBuilder):
    def __init__(self, event: str, source: str, target: str,
                 speed: typing.Union[str, int] = None,
                 callback: typing.Callable = None):
        super().__init__(event, source)

        args = []
        if speed:
            args.append(self.format_speed_arg(speed))
        self.steps = [JQueryAction(target, "fadeIn", *args, callback=callback)]


def jquery_fadein_partial(target_selector: str, speed=None, callback=None):
    def partial(event: str, source: str) -> JQueryFadeIn:
        return JQueryFadeIn(event, source, target_selector, speed, callback)

    return partial


class JQueryFadeOut(JQueryFunctionBuilder):
    def __init__(self, event: str, source: str, target: str,
                 speed: typing.Union[str, int] = None,
                 callback: typing.Callable = None):
        super().__init__(event, source)

        args = []
        if speed:
            args.append(self.format_speed_arg(speed))
        self.steps = [JQueryAction(target, "fadeOut", *args, callback=callback)]


def jquery_fadeout_partial(target_selector: str, speed=None, callback=None):
    def partial(event: str, source: str) -> JQueryFadeOut:
        return JQueryFadeOut(event, source, target_selector, speed, callback)

    return partial


class JQueryFadeToggle(JQueryFunctionBuilder):
    def __init__(self, event: str, source: str, target: str,
                 speed: typing.Union[str, int] = None,
                 callback: typing.Callable = None):
        super().__init__(event, source)

        args = []
        if speed:
            args.append(self.format_speed_arg(speed))
        self.steps = [JQueryAction(target, "fadeToggle", *args, callback=callback)]


def jquery_fadetoggle_partial(target_selector: str, speed=None, callback=None):
    def partial(event: str, source: str) -> JQueryFadeToggle:
        return JQueryFadeToggle(event, source, target_selector, speed, callback)

    return partial


class JQueryFadeTo(JQueryFunctionBuilder):
    def __init__(self, event: str, source: str, target: str,
                 speed: typing.Union[str, int],
                 opacity: typing.Union[int, float],
                 callback: typing.Callable = None):
        super().__init__(event, source)

        if not isinstance(opacity, (int, float)) or not (0 <= opacity <= 1):
            raise AttributeError(f"Invalid value for opacity: {opacity}")

        args = [self.format_speed_arg(speed), opacity]
        self.steps = [JQueryAction(target, "fadeTo", *args, callback=callback)]


def jquery_fadeto_partial(target_selector: str, speed, opacity, callback=None):
    def partial(event: str, source: str) -> JQueryFadeTo:
        return JQueryFadeTo(event, source, target_selector, speed, opacity, callback)

    return partial
