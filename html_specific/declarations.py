from tags import DoctypeElement


class HTML5Declaration(DoctypeElement):
    def __init__(self, **kwargs) -> None:
        super().__init__("html", **kwargs)


class HTML4_01StrictDeclaration(DoctypeElement):
    def __init__(self, **kwargs) -> None:
        super().__init__(
            'HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"', **kwargs
        )


class HTML4_01TransitionalDeclaration(DoctypeElement):
    def __init__(self, **kwaadrgs) -> None:
        super().__init__(
            'HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"',
            **kwargs
        )


class XHTML1_0StrictDeclaration(DoctypeElement):
    def __init__(self, **kwargs) -> None:
        super().__init__(
            'html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" '
            '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"',
            **kwargs
        )


class XHTML1_0TransitionalDeclaration(DoctypeElement):
    def __init__(self, **kwargs) -> None:
        super().__init__(
            'html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" '
            '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"',
            **kwargs
        )


class XHTML1_1Declaration(DoctypeElement):
    def __init__(self, **kwargs) -> None:
        super().__init__(
            'html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"', **kwargs
        )


class HTML3_2Declaration(DoctypeElement):
    def __init__(self, **kwargs) -> None:
        super().__init__(
            'HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"', **kwargs
        )
