from ..base import BaseHTMLElement


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
        super().__init__("td", colspan=colspan, headers=headers, rowspan=rowspan, **kwargs)


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
        super().__init__(
            "textarea",
            autofocus=autofocus,
            cols=cols,
            dirname=dirname,
            disabled=disabled,
            form=form,
            maxlength=maxlength,
            name=name,
            placeholder=placeholder,
            readonly=readonly,
            required=required,
            rows=rows,
            wrap=wrap,
            **kwargs
        )


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
        super().__init__("th", abbr=abbr, colspan=colspan, headers=headers, rowspan=rowspan, scope=scope, **kwargs)


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
        super().__init__("time", datetime=datetime, **kwargs)


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
        super().__init__("track", default=default, kind=kind, label=label, src=src, srclang=srclang, **kwargs)
