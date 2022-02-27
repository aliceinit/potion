import typing

from .jquery import JQueryFunctionBuilder, JQuerySelector
from .hide import (jquery_hide_partial,
                   jquery_show_partial,
                   jquery_toggle_partial)
from .fade import (jquery_fadein_partial,
                   jquery_fadeout_partial,
                   jquery_fadetoggle_partial,
                   jquery_fadeto_partial)


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
    show = jquery_show_partial
    toggle = jquery_toggle_partial
    fade_in = jquery_fadein_partial
    fade_out = jquery_fadeout_partial
    fade_toggle = jquery_fadetoggle_partial
    fade_to = jquery_fadeto_partial
