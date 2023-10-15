from html_specific.base import BaseHTMLElement


class BoldElement(BaseHTMLElement):
    """
    BoldElement Class extends BaseHTMLElement to represent HTML bold elements (`<b>`).
    This class creates a bold element that renders text in boldface.

    HTML Use Cases:
    ---------------
    The `<b>` HTML element is used to draw attention to enclosed text without implying any added
    importance or emphasis. It is generally used for stylistic changes without changing the importance
    of the text itself.

    Note: If the text is of more importance, consider using the `<strong>` element instead.

    Methods:
    --------
    to_string():
        Converts the bold element to an HTML string.

    Example Usage:
    --------------
    >>> bold_elem = BoldElement(content="This is bold text.")
    >>> print(bold_elem.to_string())
    <b>This is bold text.</b>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new BoldElement instance.

        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content'.

        """
        super().__init__("b", **kwargs)


class BaseElement(BaseHTMLElement):
    """
    BaseElement Class extends BaseHTMLElement to represent HTML base elements (`<base>`).
    This class creates a base element which specifies a base URL for relative URLs in a document.

    HTML Use Cases:
    ---------------
    The `<base>` HTML element specifies a base URL to use for all relative URLs contained within a document.
    This is useful for when you have the same page HTML served under different URLs or directories but the
    other resources like images, scripts, or stylesheets are kept in one place.

    Note: The `<base>` tag must be inside the `<head>` element and it must appear only once.

    Attributes:
    -----------
    href: str (optional)
        The base URL that will be used for all relative URLs in the document.
    target: str (optional)
        The default target for all hyperlinks and forms in the document.

    Methods:
    --------
    to_string():
        Converts the base element to an HTML string.

    Example Usage:
    --------------
    >>> base_elem = BaseElement(href="https://www.example.com/", target="_blank")
    >>> print(base_elem.to_string())
    <base href="https://www.example.com/" target="_blank">

    """

    def __init__(self, href: str = None, target: str = None, **kwargs) -> None:
        """
        Initializes a new BaseElement instance.

        Parameters:
        -----------
        href: str (optional)
            The base URL that will be used for all relative URLs in the document.
        target: str (optional)
            The default target for all hyperlinks and forms in the document.

        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]

        attributes["href"] = href
        attributes["target"] = target

        super().__init__("base", attributes=attributes, **kwargs)


class BiDirectionalIsolationElement(BaseHTMLElement):
    """
    BiDirectionalIsolationElement Class extends BaseHTMLElement to represent HTML bi-directional isolation elements (`<bdi>`).
    This class creates a `<bdi>` element, which is used for isolating a part of text that might be formatted
    in a different direction from other text outside it.

    HTML Use Cases:
    ---------------
    The `<bdi>` HTML element is mainly used to isolate text when you are mixing text directions,
    such as right-to-left (RTL) and left-to-right (LTR) in the same paragraph or element.

    Note: This is especially useful in multi-language environments where text direction can change dynamically.

    Methods:
    --------
    to_string():
        Converts the bi-directional isolation element to an HTML string.

    Example Usage:
    --------------
    >>> bdi_elem = BiDirectionalIsolationElement(content="مرحبا")
    >>> print(bdi_elem.to_string())
    <bdi>مرحبا</bdi>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new BiDirectionalIsolationElement instance.

        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content'.

        """
        super().__init__("bdi", **kwargs)


class BiDirectionalOverrideElement(BaseHTMLElement):
    """
    BiDirectionalOverrideElement Class extends BaseHTMLElement to represent HTML bi-directional override elements (`<bdo>`).
    This class creates a `<bdo>` element which is used for overriding the bi-directional algorithm for displaying text.

    HTML Use Cases:
    ---------------
    The `<bdo>` HTML element is used to explicitly set the direction of embedded text within a paragraph or other block-level elements.
    It's useful when you need to change the text direction from its default behavior, which is inherited from the document or parent elements.

    Attributes:
    -----------
    dir: str
        Specifies the text direction. Acceptable values are "ltr" for Left-To-Right or "rtl" for Right-To-Left.

    Methods:
    --------
    to_string():
        Converts the bi-directional override element to an HTML string.

    Example Usage:
    --------------
    >>> bdo_elem = BiDirectionalOverrideElement(dir="rtl", content="مرحبا")
    >>> print(bdo_elem.to_string())
    <bdo dir="rtl">مرحبا</bdo>

    """

    def __init__(self, dir: str, **kwargs) -> None:
        """
        Initializes a new BiDirectionalOverrideElement instance.

        Parameters:
        -----------
        dir: str
            Specifies the text direction. Acceptable values are "ltr" for Left-To-Right or "rtl" for Right-To-Left.

        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]

        attributes['dir'] = dir

        super().__init__("bdo", attributes=attributes, **kwargs)


