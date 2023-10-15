from ..base import BaseHTMLElement


class QuotationElement(BaseHTMLElement):
    """
    QuotationElement Class extends BaseHTMLElement to represent the HTML <q> element.

    HTML Use Cases:
    ---------------
    The HTML <q> element is used for short inline quotations. It typically encloses a brief quotation that is
    part of the surrounding text.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> quote_elem = QuotationElement(cite="https://example.com/quote-source")
    >>> quote_elem.content.append("This is a short quotation.")
    >>> print(quote_elem.to_string())
    <q cite="https://example.com/quote-source">This is a short quotation.</q>

    """

    def __init__(self, cite: str = None, **kwargs) -> None:
        """
        Initializes a new QuotationElement instance.

        Parameters:
        -----------
        cite : str
            The URL that specifies the source of the quotation (optional).

        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes: dict[str, str] = {
            'cite': cite
        }
        super().__init__("q", attributes=attributes, **kwargs)
