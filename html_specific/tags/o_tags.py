from html_specific.base import BaseHTMLElement


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
