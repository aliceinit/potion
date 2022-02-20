from .base_tag import HTMLTagBuilder
from .link import HTMLLink
from .horizontal_rule import HTMLHorizontalRule
from .hyperlink import HTMLHyperlink
from .line_break import HTMLLineBreak
from .paragraph import HTMLParagraph
from .emphasis import HTMLEmphasis


class TAG:
    # Empty Tags
    br = HTMLLineBreak
    hr = HTMLHorizontalRule
    # Container Tags
    a = HTMLHyperlink
    p = HTMLParagraph
    em = HTMLEmphasis
    link = HTMLLink
