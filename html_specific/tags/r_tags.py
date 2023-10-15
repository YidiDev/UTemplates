from html_specific.base import BaseHTMLElement


class RubyParenthesesElement(BaseHTMLElement):
    """
    RubyParenthesesElement Class extends BaseHTMLElement to represent the HTML <rp> element.

    HTML Use Cases:
    ---------------
    The HTML <rp> element is used to provide parentheses for the ruby text in a ruby annotation.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    # Create a RubyParenthesesElement
    >>> rp_elem = RubyParenthesesElement()

    # Convert it to an HTML string
    >>> print(rp_elem.to_string())
    <rp></rp>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new RubyParenthesesElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("rp", **kwargs)


class RubyTextElement(BaseHTMLElement):
    """
    RubyTextElement Class extends BaseHTMLElement to represent the HTML <rt> element.

    HTML Use Cases:
    ---------------
    The HTML <rt> element is used to provide the ruby text component of a ruby annotation.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    # Create a RubyTextElement
    >>> rt_elem = RubyTextElement()

    # Convert it to an HTML string
    >>> print(rt_elem.to_string())
    <rt></rt>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new RubyTextElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("rt", **kwargs)


class RubyElement(BaseHTMLElement):
    """
    RubyElement Class extends BaseHTMLElement to represent the HTML <ruby> element.

    HTML Use Cases:
    ---------------
    The HTML <ruby> element is used to specify a ruby annotation, which is used for phonetic
    annotations in East Asian typography.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    # Create a RubyElement
    >>> ruby_elem = RubyElement()

    # Convert it to an HTML string
    >>> print(ruby_elem.to_string())
    <ruby></ruby>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new RubyElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("ruby", **kwargs)
