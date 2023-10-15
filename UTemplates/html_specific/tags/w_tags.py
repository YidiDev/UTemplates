from ..base import BaseHTMLElement


class WordBreakOpportunityElement(BaseHTMLElement):
    """
    WordBreakOpportunityElement Class extends BaseHTMLElement to represent the HTML <wbr> element.

    HTML Use Cases:
    ---------------
    The HTML <wbr> element represents a word break opportunity, indicating where a word can be broken and wrapped to
    the next line when necessary.

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
    # Create a WordBreakOpportunityElement
    >>> wbr = WordBreakOpportunityElement()

    # Convert it to an HTML string
    >>> print(wbr.to_string())
    <wbr>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new WordBreakOpportunityElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("wbr", self_closing=True, **kwargs)
