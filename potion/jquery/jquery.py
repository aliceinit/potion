import typing


class JQuerySelector:
    reserved= ["this", "document"]

    @classmethod
    def from_string(cls, selector: str) -> str:
        if selector in cls.reserved:
            return selector
        else:
            return f"\"{selector}\""


class JQueryAction:
    def __init__(self, target_selector: str, jqeuery_action: str, *args):
        self.target = JQuerySelector.from_string(target_selector)
        self.action = jqeuery_action
        self.args = args

    def build(self):
        return f"$({self.target}).{self.action}({self.args if self.args else ''})"


class JQueryFunctionBuilder:

    def __init__(self, event, source):
        self.source = JQuerySelector.from_string(source)
        self.event = event
        self.steps = []

    def add_steps(self, *steps: typing.Union["JQueryFunctionBuilder",
                                             JQueryAction]):
        for step in steps:
            print(f"Adding step {step}")
            self.steps.append(step)

    def add_jquery_action(self, target, action, *args):
        self.add_steps(JQueryAction(target, action, *args))

    def build(self):
        fn = f"$({self.source}).{self.event}(function(){{"
        print(f"all steps: {self.steps}")
        for step in self.steps:
            print(f"{type(step)}: -- {step}")
            fn += step.build()
        fn += "});"
        return fn
