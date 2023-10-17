import html
from ..general_base import GeneralBaseElement


class SafeHTMLElement(GeneralBaseElement):
    def __init__(self, content: str) -> None:
        """
        Initializes a new SafeHTMLElement instance.

        HTML Use Case:
            This class is meant to safely encapsulate HTML content
            that should not be escaped, such as pre-processed HTML strings.
            The content is marked as "safe" and will be rendered as is.

        Example:
            safe_content = SafeHTMLElement("<div class='safe'>This is safe</div>")

        :param content: Content to be wrapped within the tag, assumed to be safe HTML.
        """
        self.content: str = content

    def to_string(self) -> str:
        """
        Generate the HTML content as a string without any escaping.

        HTML Use Case:
            This is used to insert safe HTML content directly into
            the document. It is assumed that any content passed into
            this class is already safe and does not need to be escaped.

        Example:
            If content was "<div class='safe'>This is safe</div>",
            returns "<div class='safe'>This is safe</div>"

        :return: The safe HTML content as a string.
        """
        return str(self.content)


class BaseHTMLElement(GeneralBaseElement):
    def __init__(
            self,
            tag_name: str,
            attributes: dict[str, any] = None,
            content: any = None,
            self_closing: bool = False,
            declaration: bool = False,
            id_attribute: str = None,
            class_attribute: str | list[str] = None,
            style: str = None,
            title: str = None,
            lang: str = None,
            dir: str = None,
            tab_index: str | int = None
    ) -> None:
        """
        Initializes a new BaseHTMLElement instance.

        HTML Use Case:
            This class is meant to represent a generic HTML element.
            The instance will contain the name of the HTML tag, its attributes,
            and its content.

        Example:
            div_element = BaseHTMLElement("div", {"class": "container"}, "Hello World")

        :param tag_name: Name of the HTML tag (e.g., "div", "span", "a").
        :param attributes: Dictionary of attributes to be added to the tag.
        :param content: Content to be wrapped within the tag.
        :param self_closing: Boolean indicating if the tag is self-closing (e.g., <img />, <br />).
        :param declaration: Boolean indicating if the tag is a declaration (e.g., <!DOCTYPE html>).
        :param id_attribute: Value of the "id" attribute for the HTML element.
        :param class_attribute: Value of the "class" attribute, can be a string or a list of strings.
        :param style: Inline CSS style for the HTML element.
        :param title: Title attribute for the HTML element.
        :param lang: Language attribute for the HTML element.
        :param dir: Text direction attribute for the HTML element.
        :param tab_index: Tabindex attribute for the HTML element.
        """
        self.tag_name: str = tag_name
        self.attributes: dict[str, any] = attributes if attributes is not None else {}
        if content is None:
            self.content: list[any] = []
        elif not isinstance(content, (str, bytes)) and hasattr(content, "__iter__"):
            # noinspection PyTypeChecker
            self.content: list[any] = content
        else:
            self.content: list[any] = [content]
        self.self_closing: bool = self_closing
        self.declaration: bool = declaration
        if self.declaration:
            self.self_closing: bool = True

        self.id_attribute: str | None = id_attribute if id_attribute is not None else self.attributes.get("id")
        self.attributes["id"] = self.id_attribute
        self.class_attribute: str | list[str] | None = class_attribute if class_attribute is not None \
            else self.attributes.get("class")
        if isinstance(self.class_attribute, list):
            self.class_attribute: str = " ".join(self.class_attribute)
        self.attributes["class"] = self.class_attribute
        self.style: str | None = style if style is not None else self.attributes.get("style")
        self.attributes["style"] = self.style
        self.title: str | None = title if title is not None else self.attributes.get("title")
        self.attributes["title"] = self.title
        self.lang: str | None = lang if lang is not None else self.attributes.get("lang")
        self.attributes["lang"] = self.lang
        self.dir: str | None = dir if dir is not None else self.attributes.get("dir")
        self.attributes["dir"] = self.dir
        self.tab_index: str | int | None = tab_index if tab_index is not None else self.attributes.get("tabindex")
        if isinstance(self.tab_index, int):
            self.tab_index: str = str(self.tab_index)
        self.attributes["tabindex"] = self.tab_index

    @property
    def _attributes(self) -> str:
        """
        Generate a string that represents all the HTML attributes.

        HTML Use Case:
            This is used internally to generate the string that will
            be inserted into the opening tag for the HTML element.

        Example:
            Given {"class": "test", "id": "elem1"}, returns ' class="test" id="elem1"'

        :return: String representing the attributes.
        """
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
        """
        Generate the opening tag string.

        HTML Use Case:
            Used to create the opening tag for the HTML element.
            Adds attributes if present.

        Example:
            For a div element with class "test", returns '<div class="test">'

        :return: Opening tag as a string.
        """
        if self.self_closing and not self.declaration:
            return f"<{self.tag_name}{self._attributes}/>"
        else:
            return f"<{self.tag_name}{self._attributes}>"

    @property
    def _content(self) -> str:
        """
        Generate the content string, ensuring it is escaped.

        HTML Use Case:
            Used internally to insert the content between the opening
            and closing tags of the HTML element.

        Example:
            For a div element with content "Hello", returns 'Hello'

        :return: Content as a string.
        """
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
        """
        Generate the closing tag string.

        HTML Use Case:
            Used to create the closing tag for the HTML element.

        Example:
            For a div element, returns '</div>'

        :return: Closing tag as a string.
        """
        if self.self_closing:
            return ""
        else:
            return f"</{self.tag_name}>"

    def to_string(self) -> str:
        """
        Generate the full HTML element as a string.

        HTML Use Case:
            This will generate the full HTML tag as a string,
            including the opening tag, attributes, content, and closing tag.

        Example:
            For a div element with class "test" and content "Hello",
            returns '<div class="test">Hello</div>'

        :return: Full HTML tag as a string.
        """
        return f"{self._opening_tag}{self._content}{self._closing_tag}"
