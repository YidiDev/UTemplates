from ..base import BaseHTMLElement


class ParagraphElement(BaseHTMLElement):
    """
    ParagraphElement Class extends BaseHTMLElement to represent the HTML <p> element.

    HTML Use Cases:
    ---------------
    The HTML <p> element represents a paragraph of text.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> paragraph_elem = ParagraphElement()
    >>> paragraph_elem.content.append("This is a paragraph of text.")
    >>> print(paragraph_elem.to_string())
    <p>This is a paragraph of text.</p>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new ParagraphElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("p", **kwargs)


class ParameterElement(BaseHTMLElement):
    """
    ParameterElement Class extends BaseHTMLElement to represent the HTML <param> element.

    HTML Use Cases:
    ---------------
    The HTML <param> element defines parameters for plugins invoked by object elements.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> param_elem = ParameterElement(name="autoplay", value="true")
    >>> print(param_elem.to_string())
    <param name="autoplay" value="true" />

    """

    def __init__(self, name: str = None, value: str = None, **kwargs) -> None:
        """
        Initializes a new ParameterElement instance.

        Parameters:
        -----------
        name : str, optional
            The name of the parameter.
        value : str, optional
            The value associated with the parameter.
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes = {}
        if name is not None:
            attributes['name'] = name
        if value is not None:
            attributes['value'] = value

        super().__init__("param", attributes=attributes, self_closing=True, **kwargs)


class PictureElement(BaseHTMLElement):
    """
    PictureElement Class extends BaseHTMLElement to represent the HTML <picture> element.

    HTML Use Cases:
    ---------------
    The HTML <picture> element contains zero or more <source> elements and one <img> element to provide versions of an
    image for different display/device scenarios.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> picture_elem = PictureElement()
    >>> source_elem = SourceElement(srcset="image.webp", type_attribute="image/webp")
    >>> img_elem = ImageElement(src="image.jpg", alt="An image")
    >>> picture_elem.add_content(source_elem, img_elem)
    >>> print(picture_elem.to_string())
    <picture>
        <source srcset="image.webp" type="image/webp" />
        <img src="image.jpg" alt="An image" />
    </picture>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new PictureElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("picture", **kwargs)


class PreformattedElement(BaseHTMLElement):
    """
    PreformattedElement Class extends BaseHTMLElement to represent the HTML <pre> element.

    HTML Use Cases:
    ---------------
    The HTML <pre> element defines preformatted text. Text within this element is shown in a fixed-width font (usually
    Courier), and whitespace characters (like spaces and tabs) are displayed as written.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> pre_elem = PreformattedElement()
    >>> pre_elem.add_content("This is a preformatted text block.")
    >>> pre_elem.add_content("    Indentation is preserved.")
    >>> print(pre_elem.to_string())
    <pre>
    This is a preformatted text block.
        Indentation is preserved.
    </pre>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new PreformattedElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("pre", **kwargs)


class ProgressElement(BaseHTMLElement):
    """
    ProgressElement Class extends BaseHTMLElement to represent the HTML <progress> element.

    HTML Use Cases:
    ---------------
    The HTML <progress> element represents the completion progress of a task. It is typically displayed as a
    progress bar.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> progress_elem = ProgressElement(max="100", value="60")
    >>> print(progress_elem.to_string())
    <progress max="100" value="60"></progress>

    """

    def __init__(self, max: str = "1", value: str = None, **kwargs) -> None:
        """
        Initializes a new ProgressElement instance.

        Parameters:
        -----------
        max : str
            The maximum value of the progress element (default is "1").
        value : str
            The current value of the progress element (optional).

        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes: dict[str, str] = {
            'max': max,
            'value': value
        }
        super().__init__("progress", attributes=attributes, **kwargs)
