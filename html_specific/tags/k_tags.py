from html_specific.base import BaseHTMLElement


class KeyboardInputElement(BaseHTMLElement):
    """
    KeyboardInputElement Class extends BaseHTMLElement to represent the HTML <kbd> element.

    HTML Use Cases:
    ---------------
    The HTML <kbd> element represents user input, typically keyboard input, or other input that can be done via text.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> kbd_elem = KeyboardInputElement(content="Ctrl + C")
    >>> print(kbd_elem.to_string())
    <kbd>Ctrl + C</kbd>
    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new KeyboardInputElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.
        """
        super().__init__("kbd", **kwargs)
