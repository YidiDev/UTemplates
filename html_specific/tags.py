from html_specific.base import BaseHTMLElement


class GeneralHTMLElement(BaseHTMLElement):
    def __init__(
            self,
            tag_name: str,
            attributes: dict[str, any] = None,
            content: str | BaseHTMLElement | list[str | BaseHTMLElement] = None,
            self_closing: bool = False
    ) -> None:
        super().__init__(
            tag_name=tag_name, attributes=attributes, content=content, self_closing=self_closing
        )


class CommentElement(BaseHTMLElement):
    """
    CommentElement Class extends BaseHTMLElement to represent HTML comments.
    The class takes a string as a comment and wraps it in an HTML comment tag `<!-- -->`.

    HTML Use Cases:
    ---------------
    HTML comments are useful to annotate your HTML source code, providing information
    about the code structure or explaining parts of the code for future reference.
    These comments are not displayed to the user on the web page.

    Attributes:
    -----------
    comment: str
        The text content of the HTML comment.

    Methods:
    --------
    to_string():
        Converts the comment to an HTML comment string.

    Example Usage:
    --------------
    >>> comment_elem = CommentElement("This is a sample comment")
    >>> print(comment_elem.to_string())
    <!--This is a sample comment-->

    """

    def __init__(self, comment: str, **kwargs) -> None:
        """
        Initializes a new CommentElement instance.

        Parameters:
        -----------
        comment: str
            The text content for the HTML comment.
        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class.

        """
        super().__init__(f"!--{comment}--", self_closing=True, **kwargs)


class DoctypeElement(BaseHTMLElement):
    """
    DoctypeElement Class extends BaseHTMLElement to represent the DOCTYPE declaration.
    This class creates an HTML DOCTYPE element specifying the document type and version of HTML.

    HTML Use Cases:
    ---------------
    The DOCTYPE declaration is used to define the document type and version of HTML being used.
    It should be the very first thing in an HTML document, before the <html> element.

    Attributes:
    -----------
    declaration: str
        The HTML version or standard used, such as 'html' for <!DOCTYPE html>.
        Default is 'html'.

    Methods:
    --------
    to_string():
        Converts the DOCTYPE to a DOCTYPE string.

    Example Usage:
    --------------
    >>> doctype_elem = DoctypeElement("html")
    >>> print(doctype_elem.to_string())
    <!DOCTYPE html>

    >>> doctype_elem = DoctypeElement("HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\"")
    >>> print(doctype_elem.to_string())
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

    """

    def __init__(self, declaration: str = "html", **kwargs) -> None:
        """
        Initializes a new DoctypeElement instance.

        Parameters:
        -----------
        declaration: str
            The HTML version or standard being used. Default is 'html'.
        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class.

        """
        super().__init__("!DOCTYPE", attributes={declaration: True}, self_closing=True, **kwargs)


class AnchorElement(BaseHTMLElement):
    """
    AnchorElement Class extends BaseHTMLElement to represent HTML anchor elements (`<a>`).
    This class creates an anchor element that can be used to define a hyperlink.

    HTML Use Cases:
    ---------------
    The anchor element is used to create hyperlinks to navigate to other web pages, files, or locations within the same page.
    It can also be used to activate JavaScript code.

    Attributes:
    -----------
    href: str
        Specifies the URL the link points to.
    download: str (optional)
        Specifies that the target will be downloaded when a user clicks on the hyperlink.
    hreflang: str (optional)
        Language of the linked resource.
    media: str (optional)
        Specifies what media/device the linked document is optimized for.
    ping: list[str] (optional)
        A space-separated list of URLs to which, when the link is followed, POST requests with the body PING will be sent by the browser.
    referrerpolicy: str (optional)
        Specifies which referrer information to send with the link.
    rel: str (optional)
        Specifies the relationship between the current document and the linked document.
    target: str (optional)
        Specifies where to open the linked document.
    type_attribute: str (optional)
        Specifies the media type of the linked document.

    Methods:
    --------
    to_string():
        Converts the anchor element to an HTML string.

    Example Usage:
    --------------
    >>> anchor_elem = AnchorElement(href="https://www.example.com")
    >>> print(anchor_elem.to_string())
    <a href="https://www.example.com"></a>

    >>> anchor_elem = AnchorElement(href="https://www.example.com", target="_blank", rel="noopener")
    >>> print(anchor_elem.to_string())
    <a href="https://www.example.com" target="_blank" rel="noopener"></a>

    """

    def __init__(
            self,
            href: str,
            download: str = None,
            hreflang: str = None,
            media: str = None,
            ping: list[str] = None,
            referrerpolicy: str = None,
            rel: str = None,
            target: str = None,
            type_attribute: str = None,
            **kwargs
    ) -> None:
        """
        Initializes a new AnchorElement instance.

        Parameters:
        -----------
        href: str
            The URL the link points to.
        download: str (optional)
            The download attribute.
        hreflang: str (optional)
            Language of the linked resource.
        media: str (optional)
            Media/device the linked document is optimized for.
        ping: list[str] (optional)
            List of URLs for ping attribute.
        referrerpolicy: str (optional)
            Referrer policy for the link.
        rel: str (optional)
            Relationship between current document and linked document.
        target: str (optional)
            Where to open the linked document.
        type_attribute: str (optional)
            Media type of the linked document.
        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]

        attributes["href"] = href
        attributes["download"] = download
        attributes["hreflang"] = hreflang
        attributes["media"] = media
        attributes["ping"] = ' '.join(ping) if ping else None
        attributes["referrerpolicy"] = referrerpolicy
        attributes["rel"] = rel
        attributes["target"] = target
        attributes["type"] = type_attribute

        super().__init__("a", attributes=attributes, **kwargs)


class AbbreviationElement(BaseHTMLElement):
    """
    AbbreviationElement Class extends BaseHTMLElement to represent HTML abbreviation elements (`<abbr>`).
    This class creates an abbreviation or acronym element and allows specifying a title that describes the abbreviation.

    HTML Use Cases:
    ---------------
    The `<abbr>` HTML element is used to indicate abbreviations or acronyms. The title attribute can provide an
    expansion or description for the abbreviation, which can be displayed as a tooltip when the user hovers over it.

    Attributes:
    -----------
    title: str
        Specifies the full text that the abbreviation represents.
    abbreviation: str
        The abbreviation or acronym to be displayed.

    Methods:
    --------
    to_string():
        Converts the abbreviation element to an HTML string.

    Example Usage:
    --------------
    >>> abbr_elem = AbbreviationElement(title="HyperText Markup Language", abbreviation="HTML")
    >>> print(abbr_elem.to_string())
    <abbr title="HyperText Markup Language">HTML</abbr>

    """

    def __init__(self, title: str, abbreviation: str, **kwargs) -> None:
        """
        Initializes a new AbbreviationElement instance.

        Parameters:
        -----------
        title: str
            The full text that the abbreviation represents.
        abbreviation: str
            The abbreviation or acronym to be displayed.
        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]

        attributes['title'] = title

        super().__init__("abbr", attributes=attributes, content=abbreviation, **kwargs)


class AddressElement(BaseHTMLElement):
    """
    AddressElement Class extends BaseHTMLElement to represent HTML address elements (`<address>`).
    This class creates an address element that can be used to define contact information.

    HTML Use Cases:
    ---------------
    The `<address>` HTML element is used to enclose contact information for a document or a section of a document.
    This element often appears in the footer of a document, a section, or an article.

    Methods:
    --------
    to_string():
        Converts the address element to an HTML string.

    Example Usage:
    --------------
    >>> address_elem = AddressElement(content=["1234 Elm Street", "Springfield, IL 62704"])
    >>> print(address_elem.to_string())
    <address>1234 Elm Street Springfield, IL 62704</address>

    >>> address_elem = AddressElement(content="Contact us at: <a href='mailto:webmaster@example.com'>webmaster@example.com</a>")
    >>> print(address_elem.to_string())
    <address>Contact us at: <a href='mailto:webmaster@example.com'>webmaster@example.com</a></address>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new AddressElement instance.

        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content'.

        """
        super().__init__("address", **kwargs)


