from ..base import BaseHTMLElement


class EmphasizedElement(BaseHTMLElement):
    """
    EmphasizedElement Class extends BaseHTMLElement to represent HTML emphasized text elements (`<em>`).

    HTML Use Cases:
    ---------------
    The `<em>` element is used to emphasize text. The content within an `<em>` element is typically displayed in italics by web browsers.

    Methods:
    --------
    to_string():
        Converts the emphasized element to an HTML string.

    Example Usage:
    --------------
    >>> em_elem = EmphasizedElement(content="This is important.")
    >>> print(em_elem.to_string())
    <em>This is important.</em>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new EmphasizedElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content', 'attributes', or 'self_closing'.

        """
        super().__init__("em", **kwargs)


class EmbedElement(BaseHTMLElement):
    """
    EmbedElement Class extends BaseHTMLElement to represent HTML embedded content elements (`<embed>`).

    HTML Use Cases:
    ---------------
    The `<embed>` element is used to embed external content like multimedia files (video, audio) or interactive content (Flash, etc.) into an HTML document.

    Methods:
    --------
    to_string():
        Converts the embed element to an HTML string.

    Example Usage:
    --------------
    >>> embed_elem = EmbedElement(src="video.mp4", type="video/mp4", width="640", height="480")
    >>> print(embed_elem.to_string())
    <embed src="video.mp4" type="video/mp4" width="640" height="480">

    """

    def __init__(
            self, height: str = None, src: str = None, type: str = None, width: str = None, **kwargs
    ) -> None:
        """
        Initializes a new EmbedElement instance.

        Parameters:
        -----------
        height : str, optional
            Specifies the height of the embedded content.
        src : str, optional
            Specifies the URL of the embedded content.
        type : str, optional
            Specifies the MIME type of the embedded content.
        width : str, optional
            Specifies the width of the embedded content.
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content', 'attributes', or 'self_closing'.

        """
        super().__init__("embed", height=height, src=src, type=type, width=width, **kwargs)
