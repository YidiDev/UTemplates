from ..base import BaseHTMLElement


class HeadingElement(BaseHTMLElement):
    """
    HeadingElement Class extends BaseHTMLElement to represent HTML heading elements (`<h1>`, `<h2>`, ..., `<h6>`).

    HTML Use Cases:
    ---------------
    The HTML heading elements represent six levels of headings, `<h1>` being the highest level and `<h6>` the lowest.
    They are block-level elements that introduce new sections and subsections in a page's content.

    Methods:
    --------
    to_string():
        Converts the heading element to an HTML string.

    Example Usage:
    --------------
    >>> heading_elem = HeadingElement(1, content="Main Title")
    >>> print(heading_elem.to_string())
    <h1>Main Title</h1>

    """

    def __init__(self, level: int, **kwargs) -> None:
        """
        Initializes a new HeadingElement instance.

        Parameters:
        -----------
        level : int
            Specifies the heading level. Valid values are integers from 1 to 6, where 1 corresponds to <h1> and 6 to <h6>.

        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content', 'attributes', or 'self_closing'.

        Raises:
        -------
        Prints a warning message if the provided level is outside of the range 1-6.
        """
        if level > 6 or level < 1:
            print("WARNING: valid heading elements should be between 1 and 6")
        super().__init__(f"h{level}", **kwargs)


class HeadElement(BaseHTMLElement):
    """
    HeadElement Class extends BaseHTMLElement to represent the HTML `<head>` element.

    HTML Use Cases:
    ---------------
    The HTML `<head>` element contains meta-information about the document and links to external resources.
    It can include elements like `<title>`, `<link>`, `<meta>`, `<script>`, etc., but it should not contain any content
    that is rendered on the web page itself.

    Methods:
    --------
    to_string():
        Converts the head element to an HTML string.

    Example Usage:
    --------------
    >>> head_elem = HeadElement(content=[TitleElement(content="My Web Page"), MetaElement(charset="UTF-8")])
    >>> print(head_elem.to_string())
    <head><title>My Web Page</title><meta charset="UTF-8"></head>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new HeadElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class,
            such as 'content', 'attributes', or 'self_closing'.
        """
        super().__init__("head", **kwargs)


class HeaderElement(BaseHTMLElement):
    """
    HeaderElement Class extends BaseHTMLElement to represent the HTML `<header>` element.

    HTML Use Cases:
    ---------------
    The HTML `<header>` element is used to contain introductory and navigational information
    for its nearest ancestor block-level section. It often contains elements like site logos,
    titles, and navigation menus.

    Methods:
    --------
    to_string():
        Converts the header element to an HTML string.

    Example Usage:
    --------------
    >>> header_elem = HeaderElement(content=[ParagraphElement(content="Welcome to My Website"), NavElement()])
    >>> print(header_elem.to_string())
    <header><p>Welcome to My Website</p><nav></nav></header>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new HeaderElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class,
            such as 'content', 'attributes', or 'self_closing'.
        """
        super().__init__("header", **kwargs)


class HorizontalRuleElement(BaseHTMLElement):
    """
    HorizontalRuleElement Class extends BaseHTMLElement to represent the HTML `<hr>` element.

    HTML Use Cases:
    ---------------
    The HTML `<hr>` element is used to represent a thematic break in the content. It's often used
    to separate content or create visual breaks in a page.

    Methods:
    --------
    to_string():
        Converts the horizontal rule element to an HTML string.

    Example Usage:
    --------------
    >>> hr_elem = HorizontalRuleElement()
    >>> print(hr_elem.to_string())
    <hr />

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new HorizontalRuleElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class,
            such as 'attributes'.
        """
        super().__init__("hr", self_closing=True, **kwargs)


class HTMLElement(BaseHTMLElement):
    """
    HTMLElement Class extends BaseHTMLElement to represent the HTML `<html>` element.

    HTML Use Cases:
    ---------------
    The HTML `<html>` element is the root element that encloses all the other HTML elements on the page.
    It serves as the container for the entire HTML document.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> html_elem = HTMLElement()
    >>> print(html_elem.to_string())
    <html></html>

    >>> html_elem_with_xmlns = HTMLElement(xmlns="http://www.w3.org/1999/xhtml")
    >>> print(html_elem_with_xmlns.to_string())
    <html xmlns="http://www.w3.org/1999/xhtml"></html>

    """

    def __init__(self, xmlns: str = None, **kwargs) -> None:
        """
        Initializes a new HTMLElement instance.

        Parameters:
        -----------
        xmlns : str, optional
            Defines the XML namespace. Commonly used when serving XHTML.

        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class,
            such as 'attributes'.
        """
        super().__init__("html", xmlns=xmlns, **kwargs)
