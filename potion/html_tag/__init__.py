from .base_tag import HTMLTagBuilder
from .button import HTMLButton
from .division import HTMLDivision
from .links import HTMLLink, HTMLHyperlink
from .horizontal_rule import HTMLHorizontalRule
from .line_break import HTMLLineBreak
from .paragraph import HTMLParagraph
from .script import HTMLScript
from .emphasis import HTMLEmphasis
from .lists import HTMLOrderedList, HTMLUnorderedList, HTMLListItem


class TAG:
    # Empty Tags
    br = HTMLLineBreak
    hr = HTMLHorizontalRule
    link = HTMLLink

    # Container Tags
    a = HTMLHyperlink
    p = HTMLParagraph
    em = HTMLEmphasis
    div = HTMLDivision
    script = HTMLScript
    button = HTMLButton

    # Lists
    ol = HTMLOrderedList
    ul = HTMLUnorderedList
    li = HTMLListItem