class AreaElement(BaseHTMLElement):
    """
    AreaElement Class extends BaseHTMLElement to represent HTML area elements (`<area>`).
    This class creates an area element that defines a clickable area within an image map.

    HTML Use Cases:
    ---------------
    The `<area>` element is used within an `<map>` element to define clickable areas on an image.
    These areas can be linked to different URLs and activated when the user clicks on them.

    Attributes:
    -----------
    alt: str (optional)
        Alternate text describing the area. Useful for accessibility.
    coords: str (optional)
        Coordinates for the area's shape. Specifies the pixel coordinates for the shape attribute.
    download: str (optional)
        Specifies that the linked resource will be downloaded when clicked.
    href: str (optional)
        URL the clickable area leads to.
    hreflang: str (optional)
        Language of the linked resource.
    media: str (optional)
        Specifies the media type for which the linked resource is optimized.
    referrerpolicy: str (optional)
        Specifies which referrer information to send when following the link.
    rel: str (optional)
        Specifies the relationship between the current document and the linked resource.
    shape: str (optional)
        Specifies the shape of the clickable area (default, rect, circle, or poly).
    target: str (optional)
        Specifies where to open the linked document.
    type_attribute: str (optional)
        Specifies the media type of the linked resource.

    Methods:
    --------
    to_string():
        Converts the area element to an HTML string.

    Example Usage:
    --------------
    >>> area_elem = AreaElement(href="#", shape="rect", coords="34,44,270,350", alt="Computer")
    >>> print(area_elem.to_string())
    <area href="#" shape="rect" coords="34,44,270,350" alt="Computer" />

    """

    def __init__(
            self,
            alt: str = None,
            coords: str = None,
            download: str = None,
            href: str = None,
            hreflang: str = None,
            media: str = None,
            referrerpolicy: str = None,
            rel: str = None,
            shape: str = None,
            target: str = None,
            type_attribute: str = None,
            **kwargs
    ) -> None:
        """
        Initializes a new AreaElement instance.

        Parameters:
        -----------
        All optional attributes correspond to their HTML attribute counterparts.

        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]

        attributes["alt"] = alt
        attributes["coords"] = coords
        attributes["download"] = download
        attributes["href"] = href
        attributes["hreflang"] = hreflang
        attributes["media"] = media
        attributes["referrerpolicy"] = referrerpolicy
        attributes["rel"] = rel
        attributes["shape"] = shape
        attributes["target"] = target
        attributes["type"] = type_attribute

        super().__init__("area", attributes=attributes, self_closing=True, **kwargs)


class ArticleElement(BaseHTMLElement):
    """
    ArticleElement Class extends BaseHTMLElement to represent HTML article elements (`<article>`).
    This class creates an article element that can be used to enclose a composition in a document,
    page, or application.

    HTML Use Cases:
    ---------------
    The `<article>` HTML element is used to enclose a self-contained composition like a blog post,
    a news story, or a forum post. An article element can contain other semantic elements like headers,
    footers, and sections, but should make sense on its own.

    Methods:
    --------
    to_string():
        Converts the article element to an HTML string.

    Example Usage:
    --------------
    >>> article_elem = ArticleElement(content=["<h1>Title</h1>", "<p>Content of the article.</p>"])
    >>> print(article_elem.to_string())
    <article><h1>Title</h1><p>Content of the article.</p></article>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new ArticleElement instance.

        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content'.

        """
        super().__init__("article", **kwargs)


class AsideElement(BaseHTMLElement):
    """
    AsideElement Class extends BaseHTMLElement to represent HTML aside elements (`<aside>`).
    This class creates an aside element that can be used to house content that is tangentially related
    to the content around it, and which can be considered separate from the main content.

    HTML Use Cases:
    ---------------
    The `<aside>` HTML element is used to contain content that is tangentially related to the content
    around it. While the content inside an `<aside>` could be relevant, removing it should not significantly
    affect the flow of the document. It's often used for sidebars, pull quotes, or advertising.

    Methods:
    --------
    to_string():
        Converts the aside element to an HTML string.

    Example Usage:
    --------------
    >>> aside_elem = AsideElement(content=["<h4>Related Links</h4>", "<ul><li><a href='#'>Link 1</a></li><li><a href='#'>Link 2</a></li></ul>"])
    >>> print(aside_elem.to_string())
    <aside><h4>Related Links</h4><ul><li><a href='#'>Link 1</a></li><li><a href='#'>Link 2</a></li></ul></aside>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new AsideElement instance.

        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content'.

        """
        super().__init__("aside", **kwargs)


class AudioElement(BaseHTMLElement):
    """
    AudioElement Class extends BaseHTMLElement to represent HTML audio elements (`<audio>`).
    This class creates an audio element that can embed audio content like songs, sound effects,
    or spoken text into HTML documents.

    HTML Use Cases:
    ---------------
    The `<audio>` HTML element is used to embed audio content in an HTML or XHTML document.
    The audio element provides options for autoplay, controlling the audio, looping, muting,
    and preloading, among others.

    Attributes:
    -----------
    autoplay: bool (optional)
        Specifies that the audio will start playing as soon as it is ready.
    controls: bool (optional)
        Specifies that audio controls should be displayed.
    loop: bool (optional)
        Specifies that the audio will start over again every time it is finished.
    muted: bool (optional)
        Specifies that the audio output should be muted.
    preload: bool (optional)
        Specifies if and how the author thinks the audio should be loaded.
    src: str (optional)
        Specifies the source URL of the audio file.

    Methods:
    --------
    to_string():
        Converts the audio element to an HTML string.

    Example Usage:
    --------------
    >>> audio_elem = AudioElement(controls=True, src="audio.mp3")
    >>> print(audio_elem.to_string())
    <audio controls src="audio.mp3"></audio>

    """

    def __init__(
            self,
            autoplay: bool = False,
            controls: bool = False,
            loop: bool = False,
            muted: bool = True,
            preload: bool = True,
            src: str = None,
            **kwargs
    ) -> None:
        """
        Initializes a new AudioElement instance.

        Parameters:
        -----------
        All optional attributes correspond to their HTML attribute counterparts.

        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class.

        """
        attributes: dict[str, str | bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]

        attributes["autoplay"] = autoplay
        attributes["controls"] = controls
        attributes["loop"] = loop
        attributes["muted"] = muted
        attributes["preload"] = preload
        attributes["src"] = src

        super().__init__("audio", attributes=attributes, **kwargs)


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


class CanvasElement(BaseHTMLElement):
    """
    CanvasElement Class extends BaseHTMLElement to represent HTML canvas elements (`<canvas>`).
    The canvas element is used to draw graphics via JavaScript, typically 2D shapes and bitmap images.

    HTML Use Cases:
    ---------------
    The `<canvas>` element provides a way to draw graphics on a web page via JavaScript APIs like WebGL and Canvas 2D.
    You can use it to render graphs, game graphics, or other visual images on the fly.

    Methods:
    --------
    to_string():
        Converts the canvas element to an HTML string.

    Example Usage:
    --------------
    >>> canvas_elem = CanvasElement(id="myCanvas", height="400", width="400")
    >>> print(canvas_elem.to_string())
    <canvas id="myCanvas" height="400" width="400"></canvas>

    """

    def __init__(
            self,
            id: str = None,
            height: str = "150",
            width: str = "300",
            **kwargs
    ) -> None:
        """
        Initializes a new CanvasElement instance.

        Parameters:
        -----------
        id: str
            Specifies a unique id for the canvas element.
        height: str
            Specifies the height of the canvas element. Default is "150".
        width: str
            Specifies the width of the canvas element. Default is "300".

        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content'.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["id"] = id
        attributes["height"] = height
        attributes["width"] = width
        super().__init__("canvas", attributes=attributes, **kwargs)


class CaptionElement(BaseHTMLElement):
    """
    CaptionElement Class extends BaseHTMLElement to represent HTML caption elements (`<caption>`).
    The caption element is used to provide a title for a `<table>` element.

    HTML Use Cases:
    ---------------
    The `<caption>` element is used within a `<table>` to provide a caption or title for the table.
    The caption appears at the top of the table and helps users understand the table's content.

    Methods:
    --------
    to_string():
        Converts the caption element to an HTML string.

    Example Usage:
    --------------
    >>> caption_elem = CaptionElement(content="Table Title")
    >>> print(caption_elem.to_string())
    <caption>Table Title</caption>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new CaptionElement instance.

        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content'.

        """
        super().__init__("caption", **kwargs)


class CiteElement(BaseHTMLElement):
    """
    CiteElement Class extends BaseHTMLElement to represent HTML cite elements (`<cite>`).
    The cite element is used to represent the title of a work (e.g., a book, a paper, an essay, a poem, etc.)

    HTML Use Cases:
    ---------------
    The `<cite>` element is used to indicate the title of a work that should be cited in a reference-like style.
    It is usually rendered in italic or some different style to highlight its purpose.

    Methods:
    --------
    to_string():
        Converts the cite element to an HTML string.

    Example Usage:
    --------------
    >>> cite_elem = CiteElement(content="The Origin of Species")
    >>> print(cite_elem.to_string())
    <cite>The Origin of Species</cite>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new CiteElement instance.

        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content'.

        """
        super().__init__("cite", **kwargs)


class CodeElement(BaseHTMLElement):
    """
    CodeElement Class extends BaseHTMLElement to represent HTML code elements (`<code>`).
    The code element is used to display inline code snippets or short pieces of computer code.

    HTML Use Cases:
    ---------------
    The `<code>` element is used to mark inline code snippets or small pieces of computer code.
    It's commonly used within paragraphs or block-level elements like `<pre>` to format the text as code.

    Methods:
    --------
    to_string():
        Converts the code element to an HTML string.

    Example Usage:
    --------------
    >>> code_elem = CodeElement(content="print('Hello, World!')")
    >>> print(code_elem.to_string())
    <code>print('Hello, World!')</code>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new CodeElement instance.

        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content'.

        """
        super().__init__("code", **kwargs)


class ColumnElement(BaseHTMLElement):
    """
    ColumnElement Class extends BaseHTMLElement to represent HTML column elements (`<col>`).
    The `<col>` element is used to specify column properties for an HTML table column group.

    HTML Use Cases:
    ---------------
    The `<col>` element is used within a `<colgroup>` element to specify formatting properties
    for one or more columns in an HTML table. The optional `span` attribute can specify the
    number of columns to which the `<col>` element should apply.

    Methods:
    --------
    to_string():
        Converts the column element to an HTML string.

    Example Usage:
    --------------
    >>> col_elem = ColumnElement(span="2")
    >>> print(col_elem.to_string())
    <col span="2">

    """

    def __init__(self, span: str = None, **kwargs) -> None:
        """
        Initializes a new ColumnElement instance.

        Parameters:
        -----------
        span : str, optional
            Specifies the number of columns the <col> element should span across in the table.

        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content'.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["span"] = span
        super().__init__("col", attributes=attributes, **kwargs)


class ColumnGroupElement(BaseHTMLElement):
    """
    ColumnGroupElement Class extends BaseHTMLElement to represent HTML column group elements (`<colgroup>`).
    The `<colgroup>` element is used to group one or more `<col>` elements that define the properties of
    table columns within the HTML table.

    HTML Use Cases:
    ---------------
    The `<colgroup>` element can be used to define a common styling or specific attributes for
    multiple columns in a table. The optional `span` attribute specifies the number of columns the
    `<colgroup>` should influence.

    Methods:
    --------
    to_string():
        Converts the column group element to an HTML string.

    Example Usage:
    --------------
    >>> colgroup_elem = ColumnGroupElement(span="2")
    >>> print(colgroup_elem.to_string())
    <colgroup span="2">

    """

    def __init__(self, span: str = None, **kwargs) -> None:
        """
        Initializes a new ColumnGroupElement instance.

        Parameters:
        -----------
        span : str, optional
            Specifies the number of columns the <colgroup> element should span across in the table.

        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content'.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["span"] = span
        super().__init__("colgroup", attributes=attributes, **kwargs)


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


