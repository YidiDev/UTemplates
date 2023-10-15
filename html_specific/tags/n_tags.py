from html_specific.base import BaseHTMLElement


class NavigationElement(BaseHTMLElement):
    """
    NavigationElement Class extends BaseHTMLElement to represent the HTML <nav> element.

    HTML Use Cases:
    ---------------
    The HTML <nav> element represents a section of a page that contains navigation links,
    such as menus, tables of contents, or indexes.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> nav_elem = NavigationElement()
    >>> print(nav_elem.to_string())
    <nav></nav>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new NavigationElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("nav", **kwargs)


class NoScriptElement(BaseHTMLElement):
    """
    NoScriptElement Class extends BaseHTMLElement to represent the HTML <noscript> element.

    HTML Use Cases:
    ---------------
    The HTML <noscript> element is used to provide an alternative content for users who have
    disabled JavaScript in their browser or have a browser that doesn't support JavaScript.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> noscript_elem = NoScriptElement()
    >>> print(noscript_elem.to_string())
    <noscript></noscript>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new NoScriptElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("noscript", **kwargs)
