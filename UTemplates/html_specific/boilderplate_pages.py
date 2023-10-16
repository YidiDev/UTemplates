from .base import BaseHTMLElement
from .declarations import HTML5Declaration
from .tags import (TitleElement, HeadElement, BodyElement, HTMLElement)
from ..general_base import GeneralBaseElement


class HTML5Page(GeneralBaseElement):
    def __init__(self, title: str = "Untitled") -> None:
        self.head_elements: list[BaseHTMLElement] = [TitleElement(content=title)]
        self.body_elements: list[BaseHTMLElement] = []

    def add_to_head(self, element: BaseHTMLElement) -> None:
        self.head_elements.append(element)

    def add_to_body(self, element: BaseHTMLElement) -> None:
        self.body_elements.append(element)

    @property
    def _html_level_elements(self) -> list[BaseHTMLElement]:
        return [HeadElement(content=self.head_elements), BodyElement(content=self.body_elements)]

    @property
    def _page_level_elements(self) -> list[BaseHTMLElement]:
        return [HTML5Declaration(), HTMLElement(content=self._html_level_elements)]

    def to_string(self) -> str:
        page_str: str = ""
        for element in self._page_level_elements:
            page_str += str(element)
        return page_str
