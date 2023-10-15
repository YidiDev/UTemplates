from ..base import BaseHTMLElement


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
