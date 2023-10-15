from ..base import BaseHTMLElement


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
