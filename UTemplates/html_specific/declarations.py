from .tags import DoctypeElement


class HTML5Declaration(DoctypeElement):
    """
    Represents an HTML5 declaration.

    HTML Use Cases:
        This is specifically for the HTML5 doctype declaration,
        usually appearing at the top of an HTML document to specify the document type.

    Examples:
        1. Creating an HTML5 Declaration:
            html5_declaration = HTML5Declaration()
            rendered = render(html5_declaration)

    :param kwargs: Any additional keyword arguments to pass to the parent DoctypeElement class.
    """
    def __init__(self, **kwargs) -> None:
        """
        Initializes the HTML5Declaration instance.

        :param kwargs: Any additional keyword arguments to pass to the parent DoctypeElement class.
        """
        super().__init__("html", **kwargs)


class HTML4_01StrictDeclaration(DoctypeElement):
    """
    Represents an HTML 4.01 Strict doctype declaration.

    HTML Use Cases:
        This is specifically for the HTML 4.01 Strict doctype declaration,
        which should appear at the top of an HTML document to specify the document type.

    Examples:
        1. Creating an HTML 4.01 Strict Declaration:
            html4_strict_declaration = HTML4_01StrictDeclaration()
            rendered = render(html4_strict_declaration)

    :param kwargs: Any additional keyword arguments to pass to the parent DoctypeElement class.
    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes the HTML4_01StrictDeclaration instance.

        :param kwargs: Any additional keyword arguments to pass to the parent DoctypeElement class.
        """
        super().__init__(
            'HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"', **kwargs
        )


class HTML4_01TransitionalDeclaration(DoctypeElement):
    """
    Represents an HTML 4.01 Transitional doctype declaration.

    HTML Use Cases:
        This class is specifically for the HTML 4.01 Transitional doctype declaration.
        It should appear at the top of an HTML document to specify the document type as HTML 4.01 Transitional.

    Examples:
        1. Creating an HTML 4.01 Transitional Declaration:
            html4_transitional_declaration = HTML4_01TransitionalDeclaration()
            rendered = render(html4_transitional_declaration)

    :param kwargs: Any additional keyword arguments to pass to the parent DoctypeElement class.
    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes the HTML4_01TransitionalDeclaration instance.

        :param kwargs: Any additional keyword arguments to pass to the parent DoctypeElement class.
        """
        super().__init__(
            'HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"',
            **kwargs
        )


class XHTML1_0StrictDeclaration(DoctypeElement):
    """
    Represents an XHTML 1.0 Strict doctype declaration.

    HTML Use Cases:
        This class is specifically for the XHTML 1.0 Strict doctype declaration.
        It should appear at the top of an XHTML document to specify the document type as XHTML 1.0 Strict.

    Examples:
        1. Creating an XHTML 1.0 Strict Declaration:
            xhtml1_strict_declaration = XHTML1_0StrictDeclaration()
            rendered = render(xhtml1_strict_declaration)

    :param kwargs: Any additional keyword arguments to pass to the parent DoctypeElement class.
    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes the XHTML1_0StrictDeclaration instance.

        :param kwargs: Any additional keyword arguments to pass to the parent DoctypeElement class.
        """
        super().__init__(
            'html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" '
            '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"',
            **kwargs
        )


class XHTML1_0TransitionalDeclaration(DoctypeElement):
    """
    Represents an XHTML 1.0 Transitional doctype declaration.

    HTML Use Cases:
        This class is specifically for the XHTML 1.0 Transitional doctype declaration.
        It should appear at the top of an XHTML document to specify the document type as XHTML 1.0 Transitional.

    Examples:
        1. Creating an XHTML 1.0 Transitional Declaration:
            xhtml1_transitional_declaration = XHTML1_0TransitionalDeclaration()
            rendered = render(xhtml1_transitional_declaration)

    :param kwargs: Any additional keyword arguments to pass to the parent DoctypeElement class.
    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes the XHTML1_0TransitionalDeclaration instance.

        :param kwargs: Any additional keyword arguments to pass to the parent DoctypeElement class.
        """
        super().__init__(
            'html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" '
            '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"',
            **kwargs
        )


class XHTML1_1Declaration(DoctypeElement):
    """
    Represents an XHTML 1.1 doctype declaration.

    HTML Use Cases:
        This class is specifically for the XHTML 1.1 doctype declaration.
        It should appear at the top of an XHTML document to specify the document type as XHTML 1.1.

    Examples:
        1. Creating an XHTML 1.1 Declaration:
            xhtml1_1_declaration = XHTML1_1Declaration()
            rendered = render(xhtml1_1_declaration)

    :param kwargs: Any additional keyword arguments to pass to the parent DoctypeElement class.
    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes the XHTML1_1Declaration instance.

        :param kwargs: Any additional keyword arguments to pass to the parent DoctypeElement class.
        """
        super().__init__(
            'html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"',
            **kwargs
        )


class HTML3_2Declaration(DoctypeElement):
    """
    Represents an HTML 3.2 doctype declaration.

    HTML Use Cases:
        This class is specifically for the HTML 3.2 doctype declaration.
        It should appear at the top of an HTML document to specify the document type as HTML 3.2.

    Examples:
        1. Creating an HTML 3.2 Declaration:
            html3_2_declaration = HTML3_2Declaration()
            rendered = render(html3_2_declaration)

    :param kwargs: Any additional keyword arguments to pass to the parent DoctypeElement class.
    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes the HTML3_2Declaration instance.

        :param kwargs: Any additional keyword arguments to pass to the parent DoctypeElement class.
        """
        super().__init__(
            'HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"',
            **kwargs
        )
