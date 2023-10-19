from ..base import BaseHTMLElement


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
            height: str = "150",
            width: str = "300",
            **kwargs
    ) -> None:
        """
        Initializes a new CanvasElement instance.

        Parameters:
        -----------
        height: str
            Specifies the height of the canvas element. Default is "150".
        width: str
            Specifies the width of the canvas element. Default is "300".

        **kwargs: dict
            Optional keyword arguments inherited from the BaseHTMLElement parent class, such as 'content'.

        """
        super().__init__("canvas", height=height, width=width, **kwargs)


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
        super().__init__("col", span=span, **kwargs)


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
        super().__init__("colgroup", span=span, **kwargs)
