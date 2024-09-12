# markdown_to_html.py
# Dependencies: markdown
# Install with: pip install markdown

import markdown

def convert_markdown_to_html(markdown_text):
    html = markdown.markdown(markdown_text)
    return html

if __name__ == "__main__":
    md_text = input("Enter Markdown text: ")
    html_output = convert_markdown_to_html(md_text)
    print("Converted HTML:")
    print(html_output)
