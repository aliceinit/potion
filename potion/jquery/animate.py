import typing
from .jquery import JQueryFunctionBuilder, JQueryAction


def to_camel_case(text):
    s = text.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(text) == 0:
        return text
    return s[0] + ''.join(i.capitalize() for i in s[1:])


class JQueryAnimate(JQueryFunctionBuilder):
    def __init__(self, event: str, source: str, target: str,
                 params: typing.Dict,
                 speed: typing.Union[str, int] = None):
        super().__init__(event, source)

        args = [{to_camel_case(k): v for k, v in params.items()}]
        if speed:
            args.append(self.format_speed_arg(speed))
        self.steps = [JQueryAction(target, "animate", *args)]


def jquery_animate_partial(target_selector: str, params, speed=None):
    def partial(event: str, source: str) -> JQueryAnimate:
        return JQueryAnimate(event, source, target_selector, params, speed)

    return partial
