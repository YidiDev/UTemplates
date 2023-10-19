from ..base import BaseHTMLElement


class LabelElement(BaseHTMLElement):
    """
    LabelElement Class extends BaseHTMLElement to represent the HTML <label> element.

    HTML Use Cases:
    ---------------
    The HTML <label> element is used to associate a text label with a form control element.
    The association is done using the `for` attribute which matches the `id` of the form control.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> label_elem = LabelElement(for_attribute="username", content="Username:")
    >>> print(label_elem.to_string())
    <label for="username">Username:</label>
    """

    def __init__(self, for_attribute: str = None, form: str = None, **kwargs) -> None:
        """
        Initializes a new LabelElement instance.

        Parameters:
        -----------
        for_attribute : str, optional
            Specifies the id of the form control with which the label is associated.
        form : str, optional
            Specifies the id of the form element the label is associated with.
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        Attributes:
        -----------
        for : str
            Represents the 'for' HTML attribute to associate the label with a form control.
        form : str
            Represents the 'form' HTML attribute to associate the label with a form.
        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['for'] = for_attribute
        super().__init__("label", form=form, attributes=attributes, **kwargs)


class LegendElement(BaseHTMLElement):
    """
    LegendElement Class extends BaseHTMLElement to represent the HTML <legend> element.

    HTML Use Cases:
    ---------------
    The HTML <legend> element is used to provide a title or caption within a <fieldset> element.
    It helps in grouping related controls in a form.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> legend_elem = LegendElement(content="Personal Information")
    >>> print(legend_elem.to_string())
    <legend>Personal Information</legend>
    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new LegendElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.
        """
        super().__init__("legend", **kwargs)


class ListItemElement(BaseHTMLElement):
    """
    ListItemElement Class extends BaseHTMLElement to represent the HTML <li> element.

    HTML Use Cases:
    ---------------
    The HTML <li> element is used to represent list items within ordered (<ol>) or unordered (<ul>) lists.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> li_elem = ListItemElement(content="Apple")
    >>> print(li_elem.to_string())
    <li>Apple</li>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new ListItemElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.
        """
        super().__init__("li", **kwargs)


class LinkElement(BaseHTMLElement):
    """
    LinkElement Class extends BaseHTMLElement to represent the HTML <link> element.

    HTML Use Cases:
    ---------------
    The HTML <link> element is used to define relationships between the current document and other resources.
    It is commonly used to link stylesheets, favicons, and other external resources.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> link_elem = LinkElement(rel="stylesheet", href="/styles.css")
    >>> print(link_elem.to_string())
    <link rel="stylesheet" href="/styles.css">

    """

    def __init__(
            self,
            crossorigin: bool = False,
            href: str = None,
            hreflang: str = None,
            media: str = None,
            referrerpolicy: str = None,
            rel: str = None,
            sizes: str = None,
            title: str = None,
            type: str = None,
            **kwargs
    ) -> None:
        """
        Initializes a new LinkElement instance.

        Parameters:
        -----------
        crossorigin : bool, optional
            Specifies if the element handles crossorigin requests.
        href : str, optional
            Specifies the URL of the linked resource.
        hreflang : str, optional
            Language of the linked resource.
        media : str, optional
            Specifies what media/device the linked resource is optimized for.
        referrerpolicy : str, optional
            Referrer policy for the linked resource.
        rel : str, optional
            Relationship between the current document and the linked resource.
        sizes : str, optional
            Specifies the sizes of icons for visual media.
        title : str, optional
            Specifies extra information about the linked resource.
        type : str, optional
            Specifies the media type of the linked resource.
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__(
            "link",
            crossorigin=crossorigin,
            href=href,
            hreflang=hreflang,
            media=media,
            referrerpolicy=referrerpolicy,
            rel=rel,
            sizes=sizes,
            title=title,
            type=type,
            **kwargs
        )
