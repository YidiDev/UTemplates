from ..base import BaseHTMLElement


class FieldsetElement(BaseHTMLElement):
    """
    FieldsetElement Class extends BaseHTMLElement to represent HTML fieldset elements (`<fieldset>`).

    HTML Use Cases:
    ---------------
    The `<fieldset>` element is used to group together related elements in a form, typically via containing them within a `<legend>`.

    Methods:
    --------
    to_string():
        Converts the fieldset element to an HTML string.

    Example Usage:
    --------------
    >>> fieldset_elem = FieldsetElement(name="personal_info")
    >>> print(fieldset_elem.to_string())
    <fieldset name="personal_info"></fieldset>

    """

    def __init__(self, disabled: bool = False, form: str = None, name: str = None, **kwargs) -> None:
        """
        Initializes a new FieldsetElement instance.

        Parameters:
        -----------
        disabled : bool, optional
            Specifies whether the fieldset should be disabled.
        form : str, optional
            Specifies the form element that the fieldset belongs to.
        name : str, optional
            Specifies the name of the fieldset.
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content', 'attributes', or 'self_closing'.

        """
        attributes: dict[str, str | bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["disabled"] = disabled
        attributes["form"] = form
        attributes["name"] = name
        super().__init__("fieldset", attributes=attributes, **kwargs)


class FigureCaptionElement(BaseHTMLElement):
    """
    FigureCaptionElement Class extends BaseHTMLElement to represent HTML figure caption elements (`<figcaption>`).

    HTML Use Cases:
    ---------------
    The `<figcaption>` element is used to provide a caption to an HTML `<figure>` element. It is usually
    placed as the first or the last child of the `<figure>`.

    Methods:
    --------
    to_string():
        Converts the figure caption element to an HTML string.

    Example Usage:
    --------------
    >>> figcaption_elem = FigureCaptionElement(content="This is a caption.")
    >>> print(figcaption_elem.to_string())
    <figcaption>This is a caption.</figcaption>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new FigureCaptionElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content', 'attributes', or 'self_closing'.
        """
        super().__init__("figcaption", **kwargs)


class FigureElement(BaseHTMLElement):
    """
    FigureElement Class extends BaseHTMLElement to represent HTML figure elements (`<figure>`).

    HTML Use Cases:
    ---------------
    The `<figure>` element is used to encapsulate media such as an image, diagram, or code snippet,
    along with its caption, provided by the `<figcaption>` element. It serves as a container for these
    media and allows them to be semantically grouped together.

    Methods:
    --------
    to_string():
        Converts the figure element to an HTML string.

    Example Usage:
    --------------
    >>> figure_elem = FigureElement(content=[image_elem, figcaption_elem])
    >>> print(figure_elem.to_string())
    <figure><img src="example.jpg" alt="An example image"><figcaption>This is a caption.</figcaption></figure>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new FigureElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content', 'attributes', or 'self_closing'.
        """
        super().__init__("figure", **kwargs)


class FooterElement(BaseHTMLElement):
    """
    FooterElement Class extends BaseHTMLElement to represent HTML footer elements (`<footer>`).

    HTML Use Cases:
    ---------------
    The `<footer>` element represents a container for the bottom section of a document or a section,
    typically containing information about the document such as author, copyright information, or links to related documents.

    Methods:
    --------
    to_string():
        Converts the footer element to an HTML string.

    Example Usage:
    --------------
    >>> footer_elem = FooterElement(content=["Copyright 2023"])
    >>> print(footer_elem.to_string())
    <footer>Copyright 2023</footer>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new FooterElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content', 'attributes', or 'self_closing'.
        """
        super().__init__("footer", **kwargs)


class FormElement(BaseHTMLElement):
    """
    FormElement Class extends BaseHTMLElement to represent HTML form elements (`<form>`).

    HTML Use Cases:
    ---------------
    The `<form>` element represents a section of a document containing interactive controls
    for submitting information to a web server. It can contain input elements like text fields,
    checkboxes, radio-buttons, submit buttons, etc.

    Methods:
    --------
    to_string():
        Converts the form element to an HTML string.

    Example Usage:
    --------------
    >>> form_elem = FormElement(action="/submit", method="post", content=["Submit your data"])
    >>> print(form_elem.to_string())
    <form action="/submit" method="post">Submit your data</form>

    """

    def __init__(
            self,
            accept_charset: str = None,
            action: str = None,
            autocomplete: str = None,
            enctype: str = None,
            method: str = None,
            name: str = None,
            novalidate: bool = False,
            rel: str = None,
            target: str = None,
            **kwargs
    ) -> None:
        """
        Initializes a new FormElement instance.

        Parameters:
        -----------
        accept_charset : str, optional
            Specifies the character encodings that are to be used for the form submission.
        action : str, optional
            Specifies where to send the form-data when a form is submitted.
        autocomplete : str, optional
            Specifies whether the <form> element should have autocomplete enabled.
        enctype : str, optional
            Specifies how the form-data should be encoded when submitting it to the server.
        method : str, optional
            Specifies the HTTP method to use when sending form-data.
        name : str, optional
            Specifies the name of the form.
        novalidate : bool, optional
            Specifies that the form should not be validated when submitted.
        rel : str, optional
            Specifies the relationship between the linked resource and the current document.
        target : str, optional
            Specifies where to display the response that is received after submitting the form.

        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content', 'attributes', or 'self_closing'.
        """
        attributes: dict[str, str | bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["accept-charset"] = accept_charset
        attributes["action"] = action
        attributes["autocomplete"] = autocomplete
        attributes["enctype"] = enctype
        attributes["method"] = method
        attributes["name"] = name
        attributes["novalidate"] = novalidate
        attributes["rel"] = rel
        attributes["target"] = target
        super().__init__("form", attributes=attributes, **kwargs)
