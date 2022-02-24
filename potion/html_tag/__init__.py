from .base_tag import HTMLTagBuilder
from .button import HTMLButton
from .division import HTMLDivision
from .links import HTMLLink, HTMLHyperlink
from .headers import HTMLHeading1, HTMLHeading2, HTMLHeading3, HTMLHeading4, HTMLHeading5, HTMLHeading6
from .horizontal_rule import HTMLHorizontalRule
from .image import HTMLImage
from .line_break import HTMLLineBreak
from .paragraph import HTMLParagraph
from .script import HTMLScript
from .style import HTMLStyle
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
    STYLE = HTMLStyle
    IMAGE = HTMLImage

    # Lists
    OL = HTMLOrderedList
    UL = HTMLUnorderedList
    LI = HTMLListItem

    # Headings
    H1 = HTMLHeading1
    H2 = HTMLHeading2
    H3 = HTMLHeading3
    H4 = HTMLHeading4
    H5 = HTMLHeading5
    H6 = HTMLHeading6