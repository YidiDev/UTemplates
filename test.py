# Assuming you've already defined GeneralBaseElement and BaseHTMLElement above...
from html_specific.base import HTMLPage, BaseHTMLElement

# Define the HTMLPage class (either your version or the modified one provided)

# Testing the HTMLPage functionality:
page = HTMLPage(title="Test Page")

# Adding meta tag to head
meta_tag = BaseHTMLElement("meta", {"charset": "UTF-8"})
page.add_to_head(meta_tag)

# Adding a style tag to head
style_content = """
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
}
"""
style_tag = BaseHTMLElement("style", content=style_content)
page.add_to_head(style_tag)

# Adding content to body
header = BaseHTMLElement("h1", content="Welcome to the Test Page!")
paragraph = BaseHTMLElement("p", content="This is a sample paragraph.")
button = BaseHTMLElement("button", attributes={"type": "button", "class": "btn btn-primary"}, content="Click Me!")

page.add_to_body(header)
page.add_to_body(paragraph)
page.add_to_body(button)

# Printing the resultant page
print(page.to_string())