class EmphasizedElement(BaseHTMLElement):
    """
    EmphasizedElement Class extends BaseHTMLElement to represent HTML emphasized text elements (`<em>`).

    HTML Use Cases:
    ---------------
    The `<em>` element is used to emphasize text. The content within an `<em>` element is typically displayed in italics by web browsers.

    Methods:
    --------
    to_string():
        Converts the emphasized element to an HTML string.

    Example Usage:
    --------------
    >>> em_elem = EmphasizedElement(content="This is important.")
    >>> print(em_elem.to_string())
    <em>This is important.</em>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new EmphasizedElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content', 'attributes', or 'self_closing'.

        """
        super().__init__("em", **kwargs)


class EmbedElement(BaseHTMLElement):
    """
    EmbedElement Class extends BaseHTMLElement to represent HTML embedded content elements (`<embed>`).

    HTML Use Cases:
    ---------------
    The `<embed>` element is used to embed external content like multimedia files (video, audio) or interactive content (Flash, etc.) into an HTML document.

    Methods:
    --------
    to_string():
        Converts the embed element to an HTML string.

    Example Usage:
    --------------
    >>> embed_elem = EmbedElement(src="video.mp4", type_attribute="video/mp4", width="640", height="480")
    >>> print(embed_elem.to_string())
    <embed src="video.mp4" type="video/mp4" width="640" height="480">

    """

    def __init__(
            self, height: str = None, src: str = None, type_attribute: str = None, width: str = None, **kwargs
    ) -> None:
        """
        Initializes a new EmbedElement instance.

        Parameters:
        -----------
        height : str, optional
            Specifies the height of the embedded content.
        src : str, optional
            Specifies the URL of the embedded content.
        type_attribute : str, optional
            Specifies the MIME type of the embedded content.
        width : str, optional
            Specifies the width of the embedded content.
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content', 'attributes', or 'self_closing'.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["height"] = height
        attributes["src"] = src
        attributes["type_attribute"] = type_attribute
        attributes["width"] = width
        super().__init__("embed", attributes=attributes, **kwargs)


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


class HeadingElement(BaseHTMLElement):
    """
    HeadingElement Class extends BaseHTMLElement to represent HTML heading elements (`<h1>`, `<h2>`, ..., `<h6>`).

    HTML Use Cases:
    ---------------
    The HTML heading elements represent six levels of headings, `<h1>` being the highest level and `<h6>` the lowest.
    They are block-level elements that introduce new sections and subsections in a page's content.

    Methods:
    --------
    to_string():
        Converts the heading element to an HTML string.

    Example Usage:
    --------------
    >>> heading_elem = HeadingElement(1, content="Main Title")
    >>> print(heading_elem.to_string())
    <h1>Main Title</h1>

    """

    def __init__(self, level: int, **kwargs) -> None:
        """
        Initializes a new HeadingElement instance.

        Parameters:
        -----------
        level : int
            Specifies the heading level. Valid values are integers from 1 to 6, where 1 corresponds to <h1> and 6 to <h6>.

        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content', 'attributes', or 'self_closing'.

        Raises:
        -------
        Prints a warning message if the provided level is outside of the range 1-6.
        """
        if level > 6 or level < 1:
            print("WARNING: valid heading elements should be between 1 and 6")
        super().__init__(f"h{level}", **kwargs)


class HeadElement(BaseHTMLElement):
    """
    HeadElement Class extends BaseHTMLElement to represent the HTML `<head>` element.

    HTML Use Cases:
    ---------------
    The HTML `<head>` element contains meta-information about the document and links to external resources.
    It can include elements like `<title>`, `<link>`, `<meta>`, `<script>`, etc., but it should not contain any content
    that is rendered on the web page itself.

    Methods:
    --------
    to_string():
        Converts the head element to an HTML string.

    Example Usage:
    --------------
    >>> head_elem = HeadElement(content=[TitleElement(content="My Web Page"), MetaElement(charset="UTF-8")])
    >>> print(head_elem.to_string())
    <head><title>My Web Page</title><meta charset="UTF-8"></head>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new HeadElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class,
            such as 'content', 'attributes', or 'self_closing'.
        """
        super().__init__("head", **kwargs)


class HeaderElement(BaseHTMLElement):
    """
    HeaderElement Class extends BaseHTMLElement to represent the HTML `<header>` element.

    HTML Use Cases:
    ---------------
    The HTML `<header>` element is used to contain introductory and navigational information
    for its nearest ancestor block-level section. It often contains elements like site logos,
    titles, and navigation menus.

    Methods:
    --------
    to_string():
        Converts the header element to an HTML string.

    Example Usage:
    --------------
    >>> header_elem = HeaderElement(content=[ParagraphElement(content="Welcome to My Website"), NavElement()])
    >>> print(header_elem.to_string())
    <header><p>Welcome to My Website</p><nav></nav></header>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new HeaderElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class,
            such as 'content', 'attributes', or 'self_closing'.
        """
        super().__init__("header", **kwargs)


class HorizontalRuleElement(BaseHTMLElement):
    """
    HorizontalRuleElement Class extends BaseHTMLElement to represent the HTML `<hr>` element.

    HTML Use Cases:
    ---------------
    The HTML `<hr>` element is used to represent a thematic break in the content. It's often used
    to separate content or create visual breaks in a page.

    Methods:
    --------
    to_string():
        Converts the horizontal rule element to an HTML string.

    Example Usage:
    --------------
    >>> hr_elem = HorizontalRuleElement()
    >>> print(hr_elem.to_string())
    <hr />

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new HorizontalRuleElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class,
            such as 'attributes'.
        """
        super().__init__("hr", self_closing=True, **kwargs)


class HTMLElement(BaseHTMLElement):
    """
    HTMLElement Class extends BaseHTMLElement to represent the HTML `<html>` element.

    HTML Use Cases:
    ---------------
    The HTML `<html>` element is the root element that encloses all the other HTML elements on the page.
    It serves as the container for the entire HTML document.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> html_elem = HTMLElement()
    >>> print(html_elem.to_string())
    <html></html>

    >>> html_elem_with_xmlns = HTMLElement(xmlns="http://www.w3.org/1999/xhtml")
    >>> print(html_elem_with_xmlns.to_string())
    <html xmlns="http://www.w3.org/1999/xhtml"></html>

    """

    def __init__(self, xmlns: str = None, **kwargs) -> None:
        """
        Initializes a new HTMLElement instance.

        Parameters:
        -----------
        xmlns : str, optional
            Defines the XML namespace. Commonly used when serving XHTML.

        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class,
            such as 'attributes'.
        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["xmlns"] = xmlns
        super().__init__("html", attributes=attributes, **kwargs)


class ItalicizedElement(BaseHTMLElement):
    """
    ItalicizedElement Class extends BaseHTMLElement to represent the HTML `<i>` element.

    HTML Use Cases:
    ---------------
    The HTML `<i>` element is used to denote text in an alternate voice or mood, such as technical terms,
    idiomatic phrases from another language, or thoughts. Note that semantic italic text should be created
    with the <em> element for emphasizing text.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> italic_elem = ItalicizedElement(content="italic text")
    >>> print(italic_elem.to_string())
    <i>italic text</i>
    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new ItalicizedElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class,
            such as 'attributes' or 'content'.
        """
        super().__init__("i", **kwargs)


