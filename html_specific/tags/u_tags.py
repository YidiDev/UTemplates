from html_specific.base import BaseHTMLElement


class UnarticulatedElement(BaseHTMLElement):
    """
    UnarticulatedElement Class extends BaseHTMLElement to represent the HTML <u> element.

    HTML Use Cases:
    ---------------
    The HTML <u> element is used to define text that should be stylistically rendered as underlined text.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Parameters:
    -----------
    **kwargs : dict
        Additional keyword arguments that are passed to the parent class.

    Example Usage:
    --------------
    # Create an UnarticulatedElement for underlined text
    >>> underlined_text = UnarticulatedElement(content="This is underlined text.")

    # Convert it to an HTML string
    >>> print(underlined_text.to_string())
    <u>This is underlined text.</u>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new UnarticulatedElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("u", **kwargs)


class UnorderedListElement(BaseHTMLElement):
    """
    UnorderedListElement Class extends BaseHTMLElement to represent the HTML <ul> element.

    HTML Use Cases:
    ---------------
    The HTML <ul> element is used to create an unordered list of items. Each item is represented
    using the <li> element, which can be added as content to this <ul> element.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Parameters:
    -----------
    **kwargs : dict
        Additional keyword arguments that are passed to the parent class.

    Example Usage:
    --------------
    # Create an UnorderedListElement
    >>> ul = UnorderedListElement()

    # Add list items using ListItemElement
    >>> li1 = ListItemElement(content="Item 1")
    >>> li2 = ListItemElement(content="Item 2")

    # Append the list items to the <ul> element
    >>> ul.append(li1)
    >>> ul.append(li2)

    # Convert it to an HTML string
    >>> print(ul.to_string())
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
    </ul>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new UnorderedListElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("ul", **kwargs)
