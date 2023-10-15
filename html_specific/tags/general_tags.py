from html_specific.base import BaseHTMLElement


class GeneralHTMLElement(BaseHTMLElement):
    def __init__(
            self,
            tag_name: str,
            attributes: dict[str, any] = None,
            content: str | BaseHTMLElement | list[str | BaseHTMLElement] = None,
            self_closing: bool = False
    ) -> None:
        super().__init__(
            tag_name=tag_name, attributes=attributes, content=content, self_closing=self_closing
        )


class CommentElement(BaseHTMLElement):
    """
    CommentElement Class extends BaseHTMLElement to represent HTML comments.
    The class takes a string as a comment and wraps it in an HTML comment tag `<!-- -->`.

    HTML Use Cases:
    ---------------
    HTML comments are useful to annotate your HTML source code, providing information
    about the code structure or explaining parts of the code for future reference.
    These comments are not displayed to the user on the web page.

    Attributes:
    -----------
    comment: str
        The text content of the HTML comment.

    Methods:
    --------
    to_string():
        Converts the comment to an HTML comment string.

    Example Usage:
    --------------
    >>> comment_elem = CommentElement("This is a sample comment")
    >>> print(comment_elem.to_string())
    <!--This is a sample comment-->

    """

    def __init__(self, comment: str, **kwargs) -> None:
        """
        Initializes a new CommentElement instance.

        Parameters:
        -----------
        comment: str
            The text content for the HTML comment.
        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class.

        """
        super().__init__(f"!--{comment}--", self_closing=True, **kwargs)


class DoctypeElement(BaseHTMLElement):
    """
    DoctypeElement Class extends BaseHTMLElement to represent the DOCTYPE declaration.
    This class creates an HTML DOCTYPE element specifying the document type and version of HTML.

    HTML Use Cases:
    ---------------
    The DOCTYPE declaration is used to define the document type and version of HTML being used.
    It should be the very first thing in an HTML document, before the <html> element.

    Attributes:
    -----------
    declaration: str
        The HTML version or standard used, such as 'html' for <!DOCTYPE html>.
        Default is 'html'.

    Methods:
    --------
    to_string():
        Converts the DOCTYPE to a DOCTYPE string.

    Example Usage:
    --------------
    >>> doctype_elem = DoctypeElement("html")
    >>> print(doctype_elem.to_string())
    <!DOCTYPE html>

    >>> doctype_elem = DoctypeElement("HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\"")
    >>> print(doctype_elem.to_string())
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

    """

    def __init__(self, declaration: str = "html", **kwargs) -> None:
        """
        Initializes a new DoctypeElement instance.

        Parameters:
        -----------
        declaration: str
            The HTML version or standard being used. Default is 'html'.
        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class.

        """
        super().__init__("!DOCTYPE", attributes={declaration: True}, self_closing=True, **kwargs)
