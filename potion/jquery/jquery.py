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
                         "css",
                         "fadeIn",
                         "fadeOut",
                         "fadeTo",
                         "fadeToggle",
                         "hide",
                         "load",
                         "show",
                         "toggle",
                         "toggleClass"]

    def __init__(self, target_selector: str,
                 jquery_action: str,
                 *args,
                 callback: typing.Union["JQueryFunctionBuilder", None] = None):

        if jquery_action not in self.supported_actions:
            raise AttributeError(f"Invalid JQuery action: {jquery_action}")

        self.target = JQuerySelector.from_string(target_selector)
        self.action = jquery_action
        self.args = args
        self.callback = (callback
                         if isinstance(callback, JQueryFunctionBuilder) or callback is None
                         else callback("", ""))

    def build(self, include_target=True):
        if self.args:
            args = ', '.join([str(a) for a in self.args])
        else:
            args = ''

        fun = f"$({self.target})" if include_target else ""
        fun += f".{self.action}({args}"
        if self.callback:
            fun += f", function(){{{self.callback.build_steps()}}}"
        fun += ")"
        return fun


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
        fn += self.build_steps()
        fn += "});"
        return fn

    def build_steps(self):
        steps = ""
        for step in self.steps:
            steps += step.build()
        return steps
