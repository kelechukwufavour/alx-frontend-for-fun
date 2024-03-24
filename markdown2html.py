#!/usr/bin/python3
"""Markdown to HTML converter."""

import sys
import re

def convert_headings(md_content):
    """Convert Markdown headings to HTML."""
    return re.sub(r'^#{1,6}\s(.*)', r'<h\1>\2</h\1>', md_content, flags=re.M)

def convert_unordered_listing(md_content):
    """Convert Markdown unordered listing to HTML."""
    return re.sub(r'^-\s(.*)', r'<ul>\n<li>\1</li>\n</ul>', md_content, flags=re.M)

def convert_ordered_listing(md_content):
    """Convert Markdown ordered listing to HTML."""
    return re.sub(r'^\*\s(.*)', r'<ol>\n<li>\1</li>\n</ol>', md_content, flags=re.M)

def convert_paragraphs(md_content):
    """Convert Markdown paragraphs to HTML."""
    return re.sub(r'(?<!\n)\n(?!\n)', r'<br/>\n', md_content)

def convert_bold_and_emphasis(md_content):
    """Convert Markdown bold and emphasis to HTML."""
    md_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', md_content)
    md_content = re.sub(r'__(.*?)__', r'<em>\1</em>', md_content)
    return md_content

def convert_special_syntax(md_content):
    """Convert Markdown special syntax to HTML."""
    md_content = re.sub(r'\[\[(.*?)\]\]', lambda match: f'{match.group(1)}<br/>{hashlib.md5(match.group(1).encode()).hexdigest()}', md_content)
    md_content = re.sub(r'\(\((.*?)\)\)', lambda match: match.group(1).replace('c', '').replace('C', ''), md_content)
    return md_content

def convert_md_to_html(md_content):
    """Convert Markdown content to HTML."""
    html_content = convert_headings(md_content)
    html_content = convert_unordered_listing(html_content)
    html_content = convert_ordered_listing(html_content)
    html_content = convert_paragraphs(html_content)
    html_content = convert_bold_and_emphasis(html_content)
    html_content = convert_special_syntax(html_content)
    return html_content

def main():
    """Main function."""
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    try:
        with open(md_file, 'r') as f:
            md_content = f.read()
    except FileNotFoundError:
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)

    html_content = convert_md_to_html(md_content)

    with open(html_file, 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    main()
