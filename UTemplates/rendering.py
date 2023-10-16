import os.path
from .general_base import GeneralBaseElement


def save_to_file(html_content: str | GeneralBaseElement | list[str | GeneralBaseElement], file_path: any) -> None:
    if isinstance(html_content, (str, GeneralBaseElement)):
        html_content: list[str | GeneralBaseElement] = [html_content]

    html_str: str = "".join(str(html_element) for html_element in html_content)

    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_str)
