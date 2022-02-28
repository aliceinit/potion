import typing


class JQuerySelector:
    reserved = ["this", "document"]

    @classmethod
    def from_string(cls, selector: str) -> str:
        if selector in cls.reserved:
            return selector
        else:
            return f"\"{selector}\""


class JQueryAction:
    supported_actions = ["animate",
                         "fadeIn",
                         "fadeOut",
                         "fadeTo",
                         "fadeToggle",
                         "hide",
                         "show",
                         "toggle"]

    def __init__(self, target_selector: str,
                 jquery_action: str,
                 *args):

        if jquery_action not in self.supported_actions:
            raise AttributeError(f"Invalid JQuery action: {jquery_action}")

        self.target = JQuerySelector.from_string(target_selector)
        self.action = jquery_action
        self.args = args

    def build(self):
        if self.args:
            args = ', '.join([str(a) for a in self.args])
        else:
            args = ''

        return f"$({self.target}).{self.action}({args})"


class JQueryFunctionBuilder:

    def __init__(self, event, source):
        self.source = JQuerySelector.from_string(source)
        self.event = event
        self.steps = []

    def add_steps(self, *steps: typing.Union["JQueryFunctionBuilder",
                                             JQueryAction]):
        for step in steps:
            self.steps.append(step)

    def add_jquery_action(self, target, action, *args):
        self.add_steps(JQueryAction(target, action, *args))

    @staticmethod
    def format_speed_arg(speed):
        if speed is not None:
            if speed in ["slow", "fast"]:
                return f'"{speed}"'
            elif isinstance(speed, int):
                return speed
            else:
                raise AttributeError(f"Invalid option {speed} for speed. Must be 'slow', 'fast' or milliseconds (int)")

    def build(self):
        fn = f"$({self.source}).{self.event}(function(){{"
        for step in self.steps:
            fn += step.build()
        fn += "});"
        return fn
