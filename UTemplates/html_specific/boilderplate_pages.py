from .base import BaseHTMLElement
from .declarations import HTML5Declaration
from .tags import (TitleElement, HeadElement, BodyElement, HTMLElement)
from ..general_base import GeneralBaseElement


class HTML5Page(GeneralBaseElement):
    """
    Represents an HTML5 web page.

    HTML Use Cases:
        This class is used to construct an entire HTML5 document.
        It allows the user to add elements to the head and body of the HTML document.

    Examples:
        1. Creating an HTML5 page with title "My Page":
            my_page = HTML5Page(title="My Page")

        2. Adding an element to the head:
            meta_element = MetaElement(attributes={"charset": "UTF-8"})
            my_page.add_to_head(meta_element)

        3. Adding an element to the body:
            p_element = PElement(content="Hello, world!")
            my_page.add_to_body(p_element)

        4. Rendering the page:
            rendered = my_page.to_string()

    :param title: The title of the web page, default is "Untitled".
    """

    def __init__(self, title: str = "Untitled") -> None:
        """
        Initializes the HTML5Page instance.

        :param title: The title of the web page.
        """
        self.head_elements: list[BaseHTMLElement] = [TitleElement(content=title)]
        self.body_elements: list[BaseHTMLElement] = []

    def add_to_head(self, element: BaseHTMLElement) -> None:
        """
        Adds an element to the head section of the HTML page.

        :param element: The BaseHTMLElement instance to add to the head section.
        """
        self.head_elements.append(element)

    def add_to_body(self, element: BaseHTMLElement) -> None:
        """
        Adds an element to the body section of the HTML page.

        :param element: The BaseHTMLElement instance to add to the body section.
        """
        self.body_elements.append(element)

    @property
    def _html_level_elements(self) -> list[BaseHTMLElement]:
        """
        Combines head and body elements for the HTML document.

        :return: A list containing the head and body elements for the HTML document.
        """
        return [HeadElement(content=self.head_elements), BodyElement(content=self.body_elements)]

    @property
    def _page_level_elements(self) -> list[BaseHTMLElement]:
        """
        Wraps the entire HTML content within the HTML5 declaration and HTML tags.

        :return: A list containing the HTML5 declaration and HTML tags, enclosing the content.
        """
        return [HTML5Declaration(), HTMLElement(content=self._html_level_elements)]

    def to_string(self) -> str:
        """
        Generates the entire HTML5 page as a string.

        :return: The HTML5 page in string format.
        """
        page_str: str = ""
        for element in self._page_level_elements:
            page_str += str(element)
        return page_str
