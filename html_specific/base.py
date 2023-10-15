from general_base import GeneralBaseElement


class BaseHTMLElement(GeneralBaseElement):
    def __init__(
            self, tag_name: str, attributes: dict[str, any] = None, content: any = None, self_closing: bool = False
    ) -> None:
        self.tag_name: str = tag_name
        self.attributes: dict[str, any] = attributes if attributes is not None else {}
        if content is None:
            self.content: list[any] = []
        elif not isinstance(content, (str, bytes)) and hasattr(content, "__iter__"):
            self.content: list[any] = content
        else:
            self.content: list[any] = [content]
        self.self_closing: bool = self_closing

    @property
    def _attributes(self) -> str:
        attributes_str: str = ""
        for key, value in self.attributes.items():
            if value is not None:
                if isinstance(value, bool):
                    if value:
                        attributes_str += f" {key}"
                else:
                    attributes_str += f' {key}="{value}"'
        return attributes_str

    @property
    def _opening_tag(self) -> str:
        return f"<{self.tag_name}{self._attributes}>"

    @property
    def _content(self) -> str:
        if self.self_closing:
            return ""
        content_strs: list[str] = []
        for item in self.content:
            content_strs.append(str(item))
        return "".join(content_strs)

    @property
    def _closing_tag(self) -> str:
        if self.self_closing:
            return ""
        else:
            return f"</{self.tag_name}>"

    def to_string(self) -> str:
        return f"{self._opening_tag}{self._content}{self._closing_tag}"


class HTMLPage(GeneralBaseElement):
    def __init__(self, title: str = "Untitled") -> None:
        self.head_elements: list[BaseHTMLElement] = [BaseHTMLElement("title", content=title)]
        self.body_elements: list[BaseHTMLElement] = []

    def add_to_head(self, element: BaseHTMLElement) -> None:
        self.head_elements.append(element)

    def add_to_body(self, element: BaseHTMLElement) -> None:
        self.body_elements.append(element)

    @property
    def _html_level_elements(self) -> list[BaseHTMLElement]:
        return [
            BaseHTMLElement("head", content=self.head_elements),
            BaseHTMLElement("body", content=self.body_elements)
        ]

    @property
    def _page_level_elements(self) -> list[BaseHTMLElement]:
        return [
            BaseHTMLElement("!DOCTYPE", attributes={"html": True}, requires_closing_tag=False),
            BaseHTMLElement("html", content=self._html_level_elements),
        ]

    def to_string(self) -> str:
        page_str: str = ""
        for element in self._page_level_elements:
            page_str += str(element)
        return page_str
