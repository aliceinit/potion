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


class Tag:
    # Empty Tags
    BR = HTMLLineBreak
    HR = HTMLHorizontalRule
    LINK = HTMLLink

    # Container Tags
    A = HTMLHyperlink
    P = HTMLParagraph
    EM = HTMLEmphasis
    DIV = HTMLDivision
    SCRIPT = HTMLScript
    BUTTON = HTMLButton

    # Lists
    OL = HTMLOrderedList
    UL = HTMLUnorderedList
    LI = HTMLListItem