class InlineFrameElement(BaseHTMLElement):
    """
    InlineFrameElement Class extends BaseHTMLElement to represent the HTML <iframe> element.

    HTML Use Cases:
    ---------------
    The HTML <iframe> element is used to embed another HTML document within the current HTML document.
    It allows for inline embedding of multimedia content like videos, interactive maps, etc.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> iframe_elem = InlineFrameElement(src="https://www.example.com")
    >>> print(iframe_elem.to_string())
    <iframe src="https://www.example.com"></iframe>
    """

    def __init__(
            self,
            allow: str = None,
            allowfullscreen: str = None,
            allowpaymentrequest: str = None,
            height: str = None,
            loading: str = None,
            name: str = None,
            referrerpolicy: str = None,
            sandbox: str = None,
            src: str = None,
            srcdoc: str = None,
            width: str = None,
            **kwargs
    ) -> None:
        """
        Initializes a new InlineFrameElement instance.

        Parameters:
        -----------
        allow : str, optional
            Feature policy to be applied to the iframe.
        allowfullscreen : str, optional
            Enables the iframe to be displayed in full-screen mode.
        allowpaymentrequest : str, optional
            Allows the iframe to make payment requests.
        height : str, optional
            Height of the iframe in pixels or percentage.
        loading : str, optional
            Provides a hint to the browser about how the iframe should be loaded.
        name : str, optional
            Name of the iframe.
        referrerpolicy : str, optional
            Referrer policy for requests originating from the iframe.
        sandbox : str, optional
            Security restrictions for the iframe.
        src : str, optional
            Source URL of the embedded content.
        srcdoc : str, optional
            Content of the iframe specified inline.
        width : str, optional
            Width of the iframe in pixels or percentage.
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class,
            such as 'attributes' or 'content'.
        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["allow"] = allow
        attributes["allowfullscreen"] = allowfullscreen
        attributes["allowpaymentrequest"] = allowpaymentrequest
        attributes["height"] = height
        attributes["loading"] = loading
        attributes["name"] = name
        attributes["referrerpolicy"] = referrerpolicy
        attributes["sandbox"] = sandbox
        attributes["src"] = src
        attributes["srcdoc"] = srcdoc
        attributes["width"] = width
        super().__init__("iframe", attributes=attributes, **kwargs)


class ImageElement(BaseHTMLElement):
    """
    ImageElement Class extends BaseHTMLElement to represent the HTML <img> element.

    HTML Use Cases:
    ---------------
    The HTML <img> element is used to embed images in a document. It supports various formats
    like PNG, JPG, GIF, WebP, etc.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> img_elem = ImageElement(src="image.jpg", alt="Example Image")
    >>> print(img_elem.to_string())
    <img src="image.jpg" alt="Example Image">
    """

    def __init__(
            self,
            alt: str = None,
            crossorigin: str = None,
            height: str = None,
            ismap: bool = False,
            loading: str = None,
            longdesc: str = None,
            referrerpolicy: str = None,
            sizes: str = None,
            src: str = None,
            srcset: str = None,
            usermap: str = None,
            width: str = None,
            **kwargs
    ) -> None:
        """
        Initializes a new ImageElement instance.

        Parameters:
        -----------
        alt : str, optional
            Specifies alternate text for the image.
        crossorigin : str, optional
            Configures the CORS settings for the image.
        height : str, optional
            Specifies the height of the image.
        ismap : bool, optional
            Specifies that the image is a server-side image map.
        loading : str, optional
            Specifies how the image should be loaded ('eager' or 'lazy').
        longdesc : str, optional
            Provides a link to a long description of the image.
        referrerpolicy : str, optional
            Specifies the referrer policy for the image.
        sizes : str, optional
            Specifies the sizes of the image for responsive design.
        src : str, optional
            Specifies the source URL of the image.
        srcset : str, optional
            Specifies the source set for the image for responsive design.
        usermap : str, optional
            Specifies the image as a client-side image map.
        width : str, optional
            Specifies the width of the image.
        **kwargs : dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class,
            such as 'attributes' or 'content'.

        """
        attributes: dict[str, str | bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["alt"] = alt
        attributes["crossorigin"] = crossorigin
        attributes["height"] = height
        attributes["ismap"] = ismap
        attributes["loading"] = loading
        attributes["longdesc"] = longdesc
        attributes["referrerpolicy"] = referrerpolicy
        attributes["sizes"] = sizes
        attributes["src"] = src
        attributes["srcset"] = srcset
        attributes["usermap"] = usermap
        attributes["width"] = width
        super().__init__("img", attributes=attributes, **kwargs)


class InputElement(BaseHTMLElement):
    """
    InputElement Class extends BaseHTMLElement to represent the HTML <input> element.

    HTML Use Cases:
    ---------------
    The HTML <input> element is used within a form to declare input controls that allow
    users to input data.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> input_elem = InputElement(type="text", placeholder="Enter your name")
    >>> print(input_elem.to_string())
    <input type="text" placeholder="Enter your name">
    """

    def __init__(
            self,
            accept: str = None,
            alt: str = None,
            autocomplete: str = None,
            autofocus: bool = False,
            checked: bool = False,
            dirname: str = None,
            disabled: bool = False,
            form: str = None,
            formaction: str = None,
            formenctype: str = None,
            formmethod: str = None,
            formnovalidate: str = None,
            formtarget: str = None,
            height: str = None,
            list: str = None,
            max: str = None,
            maxlength: str = None,
            min: str = None,
            minlength: str = None,
            multiple: bool = False,
            name: str = None,
            pattern: str = None,
            placeholder: str = None,
            readonly: bool = False,
            required: bool = False,
            size: str = None,
            src: str = None,
            step: str = None,
            type: str = None,
            value: str = None,
            width: str = None,
            **kwargs
    ) -> None:
        """
        Initializes a new InputElement instance.

        Parameters:
        -----------
        accept : str, optional
            Specifies types of files that the server accepts (only for type="file").
        alt : str, optional
            Specifies an alternate text for images (only for type="image").
        autocomplete : str, optional
            Specifies whether an input element should have autocomplete enabled.
        autofocus : bool, optional
            Specifies that the input element should automatically get focus when the page loads.
        checked : bool, optional
            Specifies that an input element should be pre-selected when the page loads (for type="checkbox" or type="radio").
        dirname : str, optional
            Specifies the name for a text-area for holding the form control name during form submission.
        disabled : bool, optional
            Specifies that the input element should be disabled.
        form : str, optional
            Specifies the form the input element belongs to.
        formaction : str, optional
            Specifies where to send the form-data when a form is submitted (only for type="submit").
        formenctype : str, optional
            Specifies how form-data should be encoded before sending it to a server (only for type="submit").
        formmethod : str, optional
            Specifies the HTTP method for sending form-data (only for type="submit").
        formnovalidate : str, optional
            Specifies that the form-data should not be validated on submission (only for type="submit").
        formtarget : str, optional
            Specifies where to display the response after submitting the form (only for type="submit").
        height : str, optional
            Specifies the height of the input element (only for type="image").
        list : str, optional
            Specifies a datalist element that contains pre-defined options for an input element.
        max : str, optional
            Specifies the maximum value for an input element.
        maxlength : str, optional
            Specifies the maximum number of characters allowed in an input element.
        min : str, optional
            Specifies a minimum value for an input element.
        minlength : str, optional
            Specifies the minimum number of characters required in an input element.
        multiple : bool, optional
            Specifies that a user can enter more than one value in an input element.
        name : str, optional
            Specifies the name for the input element.
        pattern : str, optional
            Specifies a regular expression that an input element's value is checked against.
        placeholder : str, optional
            Specifies a short hint that describes the expected value of an input element.
        readonly : bool, optional
            Specifies that the input element is read-only.
        required : bool, optional
            Specifies that the input element must be filled out before submitting the form.
        size : str, optional
            Specifies the width, in characters, of an input element.
        src : str, optional
            Specifies the source URL for an image input.
        step : str, optional
            Specifies the legal number intervals for an input element.
        type : str, optional
            Specifies the type of input element to display.
        value : str, optional
            Specifies the value of an input element.
        width : str, optional
            Specifies the width of the input element (only for type="image").
        **kwargs : dict
        """

        attributes: dict[str, str | bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["accept"] = accept
        attributes["alt"] = alt
        attributes["autocomplete"] = autocomplete
        attributes["autofocus"] = autofocus
        attributes["checked"] = checked
        attributes["dirname"] = dirname
        attributes["disabled"] = disabled
        attributes["form"] = form
        attributes["formaction"] = formaction
        attributes["formenctype"] = formenctype
        attributes["formmethod"] = formmethod
        attributes["formnovalidate"] = formnovalidate
        attributes["formtarget"] = formtarget
        attributes["height"] = height
        attributes["list"] = list
        attributes["max"] = max
        attributes["maxlength"] = maxlength
        attributes["min"] = min
        attributes["minlength"] = minlength
        attributes["multiple"] = multiple
        attributes["name"] = name
        attributes["pattern"] = pattern
        attributes["placeholder"] = placeholder
        attributes["readonly"] = readonly
        attributes["required"] = required
        attributes["size"] = size
        attributes["src"] = src
        attributes["step"] = step
        attributes["type"] = type
        attributes["value"] = value
        attributes["width"] = width
        super().__init__("input", attributes=attributes, **kwargs)


class InsertElement(BaseHTMLElement):
    """
    InsertElement Class extends BaseHTMLElement to represent the HTML <ins> element.

    HTML Use Cases:
    ---------------
    The HTML <ins> element is used to indicate text that has been inserted into a document.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> ins_elem = InsertElement(cite="https://example.com", datetime="2023-01-01T00:00:00Z", content="Inserted text")
    >>> print(ins_elem.to_string())
    <ins cite="https://example.com" datetime="2023-01-01T00:00:00Z">Inserted text</ins>
    """

    def __init__(self, cite: str = None, datetime: str = None, **kwargs) -> None:
        """
        Initializes a new InsertElement instance.

        Parameters:
        -----------
        cite : str, optional
            Specifies a URL to a document that explains the reason why the text was inserted/changed.
        datetime : str, optional
            Specifies the date and time when the text was inserted or changed.
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.
        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['cite'] = cite
        attributes['datetime'] = datetime
        super().__init__("ins", attributes=attributes, **kwargs)


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
        attributes['form'] = form
        super().__init__("label", attributes=attributes, **kwargs)


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
            crossorigin: str = None,
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
        crossorigin : str, optional
            Specifies how the element handles crossorigin requests.
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
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['crossorigin'] = crossorigin
        attributes['href'] = href
        attributes['hreflang'] = hreflang
        attributes['media'] = media
        attributes['referrerpolicy'] = referrerpolicy
        attributes['rel'] = rel
        attributes['sizes'] = sizes
        attributes['title'] = title
        attributes['type'] = type
        super().__init__("link", attributes=attributes, **kwargs)


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
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['name'] = name
        super().__init__("map", attributes=attributes, **kwargs)


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
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['charset'] = charset
        attributes['content'] = content
        attributes['http-equiv'] = http_equiv
        attributes['name'] = name
        super().__init__("meta", attributes=attributes, **kwargs)


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
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['form'] = form
        attributes['high'] = high
        attributes['low'] = low
        attributes['max'] = max
        attributes['min'] = min
        attributes['optimum'] = optimum
        attributes['value'] = value
        super().__init__("meter", attributes=attributes, **kwargs)


class NavigationElement(BaseHTMLElement):
    """
    NavigationElement Class extends BaseHTMLElement to represent the HTML <nav> element.

    HTML Use Cases:
    ---------------
    The HTML <nav> element represents a section of a page that contains navigation links,
    such as menus, tables of contents, or indexes.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> nav_elem = NavigationElement()
    >>> print(nav_elem.to_string())
    <nav></nav>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new NavigationElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("nav", **kwargs)


class NoScriptElement(BaseHTMLElement):
    """
    NoScriptElement Class extends BaseHTMLElement to represent the HTML <noscript> element.

    HTML Use Cases:
    ---------------
    The HTML <noscript> element is used to provide an alternative content for users who have
    disabled JavaScript in their browser or have a browser that doesn't support JavaScript.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> noscript_elem = NoScriptElement()
    >>> print(noscript_elem.to_string())
    <noscript></noscript>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new NoScriptElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("noscript", **kwargs)


