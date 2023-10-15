from ..base import BaseHTMLElement


class DataElement(BaseHTMLElement):
    """
    DataElement Class extends BaseHTMLElement to represent HTML data elements (`<data>`).
    The `<data>` element is used to represent a machine-readable translation of content.

    HTML Use Cases:
    ---------------
    The `<data>` element is used to associate a text string with a machine-readable value via its `value` attribute.
    This can be useful for semantic markup, as it allows for the inclusion of structured data.

    Methods:
    --------
    to_string():
        Converts the data element to an HTML string.

    Example Usage:
    --------------
    >>> data_elem = DataElement(value="42")
    >>> print(data_elem.to_string())
    <data value="42"></data>

    """

    def __init__(self, value: str = None, **kwargs) -> None:
        """
        Initializes a new DataElement instance.

        Parameters:
        -----------
        value : str, optional
            Specifies the machine-readable value for the <data> element.

        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content'.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["value"] = value
        super().__init__("data", attributes=attributes, **kwargs)


class DataListElement(BaseHTMLElement):
    """
    DataListElement Class extends BaseHTMLElement to represent HTML datalist elements (`<datalist>`).

    HTML Use Cases:
    ---------------
    The `<datalist>` element provides a list of pre-defined options for an `<input>` element.
    It is useful for creating auto-complete functionality in forms.

    Methods:
    --------
    to_string():
        Converts the datalist element to an HTML string.

    Example Usage:
    --------------
    >>> datalist_elem = DataListElement()
    >>> print(datalist_elem.to_string())
    <datalist></datalist>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new DataListElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content' or 'attributes'.

        """
        super().__init__("datalist", **kwargs)


class DefinitionDescriptionElement(BaseHTMLElement):
    """
    DefinitionDescriptionElement Class extends BaseHTMLElement to represent HTML definition description elements (`<dd>`).

    HTML Use Cases:
    ---------------
    The `<dd>` element is used to describe a term/name in a description list (`<dl>`).
    It is usually used in conjunction with `<dt>` (Definition Term) to specify a pair of term-description.

    Methods:
    --------
    to_string():
        Converts the definition description element to an HTML string.

    Example Usage:
    --------------
    >>> dd_elem = DefinitionDescriptionElement(content="This is a description.")
    >>> print(dd_elem.to_string())
    <dd>This is a description.</dd>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new DefinitionDescriptionElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content' or 'attributes'.

        """
        super().__init__("dd", **kwargs)


class DeletedElement(BaseHTMLElement):
    """
    DeletedElement Class extends BaseHTMLElement to represent HTML deleted text elements (`<del>`).

    HTML Use Cases:
    ---------------
    The `<del>` element is used to represent a range of text that has been deleted from a document.
    It often has `cite` and `datetime` attributes to specify the source and time of the deletion.

    Methods:
    --------
    to_string():
        Converts the deleted element to an HTML string.

    Example Usage:
    --------------
    >>> del_elem = DeletedElement(cite="https://example.com", datetime="2023-01-01T12:34:56", content="deleted content")
    >>> print(del_elem.to_string())
    <del cite="https://example.com" datetime="2023-01-01T12:34:56">deleted content</del>

    """

    def __init__(self, cite: str = None, datetime: str = None, **kwargs) -> None:
        """
        Initializes a new DeletedElement instance.

        Parameters:
        -----------
        cite : str, optional
            Specifies the source URL where the deletion was made.
        datetime : str, optional
            Specifies the date and time when the deletion was made, usually in ISO 8601 format.
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content' or 'attributes'.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        if cite is not None:
            attributes["cite"] = cite
        if datetime is not None:
            attributes["datetime"] = datetime
        super().__init__("del", attributes=attributes, **kwargs)


