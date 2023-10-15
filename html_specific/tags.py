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
    def __init__(self, **kwargs) -> None:
        super().__init__("b", **kwargs)


class BaseElement(BaseHTMLElement):
    def __init__(self, href: str = None, target: str = None, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["href"] = href
        attributes["target"] = target
        super().__init__("base", attributes=attributes, **kwargs)


class BiDirectionalIsolationElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("bdi", **kwargs)


class BiDirectionalOverrideElement(BaseHTMLElement):
    def __init__(self, dir: str, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['dir'] = dir
        super().__init__("bdo", attributes=attributes, **kwargs)


class BlockquoteElement(BaseHTMLElement):
    def __init__(self, cite: str = None, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["cite"] = cite
        super().__init__("blockquote", attributes=attributes, **kwargs)


class BodyElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("body", **kwargs)


class BreakElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("br", self_closing=True, **kwargs)


class ButtonElement(BaseHTMLElement):
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
        attributes["type_attribute"] = type_attribute
        attributes["value"] = value
        super().__init__("button", attributes=attributes, **kwargs)


class CanvasElement(BaseHTMLElement):
    def __init__(self, id: str = None, height: str = "150", width: str = "300", **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["id"] = id
        attributes["height"] = height
        attributes["width"] = width
        super().__init__("canvas", attributes=attributes, **kwargs)


class CaptionElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("caption", **kwargs)


class CiteElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("cite", **kwargs)


class CodeElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("code", **kwargs)


class ColumnElement(BaseHTMLElement):
    def __init__(self, span: str = None, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["span"] = span
        super().__init__("col", attributes=attributes, **kwargs)


class ColumnGroupElement(BaseHTMLElement):
    def __init__(self, span: str = None, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["span"] = span
        super().__init__("colgroup", attributes=attributes, **kwargs)


class DataElement(BaseHTMLElement):
    def __init__(self, value: str = None, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["value"] = value
        super().__init__("data", attributes=attributes, **kwargs)


class DataListElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("datalist", **kwargs)


class DefinitionDescriptionElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("dd", **kwargs)


class DeletedElement(BaseHTMLElement):
    def __init__(self, cite: str = None, datetime: str = None, **kwargs) -> None:
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
    def __init__(self, open: bool = False, **kwargs) -> None:
        attributes: dict[str, bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        if open is not None:
            attributes["open"] = open
        super().__init__("details", attributes=attributes, **kwargs)


class DefinitionElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("dfn", **kwargs)


class DialogElement(BaseHTMLElement):
    def __init__(self, open: bool = False, **kwargs) -> None:
        attributes: dict[str, bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        if open is not None:
            attributes["open"] = open
        super().__init__("dialog", attributes=attributes, **kwargs)


class DivElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("div", **kwargs)


class DescriptionListElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("dl", **kwargs)


class DescriptionTermElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("dt", **kwargs)


class EmphasizedElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("em", **kwargs)


class EmbedElement(BaseHTMLElement):
    def __init__(
            self, height: str = None, src: str = None, type_attribute: str = None, width: str = None, **kwargs
    ) -> None:
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
    def __init__(self, disabled: bool = False, form: str = None, name: str = None, **kwargs) -> None:
        attributes: dict[str, str | bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["disabled"] = disabled
        attributes["form"] = form
        attributes["name"] = name
        super().__init__("a", attributes=attributes, **kwargs)


class FigureCaptionElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("figcaption", **kwargs)


class FigureElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("figure", **kwargs)


class FooterElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("footer", **kwargs)


class FormElement(BaseHTMLElement):
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
    def __init__(self, level: int, **kwargs) -> None:
        if level > 6 or level < 1:
            print("WARNING: valid heading elements should be between 1 and 6")
        super().__init__(f"h{level}", **kwargs)


class HeadElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("head", **kwargs)


class HeaderElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("header", **kwargs)


class HorizontalRuleElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("hr", self_closing=True, **kwargs)


class HTMLElement(BaseHTMLElement):
    def __init__(self, xmlns: str = None, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes["xmlns"] = xmlns
        super().__init__("html", attributes=attributes, **kwargs)


class ItalicizedElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("i", **kwargs)


class InlineFrameElement(BaseHTMLElement):
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
    def __init__(self, cite: str = None, datetime: str = None, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['cite'] = cite
        attributes['datetime'] = datetime
        super().__init__("ins", attributes=attributes, **kwargs)


class KeyboardInputElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("kbd", **kwargs)


class LabelElement(BaseHTMLElement):
    def __init__(self, for_attribute: str = None, form: str = None, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['for'] = for_attribute
        attributes['form'] = form
        super().__init__("label", attributes=attributes, **kwargs)


class LegendElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("legend", **kwargs)


class ListItemElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("li", **kwargs)


class LinkElement(BaseHTMLElement):
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
    def __init__(self, **kwargs) -> None:
        super().__init__("main", **kwargs)


class MapElement(BaseHTMLElement):
    def __init__(self, name: str, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['name'] = name
        super().__init__("map", attributes=attributes, **kwargs)


class MarkedElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("mark", **kwargs)


class MetaElement(BaseHTMLElement):
    def __init__(
            self, charset: str = None, content: str = None, http_equiv: str = None, name: str = None, **kwargs
    ) -> None:
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
    def __init__(self, **kwargs) -> None:
        super().__init__("nav", **kwargs)


class NoScriptElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("noscript", **kwargs)


class ObjectElement(BaseHTMLElement):
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
    def __init__(self, reversed: bool = False, start: str = None, type: str = None, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['reversed'] = reversed
        attributes['start'] = start
        attributes['type'] = type
        super().__init__("ol", attributes=attributes, **kwargs)


class OptionGroupElement(BaseHTMLElement):
    def __init__(self, disabled: bool = False, label: str = None, **kwargs) -> None:
        attributes: dict[str, str | bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['disabled'] = disabled
        attributes['label'] = label
        super().__init__("optgroup", attributes=attributes, **kwargs)


class OptionElement(BaseHTMLElement):
    def __init__(
            self, disabled: bool = False, label: str = None, selected: bool = False, value: str = None, **kwargs
    ) -> None:
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
    def __init__(self, for_attribute: str = None, form: str = None, name: str = None, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['for'] = for_attribute
        attributes['form'] = form
        attributes['name'] = name
        super().__init__("output", attributes=attributes, **kwargs)


class ParagraphElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("p", **kwargs)


class ParameterElement(BaseHTMLElement):
    def __init__(self, name: str = None, value: str = None, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['name'] = name
        attributes['value'] = value
        super().__init__("param", attributes=attributes, self_closing=True, **kwargs)


class PictureElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("picture", **kwargs)


class PreformattedElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("pre", **kwargs)


class ProgressElement(BaseHTMLElement):
    def __init__(self, max: str = "1", value: str = None, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['max'] = max
        attributes['value'] = value
        super().__init__("progress", attributes=attributes, **kwargs)


class ShortQuotationElement(BaseHTMLElement):
    def __init__(self, cite: str = None, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['cite'] = cite
        super().__init__("q", attributes=attributes, **kwargs)


class RubyParenthesesElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("rp", **kwargs)


class RubyTextElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("rt", **kwargs)


class RubyElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("ruby", **kwargs)


class StruckThroughElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("s", **kwargs)


class SampleElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("samp", **kwargs)


class ScriptElement(BaseHTMLElement):
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
    def __init__(self, **kwargs) -> None:
        super().__init__("section", **kwargs)


class SelectElement(BaseHTMLElement):
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
    def __init__(self, **kwargs) -> None:
        super().__init__("small", **kwargs)


class SourceElement(BaseHTMLElement):
    def __init__(
            self, media: str = None, sizes: str = None, src: str = None, srcset: str = None, type: str = None, **kwargs
    ) -> None:
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
    def __init__(self, **kwargs) -> None:
        super().__init__("span", **kwargs)


class StrongElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("strong", **kwargs)


class StyleElement(BaseHTMLElement):
    def __init__(self, media: str = None, type: str = None, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['media'] = media
        attributes['type'] = type
        super().__init__("style", attributes=attributes, **kwargs)


class SubscriptElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("sub", **kwargs)


class SummaryElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("summary", **kwargs)


class SuperscriptElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("sup", **kwargs)


class SVGElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("svg", **kwargs)


class TableElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("table", **kwargs)


class TableBodyElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("tbody", **kwargs)


class TableDataElement(BaseHTMLElement):
    def __init__(self, colspan: str = None, headers: str = None, rowspan: str = None, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['colspan'] = colspan
        attributes['headers'] = headers
        attributes['rowspan'] = rowspan
        super().__init__("td", attributes=attributes, **kwargs)


class TemplateElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("template", **kwargs)


class TextAreaElement(BaseHTMLElement):
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
    def __init__(self, **kwargs) -> None:
        super().__init__("tfoot", **kwargs)


class TableHeaderCellElement(BaseHTMLElement):
    def __init__(
            self,
            abbr: str = None,
            colspan: str = None,
            headers: str = None,
            rowspan: str = None,
            scope: str = None,
            **kwargs
    ) -> None:
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
    def __init__(self, **kwargs) -> None:
        super().__init__("thead", **kwargs)


class TimeElement(BaseHTMLElement):
    def __init__(self, datetime: str = None, **kwargs) -> None:
        attributes: dict[str, str] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['datetime'] = datetime
        super().__init__("time", attributes=attributes, **kwargs)


class TitleElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("title", **kwargs)


class TableRowElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("tr", **kwargs)


class TrackElement(BaseHTMLElement):
    def __init__(
            self,
            default: bool = False,
            kind: str = None,
            label: str = None,
            src: str = None,
            srclang: str = None,
            **kwargs
    ) -> None:
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
    def __init__(self, **kwargs) -> None:
        super().__init__("u", **kwargs)


class UnorderedListElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("ul", **kwargs)


class VariableElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("var", **kwargs)


class VideoElement(BaseHTMLElement):
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
        attributes: dict[str, str | bool] = {}
        if kwargs.get("attributes"):
            attributes.update(kwargs["attributes"])
            del kwargs["attributes"]
        attributes['autoplay'] = autoplay
        attributes['controls'] = controls
        attributes['height'] = height
        attributes['loop'] = loop
        attributes['muted'] = muted
        attributes['poster'] = poster
        attributes['preload'] = preload
        attributes['src'] = src
        attributes['width'] = width
        super().__init__("video", attributes=attributes, **kwargs)


class WordBreakOpportunityElement(BaseHTMLElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("wbr", self_closing=True, **kwargs)
