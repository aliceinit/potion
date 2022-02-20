import typing

from .jquery import JQueryFunctionBuilder, JQuerySelector
from .hide import jquery_hide_partial


class JQuery:
    """
    Returns a function that:
        - takes a source-selector and event
        - returns a JSFunctionBuilder Object

    Intended usage -- pass to an event_listener in an HTMLTagBuilder:
        TAG.button(on_click=JQuery.hide())

     This is equivalent to:
        hide_fn: JSFunctionBuilder = JQuery.hide()(source="#hide-button", "click")
    """

    document_ready = lambda: JQueryFunctionBuilder("ready", "document")

    # JQuery Function Partials, requiring source-selector + event-name
    hide = jquery_hide_partial