class DetailsElement(BaseHTMLElement):
    """
    DetailsElement Class extends BaseHTMLElement to represent HTML details elements (`<details>`).

    HTML Use Cases:
    ---------------
    The `<details>` element is used to create an interactive widget that the user can open or close to reveal or hide content.
    The `open` attribute specifies whether the content inside the `<details>` element should be visible or not.

    Methods:
    --------
    to_string():
        Converts the details element to an HTML string.

    Example Usage:
    --------------
    >>> details_elem = DetailsElement(open=True, content="This is some hidden content.")
    >>> print(details_elem.to_string())
    <details open>This is some hidden content.</details>

    """

    def __init__(self, open: bool = False, **kwargs) -> None:
        """
        Initializes a new DetailsElement instance.

        Parameters:
        -----------
        open : bool, optional
            Specifies whether the `<details>` element should be open by default. Default is False.
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content' or 'attributes'.

        """
        attributes: dict[str, bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        if open is not None:
            attributes["open"] = open
        super().__init__("details", attributes=attributes, **kwargs)


class DefinitionElement(BaseHTMLElement):
    """
    DefinitionElement Class extends BaseHTMLElement to represent HTML definition elements (`<dfn>`).

    HTML Use Cases:
    ---------------
    The `<dfn>` element is used to indicate the term being defined within the context of a definition phrase or sentence.

    Methods:
    --------
    to_string():
        Converts the definition element to an HTML string.

    Example Usage:
    --------------
    >>> definition_elem = DefinitionElement(content="HTML")
    >>> print(definition_elem.to_string())
    <dfn>HTML</dfn>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new DefinitionElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content' or 'attributes'.

        """
        super().__init__("dfn", **kwargs)


class DialogElement(BaseHTMLElement):
    """
    DialogElement Class extends BaseHTMLElement to represent HTML dialog elements (`<dialog>`).

    HTML Use Cases:
    ---------------
    The `<dialog>` element is used to create a dialog box or subwindow that can be toggled open or closed.
    It may be used to create modal or non-modal dialog boxes for user interactions, pop-ups, and more.

    Methods:
    --------
    to_string():
        Converts the dialog element to an HTML string.

    Example Usage:
    --------------
    >>> dialog_elem = DialogElement(open=True, content="Hello, world!")
    >>> print(dialog_elem.to_string())
    <dialog open>Hello, world!</dialog>

    """

    def __init__(self, open: bool = False, **kwargs) -> None:
        """
        Initializes a new DialogElement instance.

        Parameters:
        -----------
        open : bool, optional
            Indicates whether the dialog box should be open or not when rendered. Default is False.

        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content' or 'attributes'.

        """
        attributes: dict[str, bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        if open is not None:
            attributes["open"] = open
        super().__init__("dialog", attributes=attributes, **kwargs)


class DivElement(BaseHTMLElement):
    """
    DivElement Class extends BaseHTMLElement to represent HTML div elements (`<div>`).

    HTML Use Cases:
    ---------------
    The `<div>` element is a generic container for flow content, which does not inherently represent anything.
    It can be used to group elements for styling purposes or because they share attribute values.

    Methods:
    --------
    to_string():
        Converts the div element to an HTML string.

    Example Usage:
    --------------
    >>> div_elem = DivElement(content="Hello, world!")
    >>> print(div_elem.to_string())
    <div>Hello, world!</div>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new DivElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content', 'attributes', or 'self_closing'.

        """
        super().__init__("div", **kwargs)


class DescriptionListElement(BaseHTMLElement):
    """
    DescriptionListElement Class extends BaseHTMLElement to represent HTML description list elements (`<dl>`).

    HTML Use Cases:
    ---------------
    The `<dl>` element represents a description list, usually consisting of a series of term-description pairs (`<dt>` and `<dd>` elements).

    Methods:
    --------
    to_string():
        Converts the description list element to an HTML string.

    Example Usage:
    --------------
    >>> dl_elem = DescriptionListElement(content=[DTElement(content="Term"), DDElement(content="Description")])
    >>> print(dl_elem.to_string())
    <dl><dt>Term</dt><dd>Description</dd></dl>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new DescriptionListElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content', 'attributes', or 'self_closing'.

        """
        super().__init__("dl", **kwargs)


class DescriptionTermElement(BaseHTMLElement):
    """
    DescriptionTermElement Class extends BaseHTMLElement to represent HTML description term elements (`<dt>`).

    HTML Use Cases:
    ---------------
    The `<dt>` element specifies a term in a description list (`<dl>`), and is usually followed by at least one `<dd>` element that describes the term.

    Methods:
    --------
    to_string():
        Converts the description term element to an HTML string.

    Example Usage:
    --------------
    >>> dt_elem = DescriptionTermElement(content="Apple")
    >>> print(dt_elem.to_string())
    <dt>Apple</dt>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new DescriptionTermElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content', 'attributes', or 'self_closing'.

        """
        super().__init__("dt", **kwargs)
