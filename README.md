# UTemplates - Python Templating Engine

UTemplates is a Python templating engine focused on HTML but with the potential to be extended to other languages. It facilitates the creation, manipulation, and rendering of HTML elements programmatically using Python classes and methods.

## Table of Contents
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Creating Elements](#creating-elements)
  - [Rendering HTML](#rendering-html)
  - [Utilities](#utilities)
  - [Integrations](#integrations)
- [License](#license)

## Installation

1. Clone the repository or download the source code.

```bash
pip install utemplates
```

## Getting Started

Before you start using UTemplates, ensure you have a Python environment set up. UTemplates supports Python 3.7 and newer.

## Usage

### Configuration

To customize the behavior of UTemplates, you can modify or provide a `utemplates_config.json` configuration file. This file allows you to define conversion functions that will be applied to values before rendering them. The path to the configuration file can be set through an environment variable `UTEMPLATES_CONFIG_PATH`.

#### Config Format

The configuration file is a JSON file with the following structure:

```json
{
  "conversions": [
    "module1.submodule.function1",
    "module2.submodule.function2"
  ]
}
```

- Each string in the "conversions" list is a dot-path to a conversion function that should be imported and applied during rendering.

### Creating Elements

UTemplates provides classes to structure HTML content. These can be generic or specific HTML elements:

- **GeneralBaseElement**: Abstract base class for all HTML elements.
- **GroupedBaseElement**: Class for grouping multiple elements.
- **BaseHTMLElement**: Class for creating standard HTML elements.
- **SafeHTMLElement**: Class for wrapping pre-processed HTML strings that should not be escaped.

You can create instances of these classes by calling their constructors and passing the appropriate arguments.

#### Example

```python
from utemplates.html_specific.base import BaseHTMLElement

div_element = BaseHTMLElement("div", {"class": "container"}, "Hello World")
```

This example creates a `<div>` element with the class "container" and containing the text "Hello World".

### Rendering HTML

To render HTML content, use the provided `render` method from the `rendering` module. It takes a string, a list of strings or elements, or a single element and generates an HTML string.

#### Example

```python
from utemplates.rendering import render

# For a single element
rendered_html = render(div_element())

# For multiple elements
rendered_html = render([div_element(), another_element()])

# You can also save the rendered HTML to a file
from utemplates.rendering import save_to_file
save_to_file(rendered_html, 'output.html')
```

### Utilities

The `utils.py` module includes utility functions:

- **convert_value**: Applies configured conversion functions to a given value.

### Integrations

UTemplates offers integration support for the Django framework to render responses directly:

#### Django Integration

```python
from utemplates.integrations.django_integrations import render_to_response

def my_view(request):
    html_content = create_some_html_content()
    return render_to_response(html_content)
```

## License

UTemplates is open-sourced under the MIT license.