class ObjectElement(BaseHTMLElement):
    """
    ObjectElement Class extends BaseHTMLElement to represent the HTML <object> element.

    HTML Use Cases:
    ---------------
    The HTML <object> element is used to embed external resources, such as images, videos, or
    other multimedia content, into a web page.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> object_elem = ObjectElement(data="example.mp4", width="300", height="200")
    >>> print(object_elem.to_string())
    <object data="example.mp4" width="300" height="200"></object>

    """

    def __init__(
            self,
            data: str = None,
            form: str = None,
            height: str = None,
            name: str = None,
            type: str = None,
            typemustmatch: str = None,
            usemap: str = None,
            width: str = None,
            **kwargs
    ) -> None:
        """
        Initializes a new ObjectElement instance.

        Parameters:
        -----------
        data : str, optional
            The URL of the external resource to be embedded.
        form : str, optional
            The form element's ID that the object element is associated with.
        height : str, optional
            The height of the embedded object.
        name : str, optional
            The name of the embedded object.
        type : str, optional
            The MIME type of the embedded object.
        typemustmatch : str, optional
            Indicates that the type attribute must match the type of the embedded content.
        usemap : str, optional
            The name of a map element that defines image map information.
        width : str, optional
            The width of the embedded object.
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['data'] = data
        attributes['form'] = form
        attributes['height'] = height
        attributes['name'] = name
        attributes['type'] = type
        attributes['typemustmatch'] = typemustmatch
        attributes['usemap'] = usemap
        attributes['width'] = width
        super().__init__("object", attributes=attributes, **kwargs)


class OrderedListElement(BaseHTMLElement):
    """
    OrderedListElement Class extends BaseHTMLElement to represent the HTML <ol> element.

    HTML Use Cases:
    ---------------
    The HTML <ol> element is used to create an ordered list, where list items are
    automatically numbered.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> ol_elem = OrderedListElement()
    >>> ol_elem.add_child("li", "Item 1")
    >>> ol_elem.add_child("li", "Item 2")
    >>> print(ol_elem.to_string())
    <ol>
        <li>Item 1</li>
        <li>Item 2</li>
    </ol>

    """

    def __init__(self, reversed: bool = False, start: str = None, type: str = None, **kwargs) -> None:
        """
        Initializes a new OrderedListElement instance.

        Parameters:
        -----------
        reversed : bool, optional
            Specifies whether the list should be displayed in reverse order.
        start : str, optional
            Specifies the starting value for the list.
        type : str, optional
            Specifies the type of numbering or bullet style for the list.
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['reversed'] = reversed
        attributes['start'] = start
        attributes['type'] = type
        super().__init__("ol", attributes=attributes, **kwargs)


