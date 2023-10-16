import os.path
from .general_base import GeneralBaseElement


def render(
        html_content: str | GeneralBaseElement | list[str | GeneralBaseElement] | tuple[str | GeneralBaseElement]
) -> str:
    if isinstance(html_content, (str, GeneralBaseElement)):
        html_content: list[str | GeneralBaseElement] = [html_content]
    return "".join(str(html_element) for html_element in html_content)


def save_to_file(html_str: str, file_path: any) -> None:
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_str)
