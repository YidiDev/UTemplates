from ..base import BaseHTMLElement


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
        super().__init__(
            "iframe",
            allow=allow,
            allowfullscreen=allowfullscreen,
            allowpaymentrequest=allowpaymentrequest,
            height=height,
            loading=loading,
            name=name,
            referrerpolicy=referrerpolicy,
            sandbox=sandbox,
            src=src,
            srcdoc=srcdoc,
            width=width,
            **kwargs
        )


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
        super().__init__(
            "img",
            alt=alt,
            crossorigin=crossorigin,
            height=height,
            ismap=ismap,
            loading=loading,
            longdesc=longdesc,
            sizes=sizes,
            src=src,
            srcset=srcset,
            usermap=usermap,
            width=width,
            **kwargs
        )


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
        super().__init__(
            "input",
            accept=accept,
            alt=alt,
            autocomplete=autocomplete,
            autofocus=autofocus,
            checked=checked,
            dirname=dirname,
            disabled=disabled,
            form=form,
            formaction=formaction,
            formenctype=formenctype,
            formmethod=formmethod,
            formnovalidate=formnovalidate,
            formtarget=formtarget,
            height=height,
            list=list,
            max=max,
            maxlength=maxlength,
            min=min,
            minlength=minlength,
            multiple=multiple,
            name=name,
            pattern=pattern,
            placeholder=placeholder,
            readonly=readonly,
            required=required,
            size=size,
            src=src,
            step=step,
            type=type,
            value=value,
            width=width,
            self_closing=True,
            **kwargs
        )


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
        super().__init__("ins", cite=cite, datetime=datetime, **kwargs)
