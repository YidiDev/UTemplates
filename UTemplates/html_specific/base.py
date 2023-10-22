import html
from ..general_base import GeneralBaseElement
from ..utils import convert_value


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
            custom_utemplates_conversion_functions: list = None,
            id_attribute: str = None,
            class_attribute: str | list[str] = None,
            style: str = None,
            title: str = None,
            lang: str = None,
            dir: str = None,
            tab_index: str | int = None,
            **kwargs
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
        :param attributes: Optional attributes to be added to the tag.
        :param content: Content to be placed within the tag.
        :param self_closing: If True, denotes a self-closing tag (e.g., <img />, <br />). Defaults to False.
        :param declaration: If True, denotes a declaration tag (e.g., <!DOCTYPE html>). Defaults to False.
        :param custom_utemplates_conversion_functions: List of custom conversion functions to transform content.
        :param id_attribute: The "id" attribute value for the HTML element.
        :param class_attribute: The "class" attribute value; can be a single string or list of strings for multiple classes.
        :param style: Inline CSS style attribute for the HTML element.
        :param title: Title attribute for the HTML element.
        :param lang: Language attribute for the HTML element.
        :param dir: Text direction attribute ("ltr" or "rtl") for the HTML element.
        :param tab_index: Tab index attribute for the HTML element; can be an integer or a string representation of an integer.
        :param kwargs: Additional attributes not explicitly listed. Attribute names with underscores will be replaced by hyphens.
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
        if self.self_closing:
            self.attributes["content"] = "".join(str(content_item) for content_item in self.content)
        self.declaration: bool = declaration
        if self.declaration:
            self.self_closing: bool = True
        self.custom_utemplates_conversion_functions: list = custom_utemplates_conversion_functions

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

        for key, value in kwargs.items():
            self.attributes[key.replace("_", "-")] = value

    def add_child(self, child: GeneralBaseElement) -> None:
        """
        Adds a child element to the content of the current HTML element.

        HTML Use Case:
            Useful for appending nested elements to the current element's content.

        Example:
            div_element = BaseHTMLElement("div", {"class": "container"})
            span_element = BaseHTMLElement("span", content="Hello World")
            div_element.add_child(span_element)

        :param child: The BaseHTMLElement instance to add as a child.
        """
        self.content.append(child)

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
                    if '"' in value:
                        attributes_str += f" {key}='{value}'"
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
        Generate the content string, ensuring it is converted and escaped.

        HTML Use Case:
            Used internally to insert the content between the opening
            and closing tags of the HTML element.

        Example:
            For a div element with content "Hello", returns 'Hello'

        :return: Content as a string.
        """
        def ensure_content_is_converted_and_escaped(content: any) -> str:
            if not isinstance(content, GeneralBaseElement):
                content: any = convert_value(
                    content, conversion_functions_list=self.custom_utemplates_conversion_functions
                )
            if isinstance(content, GeneralBaseElement):
                escaped_content: str = str(content)
            else:
                escaped_content: str = html.escape(str(content))
            return escaped_content
        if self.self_closing:
            return ""
        content_strs: list[str] = []
        for item in self.content:
            content_strs.append(ensure_content_is_converted_and_escaped(item))
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