class BlockquoteElement(BaseHTMLElement):
    """
    BlockquoteElement Class extends BaseHTMLElement to represent HTML blockquote elements (`<blockquote>`).
    This class creates a `<blockquote>` element, which is used to indicate that the enclosed text is an extended quotation.

    HTML Use Cases:
    ---------------
    The `<blockquote>` element is often used to quote blocks of text from another source, within your document.
    It is especially useful for quoting multiple lines of text or even multiple paragraphs.

    Attributes:
    -----------
    cite: str, optional
        The URL of the quoted source, often displayed as a clickable link next to the blockquote.

    Methods:
    --------
    to_string():
        Converts the blockquote element to an HTML string.

    Example Usage:
    --------------
    >>> blockquote_elem = BlockquoteElement(cite="https://example.com", content="This is a quote.")
    >>> print(blockquote_elem.to_string())
    <blockquote cite="https://example.com">This is a quote.</blockquote>

    """

    def __init__(self, cite: str = None, **kwargs) -> None:
        """
        Initializes a new BlockquoteElement instance.

        Parameters:
        -----------
        cite: str, optional
            Specifies the URL of the quoted source.

        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content'.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]

        attributes["cite"] = cite

        super().__init__("blockquote", attributes=attributes, **kwargs)


class BodyElement(BaseHTMLElement):
    """
    BodyElement Class extends BaseHTMLElement to represent HTML body elements (`<body>`).
    This class creates a `<body>` element, which serves as the container for the visible content of an HTML document.

    HTML Use Cases:
    ---------------
    The `<body>` tag is used to define the body of an HTML document and typically contains all the content
    of a web page except for the `<head>` section. This can include text, images, links, forms, and more.

    Methods:
    --------
    to_string():
        Converts the body element to an HTML string.

    Example Usage:
    --------------
    >>> body_elem = BodyElement(content=[ParagraphElement(content="Hello, World!")])
    >>> print(body_elem.to_string())
    <body><p>Hello, World!</p></body>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new BodyElement instance.

        Parameters:
        -----------
        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content',
            which can be a list of other HTML elements to include within the <body> tag.

        """
        super().__init__("body", **kwargs)


class BreakElement(BaseHTMLElement):
    """
    BreakElement Class extends BaseHTMLElement to represent HTML break elements (`<br>`).
    This class creates a `<br>` element, which inserts a line break.

    HTML Use Cases:
    ---------------
    The `<br>` element is used to insert a line break within text, essentially moving the content
    following the `<br>` tag to the next line. It is typically used within text-based elements like
    `<p>` or `<span>` to format text.

    Methods:
    --------
    to_string():
        Converts the break element to an HTML string.

    Example Usage:
    --------------
    >>> break_elem = BreakElement()
    >>> print(break_elem.to_string())
    <br />

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new BreakElement instance.

        Parameters:
        -----------
        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'attributes'.

        """
        super().__init__("br", self_closing=True, **kwargs)


class ButtonElement(BaseHTMLElement):
    """
    ButtonElement Class extends BaseHTMLElement to represent HTML button elements (`<button>`).
    This class creates a `<button>` element, which defines a clickable button used in forms and scripts.

    HTML Use Cases:
    ---------------
    The `<button>` element is used within a form or independently to trigger an action. It allows various attributes
    such as 'type' to specify its behavior and 'formaction' to specify the URL for form submission.

    Methods:
    --------
    to_string():
        Converts the button element to an HTML string.

    Example Usage:
    --------------
    >>> btn_elem = ButtonElement(value="Click Me", type_attribute="submit")
    >>> print(btn_elem.to_string())
    <button value="Click Me" type="submit"></button>

    """

    def __init__(
            self,
            autofocus: bool = False,
            disabled: bool = False,
            form: str = None,
            formaction: str = None,
            formenctype: str = None,
            formmethod: str = None,
            formnovalidate: bool = False,
            formtarget: str = None,
            name: str = None,
            type_attribute: str = None,
            value: str = None,
            **kwargs
    ) -> None:
        """
        Initializes a new ButtonElement instance.

        Parameters:
        -----------
        autofocus: bool
            Specifies that the button should automatically get focus when the page loads.
        disabled: bool
            Specifies that the button should be disabled.
        form: str
            Specifies which form the button belongs to.
        formaction: str
            Specifies the URL of the file that will process the input control when the user submits the form.
        formenctype: str
            Specifies how form-data should be encoded before sending it to a server.
        formmethod: str
            Specifies the HTTP method for sending form-data.
        formnovalidate: bool
            Specifies that the form-data should not be validated on submission.
        formtarget: str
            Specifies where to display the response after submitting the form.
        name: str
            Specifies the name for the button.
        type_attribute: str
            Specifies the type of the button (e.g., 'submit', 'reset', 'button').
        value: str
            Specifies the initial value for the button.

        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content'.

        """
        attributes: dict[str, str | bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["autofocus"] = autofocus
        attributes["disabled"] = disabled
        attributes["form"] = form
        attributes["formaction"] = formaction
        attributes["formenctype"] = formenctype
        attributes["formmethod"] = formmethod
        attributes["formnovalidate"] = formnovalidate
        attributes["formtarget"] = formtarget
        attributes["name"] = name
        attributes["type"] = type_attribute
        attributes["value"] = value
        super().__init__("button", attributes=attributes, **kwargs)
