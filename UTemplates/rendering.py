import os.path
from .general_base import (GeneralBaseElement, GroupedBaseElement)


def render(
        html_content: str | GeneralBaseElement | list[str | GeneralBaseElement] | tuple[str | GeneralBaseElement]
) -> str:
    """
    Render HTML content as a string.

    Use Cases:
        1. For converting a single GeneralBaseElement to its string representation.
        2. For joining multiple GeneralBaseElement instances or plain strings into a single HTML string.

    Examples:
        1. Single Element:
            div = BaseHTMLElement("div", content="Hello, world!")
            rendered = render(div)

        2. Multiple Elements:
            div1 = BaseHTMLElement("div", content="Hello")
            div2 = BaseHTMLElement("div", content="world!")
            rendered = render([div1, div2])

        3. Mixed Content:
            rendered = render(["Some text", BaseHTMLElement("br"), "More text"])

    :param html_content: The HTML content to render, can be a string, GeneralBaseElement,
                         list of strings and/or GeneralBaseElements, or tuple of strings
                         and/or GeneralBaseElements.

    :return: The rendered HTML content as a single string.
    """
    if isinstance(html_content, (str, GeneralBaseElement)):
        html_content: list[str | GeneralBaseElement] = [html_content]
    return str(GroupedBaseElement(elements=html_content))


def save_to_file(html_str: str, file_path: any) -> None:
    """
    Save HTML content to a file.

    Use Cases:
        1. Saving the rendered HTML content to a file for later use or to serve as a static webpage.
        2. Outputting the HTML content to a specific file path, creating directories as needed.

    Examples:
        1. Basic Usage:
            save_to_file('<html><body>Hello, world!</body></html>', './path/to/output.html')

        2. With Rendering:
            div = BaseHTMLElement("div", content="Hello, world!")
            rendered = render(div)
            save_to_file(rendered, './path/to/output.html')

    :param html_str: The HTML content to save, as a string.
    :param file_path: The file path where the HTML content should be saved.
                      Directories will be created if they do not exist.

    :return: None
    """
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_str)