class OptionGroupElement(BaseHTMLElement):
    """
    OptionGroupElement Class extends BaseHTMLElement to represent the HTML <optgroup> element.

    HTML Use Cases:
    ---------------
    The HTML <optgroup> element is used to group a set of related <option> elements within a <select> element.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> optgroup_elem = OptionGroupElement(label="Group 1")
    >>> optgroup_elem.add_child("option", "Option 1")
    >>> optgroup_elem.add_child("option", "Option 2")
    >>> print(optgroup_elem.to_string())
    <optgroup label="Group 1">
        <option>Option 1</option>
        <option>Option 2</option>
    </optgroup>

    """

    def __init__(self, disabled: bool = False, label: str = None, **kwargs) -> None:
        """
        Initializes a new OptionGroupElement instance.

        Parameters:
        -----------
        disabled : bool, optional
            Specifies whether the <optgroup> should be disabled.
        label : str, optional
            Specifies the label or title for the <optgroup>.
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes: dict[str, str | bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['disabled'] = disabled
        attributes['label'] = label
        super().__init__("optgroup", attributes=attributes, **kwargs)


class OptionElement(BaseHTMLElement):
    """
    OptionElement Class extends BaseHTMLElement to represent the HTML <option> element.

    HTML Use Cases:
    ---------------
    The HTML <option> element is used to define an option in a <select> element.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> option_elem = OptionElement(value="option_value", label="Option Label", selected=True)
    >>> print(option_elem.to_string())
    <option value="option_value" label="Option Label" selected>Option Label</option>

    """

    def __init__(
            self, disabled: bool = False, label: str = None, selected: bool = False, value: str = None, **kwargs
    ) -> None:
        """
        Initializes a new OptionElement instance.

        Parameters:
        -----------
        disabled : bool, optional
            Specifies whether the <option> should be disabled.
        label : str, optional
            Specifies the label or text for the <option>.
        selected : bool, optional
            Specifies whether the <option> should be selected by default.
        value : str, optional
            Specifies the value associated with the <option>.
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes: dict[str, str | bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['disabled'] = disabled
        attributes['label'] = label
        attributes['selected'] = selected
        attributes['value'] = value
        super().__init__("option", attributes=attributes, **kwargs)


class OutputElement(BaseHTMLElement):
    """
    OutputElement Class extends BaseHTMLElement to represent the HTML <output> element.

    HTML Use Cases:
    ---------------
    The HTML <output> element represents the result of a calculation or user action.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    >>> output_elem = OutputElement(for_attribute="result", form="calculation", name="output_result")
    >>> print(output_elem.to_string())
    <output for="result" form="calculation" name="output_result"></output>

    """

    def __init__(self, for_attribute: str = None, form: str = None, name: str = None, **kwargs) -> None:
        """
        Initializes a new OutputElement instance.

        Parameters:
        -----------
        for_attribute : str, optional
            Specifies the ID of the associated form control element.
        form : str, optional
            Specifies the ID of the form element that this output element belongs to.
        name : str, optional
            Specifies the name of the output element.
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['for'] = for_attribute
        attributes['form'] = form
        attributes['name'] = name
        super().__init__("output", attributes=attributes, **kwargs)


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


class ShortQuotationElement(BaseHTMLElement):
    """
    ShortQuotationElement Class extends BaseHTMLElement to represent the HTML <q> element.

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
    >>> quote_elem = ShortQuotationElement(cite="https://example.com/quote-source")
    >>> quote_elem.content.append("This is a short quotation.")
    >>> print(quote_elem.to_string())
    <q cite="https://example.com/quote-source">This is a short quotation.</q>

    """

    def __init__(self, cite: str = None, **kwargs) -> None:
        """
        Initializes a new ShortQuotationElement instance.

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


class RubyParenthesesElement(BaseHTMLElement):
    """
    RubyParenthesesElement Class extends BaseHTMLElement to represent the HTML <rp> element.

    HTML Use Cases:
    ---------------
    The HTML <rp> element is used to provide parentheses for the ruby text in a ruby annotation.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    # Create a RubyParenthesesElement
    >>> rp_elem = RubyParenthesesElement()

    # Convert it to an HTML string
    >>> print(rp_elem.to_string())
    <rp></rp>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new RubyParenthesesElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("rp", **kwargs)


class RubyTextElement(BaseHTMLElement):
    """
    RubyTextElement Class extends BaseHTMLElement to represent the HTML <rt> element.

    HTML Use Cases:
    ---------------
    The HTML <rt> element is used to provide the ruby text component of a ruby annotation.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    # Create a RubyTextElement
    >>> rt_elem = RubyTextElement()

    # Convert it to an HTML string
    >>> print(rt_elem.to_string())
    <rt></rt>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new RubyTextElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("rt", **kwargs)


class RubyElement(BaseHTMLElement):
    """
    RubyElement Class extends BaseHTMLElement to represent the HTML <ruby> element.

    HTML Use Cases:
    ---------------
    The HTML <ruby> element is used to specify a ruby annotation, which is used for phonetic
    annotations in East Asian typography.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    # Create a RubyElement
    >>> ruby_elem = RubyElement()

    # Convert it to an HTML string
    >>> print(ruby_elem.to_string())
    <ruby></ruby>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new RubyElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("ruby", **kwargs)


class StruckThroughElement(BaseHTMLElement):
    """
    StruckThroughElement Class extends BaseHTMLElement to represent the HTML <s> element.

    HTML Use Cases:
    ---------------
    The HTML <s> element is used to represent text that is no longer accurate or relevant.
    It typically renders the text with a line through it.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    # Create a StruckThroughElement
    >>> s_elem = StruckThroughElement()

    # Convert it to an HTML string
    >>> print(s_elem.to_string())
    <s></s>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new StruckThroughElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("s", **kwargs)


class SampleElement(BaseHTMLElement):
    """
    SampleElement Class extends BaseHTMLElement to represent the HTML <samp> element.

    HTML Use Cases:
    ---------------
    The HTML <samp> element is used to define sample output or example text. It typically represents
    text that is a sample of how something might appear, such as program code output or user input.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    # Create a SampleElement
    >>> samp_elem = SampleElement()

    # Convert it to an HTML string
    >>> print(samp_elem.to_string())
    <samp></samp>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new SampleElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("samp", **kwargs)


class ScriptElement(BaseHTMLElement):
    """
    ScriptElement Class extends BaseHTMLElement to represent the HTML <script> element.

    HTML Use Cases:
    ---------------
    The HTML <script> element is used to embed or reference client-side JavaScript code in an HTML document.
    It can be used for various purposes, including adding interactivity and functionality to web pages.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    # Create a ScriptElement with an external script source
    >>> script_elem = ScriptElement(src="myscript.js", type="text/javascript")

    # Convert it to an HTML string
    >>> print(script_elem.to_string())
    <script src="myscript.js" type="text/javascript"></script>

    """

    def __init__(
            self,
            async_attribute: bool = False,
            crossorigin: str = None,
            defer: bool = False,
            integrity: str = None,
            nomodule: str = None,
            referrerpolicy: str = None,
            src: str = None,
            type: str = None,
            **kwargs
    ) -> None:
        """
        Initializes a new ScriptElement instance.

        Parameters:
        -----------
        async_attribute : bool, optional
            Specifies whether the script should be executed asynchronously (default is False).
        crossorigin : str, optional
            Specifies how the script can be loaded from a different origin (e.g., "anonymous", "use-credentials").
        defer : bool, optional
            Specifies whether the script execution should be deferred until after the page is parsed (default is False).
        integrity : str, optional
            A cryptographic hash of the script file for enhanced security.
        nomodule : str, optional
            Specifies that the script should not be executed in modules supporting modern JavaScript (e.g., ES6).
        referrerpolicy : str, optional
            Specifies the policy for sending the Referer header when fetching the script (e.g., "no-referrer").
        src : str, optional
            Specifies the URL of an external script file.
        type : str, optional
            Specifies the media type of the script (e.g., "text/javascript").

        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes: dict[str, str | bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['async'] = async_attribute
        attributes['crossorigin'] = crossorigin
        attributes['defer'] = defer
        attributes['integrity'] = integrity
        attributes['nomodule'] = nomodule
        attributes['referrerpolicy'] = referrerpolicy
        attributes['src'] = src
        attributes['type'] = type
        super().__init__("script", attributes=attributes, **kwargs)


class SectionElement(BaseHTMLElement):
    """
    SectionElement Class extends BaseHTMLElement to represent the HTML <section> element.

    HTML Use Cases:
    ---------------
    The HTML <section> element is used to define sections or thematic groupings of content
    within an HTML document. It is often used to structure and organize content on a webpage.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    # Create a SectionElement
    >>> section_elem = SectionElement()

    # Convert it to an HTML string
    >>> print(section_elem.to_string())
    <section></section>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new SectionElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("section", **kwargs)


class SelectElement(BaseHTMLElement):
    """
    SelectElement Class extends BaseHTMLElement to represent the HTML <select> element.

    HTML Use Cases:
    ---------------
    The HTML <select> element is used to create a dropdown list or a list box control.
    It allows users to select one or multiple options from a list.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    # Create a SelectElement with options
    >>> select_elem = SelectElement(name="color")
    >>> option1 = OptionElement(value="red", content="Red")
    >>> option2 = OptionElement(value="green", content="Green")
    >>> select_elem.add_content(option1)
    >>> select_elem.add_content(option2)

    # Convert it to an HTML string
    >>> print(select_elem.to_string())
    <select name="color">
        <option value="red">Red</option>
        <option value="green">Green</option>
    </select>

    """

    def __init__(
            self,
            autofocus: bool = False,
            disabled: bool = False,
            form: str = None,
            multiple: bool = False,
            name: str = None,
            required: bool = False,
            size: str = None,
            **kwargs
    ) -> None:
        """
        Initializes a new SelectElement instance.

        Parameters:
        -----------
        autofocus : bool, optional
            Indicates whether the select element should automatically get focus when the page loads.
        disabled : bool, optional
            Indicates whether the select element should be disabled.
        form : str, optional
            Specifies the form element the select element belongs to.
        multiple : bool, optional
            Indicates whether multiple options can be selected.
        name : str, optional
            Specifies the name attribute for the select element.
        required : bool, optional
            Indicates whether the select element is required.
        size : str, optional
            Specifies the number of visible options in a dropdown list.

        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes: dict[str, str | bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['autofocus'] = autofocus
        attributes['disabled'] = disabled
        attributes['form'] = form
        attributes['multiple'] = multiple
        attributes['name'] = name
        attributes['required'] = required
        attributes['size'] = size
        super().__init__("select", attributes=attributes, **kwargs)


class SmallElement(BaseHTMLElement):
    """
    SmallElement Class extends BaseHTMLElement to represent the HTML <small> element.

    HTML Use Cases:
    ---------------
    The HTML <small> element is used to make the text size smaller than the surrounding text.
    It is typically used for fine print, legal disclaimers, and other small annotations.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Example Usage:
    --------------
    # Create a SmallElement with content
    >>> small_elem = SmallElement(content="This is small text.")

    # Convert it to an HTML string
    >>> print(small_elem.to_string())
    <small>This is small text.</small>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new SmallElement instance.

        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("small", **kwargs)


class SourceElement(BaseHTMLElement):
    """
    SourceElement Class extends BaseHTMLElement to represent the HTML <source> element.

    HTML Use Cases:
    ---------------
    The HTML <source> element is used to specify multiple media resources for the <picture>, <audio>,
    and <video> elements. It allows the browser to choose the most suitable media resource based
    on the device's capabilities and the media type.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Parameters:
    -----------
    media : str, optional
        Specifies the media type of the resource. Example: "screen and (min-width: 768px)".

    sizes : str, optional
        Specifies the sizes of the image or media resource for different viewport sizes.
        Example: "100vw".

    src : str, optional
        Specifies the URL of the media resource.

    srcset : str, optional
        Specifies a comma-separated list of image sources and their descriptors.
        Example: "image.jpg 1024w, image-small.jpg 320w".

    type : str, optional
        Specifies the MIME type of the resource.
        Example: "image/jpeg".

    Example Usage:
    --------------
    # Create a SourceElement for responsive image loading
    >>> source_elem = SourceElement(
    ...     media="(min-width: 768px)",
    ...     sizes="100vw",
    ...     srcset="image.jpg 1024w, image-small.jpg 320w",
    ...     type="image/jpeg"
    ... )

    # Convert it to an HTML string
    >>> print(source_elem.to_string())
    <source media="(min-width: 768px)" sizes="100vw" srcset="image.jpg 1024w, image-small.jpg 320w" type="image/jpeg">

    """

    def __init__(
            self, media: str = None, sizes: str = None, src: str = None, srcset: str = None, type: str = None, **kwargs
    ) -> None:
        """
        Initializes a new SourceElement instance.

        Parameters:
        -----------
        media : str, optional
            Specifies the media type of the resource.

        sizes : str, optional
            Specifies the sizes of the image or media resource.

        src : str, optional
            Specifies the URL of the media resource.

        srcset : str, optional
            Specifies a comma-separated list of image sources and their descriptors.

        type : str, optional
            Specifies the MIME type of the resource.

        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['media'] = media
        attributes['sizes'] = sizes
        attributes['src'] = src
        attributes['srcset'] = srcset
        attributes['type'] = type
        super().__init__("source", attributes=attributes, **kwargs)


class SpanElement(BaseHTMLElement):
    """
    SpanElement Class extends BaseHTMLElement to represent the HTML <span> element.

    HTML Use Cases:
    ---------------
    The HTML <span> element is an inline container used to apply styles or scripts to a specific
    portion of text within a larger text block. It doesn't add any visual or semantic meaning to
    its content but can be styled or manipulated using CSS or JavaScript.

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
    # Create a SpanElement with some text content
    >>> span_elem = SpanElement(content="This is a styled span.")

    # Convert it to an HTML string
    >>> print(span_elem.to_string())
    <span>This is a styled span.</span>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new SpanElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("span", **kwargs)


class StrongElement(BaseHTMLElement):
    """
    StrongElement Class extends BaseHTMLElement to represent the HTML <strong> element.

    HTML Use Cases:
    ---------------
    The HTML <strong> element is used to indicate text with strong importance or emphasis.
    Browsers typically render the content of this element in bold.

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
    # Create a StrongElement with some emphasized text
    >>> strong_elem = StrongElement(content="This is important.")

    # Convert it to an HTML string
    >>> print(strong_elem.to_string())
    <strong>This is important.</strong>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new StrongElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("strong", **kwargs)


class StyleElement(BaseHTMLElement):
    """
    StyleElement Class extends BaseHTMLElement to represent the HTML <style> element.

    HTML Use Cases:
    ---------------
    The HTML <style> element is used to embed CSS (Cascading Style Sheets) code within an HTML document.
    It can be placed in the <head> section of an HTML document to define the document's styles.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Parameters:
    -----------
    media : str, optional
        Specifies the media type for which the styles are intended, e.g., "screen" or "print".
    type : str, optional
        Specifies the type of stylesheet language being used, e.g., "text/css".

    **kwargs : dict
        Additional keyword arguments that are passed to the parent class.

    Example Usage:
    --------------
    # Create a StyleElement with CSS code
    >>> css_code = "body { background-color: lightblue; }"
    >>> style_elem = StyleElement(content=css_code, type="text/css")

    # Convert it to an HTML string
    >>> print(style_elem.to_string())
    <style type="text/css">body { background-color: lightblue; }</style>

    """

    def __init__(self, media: str = None, type: str = None, **kwargs) -> None:
        """
        Initializes a new StyleElement instance.

        Parameters:
        -----------
        media : str, optional
            Specifies the media type for which the styles are intended, e.g., "screen" or "print".
        type : str, optional
            Specifies the type of stylesheet language being used, e.g., "text/css".

        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["media"] = media
        attributes["type"] = type
        super().__init__("style", attributes=attributes, **kwargs)


class SubscriptElement(BaseHTMLElement):
    """
    SubscriptElement Class extends BaseHTMLElement to represent the HTML <sub> element.

    HTML Use Cases:
    ---------------
    The HTML <sub> element is used to define subscripted text. Subscripted text is typically rendered
    lower and smaller than the surrounding text and is commonly used for mathematical notations,
    chemical formulas, and footnotes.

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
    # Create a SubscriptElement with subscripted text
    >>> sub_elem = SubscriptElement(content="H2O")

    # Convert it to an HTML string
    >>> print(sub_elem.to_string())
    <sub>H2O</sub>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new SubscriptElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("sub", **kwargs)


class SummaryElement(BaseHTMLElement):
    """
    SummaryElement Class extends BaseHTMLElement to represent the HTML <summary> element.

    HTML Use Cases:
    ---------------
    The HTML <summary> element is used as a child of the <details> element to provide a visible
    summary or label for the details content. When a user interacts with the <details> element,
    the content controlled by it can be collapsed or expanded, and the summary provides a
    clickable label for this interaction.

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
    # Create a SummaryElement with a summary text
    >>> summary_elem = SummaryElement(content="More Info")

    # Convert it to an HTML string
    >>> print(summary_elem.to_string())
    <summary>More Info</summary>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new SummaryElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("summary", **kwargs)


class SuperscriptElement(BaseHTMLElement):
    """
    SuperscriptElement Class extends BaseHTMLElement to represent the HTML <sup> element.

    HTML Use Cases:
    ---------------
    The HTML <sup> element is used to define text that should be displayed as superscript.
    Superscript text appears smaller and above the baseline of the regular text, typically used
    for mathematical notations, footnotes, or citations.

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
    # Create a SuperscriptElement with superscript text
    >>> superscript_elem = SuperscriptElement(content="2")

    # Convert it to an HTML string
    >>> print(superscript_elem.to_string())
    <sup>2</sup>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new SuperscriptElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("sup", **kwargs)


class SVGElement(BaseHTMLElement):
    """
    SVGElement Class extends BaseHTMLElement to represent the HTML <svg> element.

    HTML Use Cases:
    ---------------
    The HTML <svg> element is used to embed scalable vector graphics (SVG) in an HTML document.
    SVG is a vector image format that allows for high-quality graphics and animations to be
    displayed in web pages.

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
    # Create an SVGElement with SVG content
    >>> svg_content = '<circle cx="50" cy="50" r="40" stroke="black" stroke-width="2" fill="red" />'
    >>> svg_elem = SVGElement(content=svg_content)

    # Convert it to an HTML string
    >>> print(svg_elem.to_string())
    <svg>
        <circle cx="50" cy="50" r="40" stroke="black" stroke-width="2" fill="red"></circle>
    </svg>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new SVGElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("svg", **kwargs)


class TableElement(BaseHTMLElement):
    """
    TableElement Class extends BaseHTMLElement to represent the HTML <table> element.

    HTML Use Cases:
    ---------------
    The HTML <table> element is used to create tables to organize data into rows and columns.
    It is one of the fundamental elements for structuring content in HTML documents.

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
    # Create a TableElement with table rows and columns
    >>> table_elem = TableElement()
    >>> table_elem.content = [
    ...     "<tr><td>Row 1, Cell 1</td><td>Row 1, Cell 2</td></tr>",
    ...     "<tr><td>Row 2, Cell 1</td><td>Row 2, Cell 2</td></tr>"
    ... ]

    # Convert it to an HTML string
    >>> print(table_elem.to_string())
    <table>
        <tr><td>Row 1, Cell 1</td><td>Row 1, Cell 2</td></tr>
        <tr><td>Row 2, Cell 1</td><td>Row 2, Cell 2</td></tr>
    </table>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new TableElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("table", **kwargs)


class TableBodyElement(BaseHTMLElement):
    """
    TableBodyElement Class extends BaseHTMLElement to represent the HTML <tbody> element.

    HTML Use Cases:
    ---------------
    The HTML <tbody> element is used as a container for one or more table rows
    (<tr> elements) that make up the body of the table. It is typically placed
    within a <table> element to group rows together.

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
    # Create a TableBodyElement with table rows
    >>> tbody_elem = TableBodyElement()
    >>> tbody_elem.content = [
    ...     "<tr><td>Row 1, Cell 1</td><td>Row 1, Cell 2</td></tr>",
    ...     "<tr><td>Row 2, Cell 1</td><td>Row 2, Cell 2</td></tr>"
    ... ]

    # Convert it to an HTML string
    >>> print(tbody_elem.to_string())
    <tbody>
        <tr><td>Row 1, Cell 1</td><td>Row 1, Cell 2</td></tr>
        <tr><td>Row 2, Cell 1</td><td>Row 2, Cell 2</td></tr>
    </tbody>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new TableBodyElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("tbody", **kwargs)


class TableDataElement(BaseHTMLElement):
    """
    TableDataElement Class extends BaseHTMLElement to represent the HTML <td> element.

    HTML Use Cases:
    ---------------
    The HTML <td> element is used to define a cell within an HTML table. It can
    contain data, such as text or other HTML elements, and is typically used within
    table rows (<tr> elements) in conjunction with table headers (<th> elements) or
    other data cells.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Parameters:
    -----------
    colspan : str, optional
        Specifies the number of columns that the cell should span.
    headers : str, optional
        Specifies a space-separated list of header cell IDs that are associated
        with the data cell. Used for accessibility and linking.
    rowspan : str, optional
        Specifies the number of rows that the cell should span.

    **kwargs : dict
        Additional keyword arguments that are passed to the parent class.

    Example Usage:
    --------------
    # Create a TableDataElement with content
    >>> td_elem = TableDataElement()
    >>> td_elem.content = "Cell Data"

    # Convert it to an HTML string
    >>> print(td_elem.to_string())
    <td>Cell Data</td>

    # Create a TableDataElement with colspan and rowspan
    >>> td_elem2 = TableDataElement(colspan="2", rowspan="3")
    >>> td_elem2.content = "Spanned Cell Data"

    # Convert it to an HTML string
    >>> print(td_elem2.to_string())
    <td colspan="2" rowspan="3">Spanned Cell Data</td>

    """

    def __init__(self, colspan: str = None, headers: str = None, rowspan: str = None, **kwargs) -> None:
        """
        Initializes a new TableDataElement instance.

        Parameters:
        -----------
        colspan : str, optional
            Specifies the number of columns that the cell should span.
        headers : str, optional
            Specifies a space-separated list of header cell IDs that are associated
            with the data cell. Used for accessibility and linking.
        rowspan : str, optional
            Specifies the number of rows that the cell should span.
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['colspan'] = colspan
        attributes['headers'] = headers
        attributes['rowspan'] = rowspan
        super().__init__("td", attributes=attributes, **kwargs)


class TemplateElement(BaseHTMLElement):
    """
    TemplateElement Class extends BaseHTMLElement to represent the HTML <template> element.

    HTML Use Cases:
    ---------------
    The HTML <template> element is used to hold client-side content that you don't
    want to be rendered when the page loads. Instead, you can use JavaScript to
    instantiate and manipulate the content inside the template later.

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
    # Create a TemplateElement with some content
    >>> template_elem = TemplateElement()
    >>> template_elem.content = "This is a template."

    # Convert it to an HTML string
    >>> print(template_elem.to_string())
    <template>This is a template.</template>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new TemplateElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("template", **kwargs)


class TextAreaElement(BaseHTMLElement):
    """
    TextAreaElement Class extends BaseHTMLElement to represent the HTML <textarea> element.

    HTML Use Cases:
    ---------------
    The HTML <textarea> element is used to create a multi-line text input field that allows users
    to enter longer text, such as comments or descriptions.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Parameters:
    -----------
    autofocus : bool, optional (default=False)
        Specifies that the textarea should be focused automatically when the page loads.
    cols : str, optional
        Specifies the visible width of the textarea (in characters).
    dirname : str, optional
        Specifies the name of the directory for text direction.
    disabled : bool, optional (default=False)
        Specifies that the textarea should be disabled (user cannot interact with it).
    form : str, optional
        Specifies the form that the textarea belongs to.
    maxlength : str, optional
        Specifies the maximum number of characters allowed in the textarea.
    name : str, optional
        Specifies the name of the textarea, which is used when submitting the form.
    placeholder : str, optional
        Specifies a short hint that describes the expected value of the textarea.
    readonly : bool, optional (default=False)
        Specifies that the textarea is read-only (user can see the text but cannot edit it).
    required : bool, optional (default=False)
        Specifies that the textarea must be filled out before submitting the form.
    rows : str, optional
        Specifies the visible height of the textarea (in lines).
    wrap : str, optional
        Specifies how the text in the textarea should be wrapped when submitted in a form.
        Possible values are 'soft', 'hard', or None.

    Example Usage:
    --------------
    # Create a TextAreaElement with some attributes
    >>> textarea_elem = TextAreaElement(
    ...     name="comment",
    ...     rows="4",
    ...     cols="40",
    ...     placeholder="Enter your comment here",
    ...     required=True
    ... )

    # Convert it to an HTML string
    >>> print(textarea_elem.to_string())
    <textarea name="comment" rows="4" cols="40" placeholder="Enter your comment here" required></textarea>

    """

    def __init__(
            self,
            autofocus: bool = False,
            cols: str = None,
            dirname: str = None,
            disabled: bool = False,
            form: str = None,
            maxlength: str = None,
            name: str = None,
            placeholder: str = None,
            readonly: bool = False,
            required: bool = False,
            rows: str = None,
            wrap: str = None,
            **kwargs
    ) -> None:
        """
        Initializes a new TextAreaElement instance.

        Parameters:
        -----------
        autofocus : bool, optional (default=False)
            Specifies that the textarea should be focused automatically when the page loads.
        cols : str, optional
            Specifies the visible width of the textarea (in characters).
        dirname : str, optional
            Specifies the name of the directory for text direction.
        disabled : bool, optional (default=False)
            Specifies that the textarea should be disabled (user cannot interact with it).
        form : str, optional
            Specifies the form that the textarea belongs to.
        maxlength : str, optional
            Specifies the maximum number of characters allowed in the textarea.
        name : str, optional
            Specifies the name of the textarea, which is used when submitting the form.
        placeholder : str, optional
            Specifies a short hint that describes the expected value of the textarea.
        readonly : bool, optional (default=False)
            Specifies that the textarea is read-only (user can see the text but cannot edit it).
        required : bool, optional (default=False)
            Specifies that the textarea must be filled out before submitting the form.
        rows : str, optional
            Specifies the visible height of the textarea (in lines).
        wrap : str, optional
            Specifies how the text in the textarea should be wrapped when submitted in a form.
            Possible values are 'soft', 'hard', or None.

        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes: dict[str, str | bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['autofocus'] = autofocus
        attributes['cols'] = cols
        attributes['dirname'] = dirname
        attributes['disabled'] = disabled
        attributes['form'] = form
        attributes['maxlength'] = maxlength
        attributes['name'] = name
        attributes['placeholder'] = placeholder
        attributes['readonly'] = readonly
        attributes['required'] = required
        attributes['rows'] = rows
        attributes['wrap'] = wrap
        super().__init__("textarea", attributes=attributes, **kwargs)


class TableFooterElement(BaseHTMLElement):
    """
    TableFooterElement Class extends BaseHTMLElement to represent the HTML <tfoot> element.

    HTML Use Cases:
    ---------------
    The HTML <tfoot> element is used to group footer content in an HTML table.

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
    # Create a TableFooterElement
    >>> tfoot_elem = TableFooterElement()

    # Convert it to an HTML string
    >>> print(tfoot_elem.to_string())
    <tfoot></tfoot>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new TableFooterElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("tfoot", **kwargs)


class TableHeaderCellElement(BaseHTMLElement):
    """
    TableHeaderCellElement Class extends BaseHTMLElement to represent the HTML <th> (table header cell) element.

    HTML Use Cases:
    ---------------
    The HTML <th> element defines a header cell in an HTML table. It is used to label the data columns in a table.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Parameters:
    -----------
    abbr : str, optional
        A text alternative for the header cell, useful for accessibility.
    colspan : str, optional
        The number of columns that the header cell should span.
    headers : str, optional
        A space-separated list of header cell IDs that the header cell is associated with.
    rowspan : str, optional
        The number of rows that the header cell should span.
    scope : str, optional
        Defines the scope of the header cell's content (e.g., 'col', 'row', 'colgroup', 'rowgroup').

    **kwargs : dict
        Additional keyword arguments that are passed to the parent class.

    Example Usage:
    --------------
    # Create a TableHeaderCellElement with attributes
    >>> th_elem = TableHeaderCellElement(abbr="Name", colspan="2")

    # Convert it to an HTML string
    >>> print(th_elem.to_string())
    <th abbr="Name" colspan="2"></th>

    """

    def __init__(
            self,
            abbr: str = None,
            colspan: str = None,
            headers: str = None,
            rowspan: str = None,
            scope: str = None,
            **kwargs
    ) -> None:
        """
        Initializes a new TableHeaderCellElement instance.

        Parameters:
        -----------
        abbr : str, optional
            A text alternative for the header cell, useful for accessibility.
        colspan : str, optional
            The number of columns that the header cell should span.
        headers : str, optional
            A space-separated list of header cell IDs that the header cell is associated with.
        rowspan : str, optional
            The number of rows that the header cell should span.
        scope : str, optional
            Defines the scope of the header cell's content (e.g., 'col', 'row', 'colgroup', 'rowgroup').

        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['abbr'] = abbr
        attributes['colspan'] = colspan
        attributes['headers'] = headers
        attributes['rowspan'] = rowspan
        attributes['scope'] = scope
        super().__init__("th", attributes=attributes, **kwargs)


class TableHeaderElement(BaseHTMLElement):
    """
    TableHeaderElement Class extends BaseHTMLElement to represent the HTML <thead> (table header) element.

    HTML Use Cases:
    ---------------
    The HTML <thead> element groups a set of table rows that contain the table's column labels.

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
    # Create a TableHeaderElement
    >>> thead_elem = TableHeaderElement()

    # Convert it to an HTML string
    >>> print(thead_elem.to_string())
    <thead></thead>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new TableHeaderElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("thead", **kwargs)


class TimeElement(BaseHTMLElement):
    """
    TimeElement Class extends BaseHTMLElement to represent the HTML <time> element.

    HTML Use Cases:
    ---------------
    The HTML <time> element represents a specific period in time, or a range of time. It can be used
    to provide machine-readable date and time information and can be styled with CSS for display.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Parameters:
    -----------
    datetime : str, optional
        A string representing the date and time. It should be in a format that can be parsed by machines.

    **kwargs : dict
        Additional keyword arguments that are passed to the parent class.

    Example Usage:
    --------------
    # Create a TimeElement with a datetime attribute
    >>> time_elem = TimeElement(datetime="2023-10-15T08:00:00Z")

    # Convert it to an HTML string
    >>> print(time_elem.to_string())
    <time datetime="2023-10-15T08:00:00Z"></time>

    """

    def __init__(self, datetime: str = None, **kwargs) -> None:
        """
        Initializes a new TimeElement instance.

        Parameters:
        -----------
        datetime : str, optional
            A string representing the date and time. It should be in a format that can be parsed by machines.

        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['datetime'] = datetime
        super().__init__("time", attributes=attributes, **kwargs)


class TitleElement(BaseHTMLElement):
    """
    TitleElement Class extends BaseHTMLElement to represent the HTML <title> element.

    HTML Use Cases:
    ---------------
    The HTML <title> element defines the title of an HTML document, which is displayed in the browser's
    title bar or tab. It is also used by search engines to index and display the page's title in search results.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    **kwargs : dict
        Additional keyword arguments that are passed to the parent class.

    Example Usage:
    --------------
    # Create a TitleElement with a title
    >>> title_elem = TitleElement()
    >>> title_elem.add_content("My Page Title")

    # Convert it to an HTML string
    >>> print(title_elem.to_string())
    <title>My Page Title</title>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new TitleElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("title", **kwargs)


class TableRowElement(BaseHTMLElement):
    """
    TableRowElement Class extends BaseHTMLElement to represent the HTML <tr> (table row) element.

    HTML Use Cases:
    ---------------
    The HTML <tr> element is used to define a row in an HTML table. It contains one or more table data cells
    (<td>) or table header cells (<th>), which define the actual content of the row.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    **kwargs : dict
        Additional keyword arguments that are passed to the parent class.

    Example Usage:
    --------------
    # Create a TableRowElement
    >>> row_elem = TableRowElement()

    # Add table data cells to the row
    >>> data_cell1 = TableDataElement()
    >>> data_cell1.add_content("Data 1")
    >>> data_cell2 = TableDataElement()
    >>> data_cell2.add_content("Data 2")
    >>> row_elem.add_content([data_cell1, data_cell2])

    # Convert it to an HTML string
    >>> print(row_elem.to_string())
    <tr>
        <td>Data 1</td>
        <td>Data 2</td>
    </tr>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new TableRowElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("tr", **kwargs)


class TrackElement(BaseHTMLElement):
    """
    TrackElement Class extends BaseHTMLElement to represent the HTML <track> element.

    HTML Use Cases:
    ---------------
    The HTML <track> element is used to provide text tracks for media elements like <video> and <audio>.
    Text tracks can include subtitles, captions, descriptions, and more.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Parameters:
    -----------
    default : bool, optional
        Specifies whether the track should be enabled by default (default is False).

    kind : str, optional
        Specifies the kind of text track, such as "subtitles," "captions," "descriptions," etc.

    label : str, optional
        Specifies a label or title for the track.

    src : str, optional
        Specifies the URL of the track file.

    srclang : str, optional
        Specifies the language of the text track.

    **kwargs : dict
        Additional keyword arguments that are passed to the parent class.

    Example Usage:
    --------------
    # Create a TrackElement for subtitles
    >>> track_elem = TrackElement(default=True, kind="subtitles", label="English Subtitles", src="subtitles.vtt", srclang="en")

    # Convert it to an HTML string
    >>> print(track_elem.to_string())
    <track default="true" kind="subtitles" label="English Subtitles" src="subtitles.vtt" srclang="en">

    """

    def __init__(
            self,
            default: bool = False,
            kind: str = None,
            label: str = None,
            src: str = None,
            srclang: str = None,
            **kwargs
    ) -> None:
        """
        Initializes a new TrackElement instance.

        Parameters:
        -----------
        default : bool, optional
            Specifies whether the track should be enabled by default (default is False).

        kind : str, optional
            Specifies the kind of text track, such as "subtitles," "captions," "descriptions," etc.

        label : str, optional
            Specifies a label or title for the track.

        src : str, optional
            Specifies the URL of the track file.

        srclang : str, optional
            Specifies the language of the text track.

        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes: dict[str, str | bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['default'] = default
        attributes['kind'] = kind
        attributes['label'] = label
        attributes['src'] = src
        attributes['srclang'] = srclang
        super().__init__("track", attributes=attributes, **kwargs)


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


class VariableElement(BaseHTMLElement):
    """
    VariableElement Class extends BaseHTMLElement to represent the HTML <var> element.

    HTML Use Cases:
    ---------------
    The HTML <var> element is used to indicate a variable or placeholder within text or content.
    It typically represents a variable, a mathematical expression, or a placeholder for user input.

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
    # Create a VariableElement
    >>> variable = VariableElement(content="x")

    # Convert it to an HTML string
    >>> print(variable.to_string())
    <var>x</var>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new VariableElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("var", **kwargs)


class VideoElement(BaseHTMLElement):
    """
    VideoElement Class extends BaseHTMLElement to represent the HTML <video> element.

    HTML Use Cases:
    ---------------
    The HTML <video> element is used to embed video content in a web page.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Parameters:
    -----------
    autoplay : bool, optional
        Specifies whether the video should start playing as soon as it is loaded. Default is False.

    controls : bool, optional
        Specifies whether video controls (e.g., play, pause, volume) should be displayed. Default is False.

    height : str, optional
        Specifies the height of the video player.

    loop : bool, optional
        Specifies whether the video should loop when it reaches the end. Default is False.

    muted : bool, optional
        Specifies whether the audio should be muted. Default is False.

    poster : str, optional
        Specifies an image to be displayed as the video's thumbnail before it is played.

    preload : str, optional
        Specifies how the video should be loaded. Can be 'auto', 'metadata', or 'none'. Default is None.

    src : str, optional
        Specifies the URL of the video file.

    width : str, optional
        Specifies the width of the video player.

    **kwargs : dict
        Additional keyword arguments that are passed to the parent class.

    Example Usage:
    --------------
    # Create a VideoElement
    >>> video = VideoElement(src="video.mp4", controls=True, width="640", height="360")

    # Convert it to an HTML string
    >>> print(video.to_string())
    <video src="video.mp4" controls width="640" height="360"></video>

    """

    def __init__(
        self,
        autoplay: bool = False,
        controls: bool = False,
        height: str = None,
        loop: bool = False,
        muted: bool = False,
        poster: str = None,
        preload: str = None,
        src: str = None,
        width: str = None,
        **kwargs
    ) -> None:
        """
        Initializes a new VideoElement instance.

        Parameters:
        -----------
        autoplay : bool, optional
            Specifies whether the video should start playing as soon as it is loaded. Default is False.

        controls : bool, optional
            Specifies whether video controls (e.g., play, pause, volume) should be displayed. Default is False.

        height : str, optional
            Specifies the height of the video player.

        loop : bool, optional
            Specifies whether the video should loop when it reaches the end. Default is False.

        muted : bool, optional
            Specifies whether the audio should be muted. Default is False.

        poster : str, optional
            Specifies an image to be displayed as the video's thumbnail before it is played.

        preload : str, optional
            Specifies how the video should be loaded. Can be 'auto', 'metadata', or 'none'. Default is None.

        src : str, optional
            Specifies the URL of the video file.

        width : str, optional
            Specifies the width of the video player.

        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        attributes = {
            'autoplay': autoplay,
            'controls': controls,
            'height': height,
            'loop': loop,
            'muted': muted,
            'poster': poster,
            'preload': preload,
            'src': src,
            'width': width
        }
        super().__init__("video", attributes=attributes, **kwargs)


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
