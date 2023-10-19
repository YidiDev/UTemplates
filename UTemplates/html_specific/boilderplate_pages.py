from .base import BaseHTMLElement
from .declarations import HTML5Declaration
from .tags import (TitleElement, HeadElement, BodyElement, HTMLElement, DoctypeElement)
from ..general_base import GeneralBaseElement


class HTMLPage(GeneralBaseElement):
    """
    Represents an HTML web page.

    HTML Use Cases:
        This class constructs an entire HTML document.
        Users can add elements to the head and body sections of the HTML document.

    Examples:
        1. Creating an HTML page with title "My Page":
            my_page = HTMLPage(title="My Page")

        2. Adding an element to the head:
            meta_element = MetaElement(attributes={"charset": "UTF-8"})
            my_page.add_to_head(meta_element)

        3. Adding an element to the body:
            p_element = PElement(content="Hello, world!")
            my_page.add_to_body(p_element)

        4. Rendering the page:
            rendered = my_page.to_string()

    Attributes:
        title (str): The title of the web page. Defaults to "Untitled".
    """

    def __init__(self, title: str = "Untitled", declaration_element: DoctypeElement = HTML5Declaration()) -> None:
        """
        Initializes the HTMLPage instance.

        Args:
            title (str, optional): The title of the web page. Defaults to "Untitled".
            declaration_element (DoctypeElement, optional): The type of HTML document declaration. Defaults to HTML5Declaration.
        """
        self.declaration_element: DoctypeElement = declaration_element
        self._head_element: HeadElement = HeadElement(content=TitleElement(content=title))
        self._body_element: BodyElement = BodyElement()

    def add_to_head(self, element: BaseHTMLElement) -> None:
        """
        Appends an element to the head section of the HTML page.

        Args:
            element (BaseHTMLElement): Element to add to the head section.
        """
        self._head_element.add_child(element)

    def add_to_body(self, element: BaseHTMLElement) -> None:
        """
        Appends an element to the body section of the HTML page.

        Args:
            element (BaseHTMLElement): Element to add to the body section.
        """
        self._body_element.add_child(element)

    @property
    def _html_level_elements(self) -> list[BaseHTMLElement]:
        """
        Combines head and body elements for rendering in the HTML document.

        Returns:
            list[BaseHTMLElement]: A list containing the head and body elements.
        """
        return [self._head_element, self._body_element]

    @property
    def _page_level_elements(self) -> list[BaseHTMLElement]:
        """
        Wraps the entire content within the HTML declaration and HTML tags.

        Returns:
            list[BaseHTMLElement]: A list containing the HTML declaration and tags enclosing the content.
        """
        return [self.declaration_element, HTMLElement(content=self._html_level_elements)]

    def to_string(self) -> str:
        """
        Renders the entire HTML page as a string.

        Returns:
            str: The HTML page in string format.
        """
        page_str: str = ""
        for element in self._page_level_elements:
            page_str += str(element)
        return page_str


class HTML5Page(HTMLPage):
    """
    Represents an HTML5 web page, a subclass of HTMLPage.

    It's a convenience class that defaults to using the HTML5 declaration.

    Examples:
        Creating an HTML5 page with title "My Page":
            my_page = HTML5Page(title="My Page")

    """
    def __init__(self, **kwargs) -> None:
        """
        Initializes the HTML5Page instance, setting the HTML5 declaration as default.

        Args:
            **kwargs: Arguments to be passed to the base HTMLPage class.
        """
        super().__init__(declaration_element=HTML5Declaration(), **kwargs)
