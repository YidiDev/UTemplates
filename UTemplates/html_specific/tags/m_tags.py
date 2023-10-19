from ..base import BaseHTMLElement


class MainElement(BaseHTMLElement):
    """
    MainElement Class extends BaseHTMLElement to represent the HTML <main> element.

    HTML Use Cases:
    ---------------
    The HTML <main> element represents the main content of the body of a document or application.
    The main content area consists of content that is directly related to or expands upon the central topic
    of a document or the central functionality of an application.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> main_elem = MainElement(content="This is the main content.")
    >>> print(main_elem.to_string())
    <main>This is the main content.</main>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new MainElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("main", **kwargs)


class MapElement(BaseHTMLElement):
    """
    MapElement Class extends BaseHTMLElement to represent the HTML <map> element.

    HTML Use Cases:
    ---------------
    The HTML <map> element is used with <area> elements to define an image map.
    An image map allows geometric areas on an image to be associated with hyperlinks.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> area1 = BaseHTMLElement(tag_name='area', attributes={'shape': 'rect', 'coords': '34,44,270,350', 'href': '#'})
    >>> area2 = BaseHTMLElement(tag_name='area', attributes={'shape': 'circle', 'coords': '128,128,100', 'href': '#'})
    >>> map_elem = MapElement(name="myMap", content=[area1, area2])
    >>> print(map_elem.to_string())
    <map name="myMap"><area shape="rect" coords="34,44,270,350" href="#"><area shape="circle" coords="128,128,100" href="#"></map>

    """

    def __init__(self, name: str, **kwargs) -> None:
        """
        Initializes a new MapElement instance.

        Parameters:
        -----------
        name : str
            The name attribute for the <map> element.
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("map", name=name, **kwargs)


class MarkedElement(BaseHTMLElement):
    """
    MarkedElement Class extends BaseHTMLElement to represent the HTML <mark> element.

    HTML Use Cases:
    ---------------
    The HTML <mark> element is used to highlight parts of the text that are of
    particular relevance or require special attention. It's commonly used for search results
    or other crucial information within a block of text.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> mark_elem = MarkedElement(content="Important")
    >>> print(mark_elem.to_string())
    <mark>Important</mark>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new MarkedElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("mark", **kwargs)


class MetaElement(BaseHTMLElement):
    """
    MetaElement Class extends BaseHTMLElement to represent the HTML <meta> element.

    HTML Use Cases:
    ---------------
    The HTML <meta> element provides metadata about the HTML document.
    Metadata is information about the data within the document, and it doesn't appear on the web page itself.
    The <meta> element can be used to specify character encoding, authorship, viewport settings, and more.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> meta_elem = MetaElement(charset="UTF-8", name="viewport", content="width=device-width, initial-scale=1.0")
    >>> print(meta_elem.to_string())
    <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0">

    """

    def __init__(
            self, charset: str = None, content: str = None, http_equiv: str = None, name: str = None, **kwargs
    ) -> None:
        """
        Initializes a new MetaElement instance.

        Parameters:
        -----------
        charset : str, optional
            The character encoding of the document.
        content : str, optional
            The value of the metadata.
        http_equiv : str, optional
            Used when the metadata has an HTTP header equivalent.
        name : str, optional
            A name for the metadata.

        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("meta", charset=charset, content=content, http_equiv=http_equiv, name=name, **kwargs)


class MeterElement(BaseHTMLElement):
    """
    MeterElement Class extends BaseHTMLElement to represent the HTML <meter> element.

    HTML Use Cases:
    ---------------
    The HTML <meter> element represents a scalar measurement within a known range or a fractional value.
    It's commonly used to display a visual representation of values like disk usage, completion progress, or ratings.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> meter_elem = MeterElement(value="75", min="0", max="100", low="25", high="90", optimum="80")
    >>> print(meter_elem.to_string())
    <meter value="75" min="0" max="100" low="25" high="90" optimum="80">

    """

    def __init__(
            self,
            form: str = None,
            high: str = None,
            low: str = None,
            max: str = None,
            min: str = None,
            optimum: str = None,
            value: str = None,
            **kwargs
    ) -> None:
        """
        Initializes a new MeterElement instance.

        Parameters:
        -----------
        form : str, optional
            The ID of the form element that the meter element is associated with.
        high : str, optional
            The high value of the range.
        low : str, optional
            The low value of the range.
        max : str, optional
            The maximum value of the range.
        min : str, optional
            The minimum value of the range.
        optimum : str, optional
            The optimal value of the range.
        value : str, optional
            The current value of the meter.

        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__(
            "meter", form=form, high=high, low=low, max=max, min=min, optimum=optimum, value=value, **kwargs
        )
