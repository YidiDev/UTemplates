import html
from ..general_base import GeneralBaseElement


class SafeHTMLElement(GeneralBaseElement):
    def __init__(self, content: str) -> None:
        self.content: str = content

    def to_string(self) -> str:
        return str(self.content)


class BaseHTMLElement(GeneralBaseElement):
    def __init__(
            self,
            tag_name: str,
            attributes: dict[str, any] = None,
            content: any = None,
            self_closing: bool = False,
            declaration: bool = False
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
        self.declaration: bool = declaration
        if self.declaration:
            self.self_closing: bool = True

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
        if self.self_closing and not self.declaration:
            return f"<{self.tag_name}{self._attributes}/>"
        else:
            return f"<{self.tag_name}{self._attributes}>"

    @property
    def _content(self) -> str:
        def ensure_content_is_escaped(content: str | GeneralBaseElement) -> str:
            if isinstance(content, GeneralBaseElement):
                escaped_content: str = str(content)
            else:
                escaped_content: str = html.escape(str(content))
            return escaped_content
        if self.self_closing:
            return ""
        content_strs: list[str] = []
        for item in self.content:
            content_strs.append(ensure_content_is_escaped(item))
        return "".join(content_strs)

    @property
    def _closing_tag(self) -> str:
        if self.self_closing:
            return ""
        else:
            return f"</{self.tag_name}>"

    def to_string(self) -> str:
        return f"{self._opening_tag}{self._content}{self._closing_tag}"
