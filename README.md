# alx-frontend-for-fun
# Markdown to HTML Converter

This is a Python script that converts Markdown files to HTML format, adhering to specific syntax and requirements.

## Requirements

- All files are interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7 or higher.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- PEP 8 style (version 1.7.*) is followed.
- All files must be executable.
- All modules are documented using `python3 -c 'print(__import__("my_module").__doc__)'`.
- Code should not be executed when imported (by using `if __name__ == "__main__":`).

## Usage

To use the script, provide two arguments:
Where:
- `input.md` is the Markdown file you want to convert.
- `output.html` is the desired name for the output HTML file.

## Tasks Implemented

- **Start a Script**: The script initializes with basic functionality and argument validation.
- **Headings**: Supports converting Markdown headings to HTML `<h1>` to `<h6>` tags.
- **Unordered Listing**: Converts Markdown unordered lists to HTML `<ul>` tags.
- **Ordered Listing**: Converts Markdown ordered lists to HTML `<ol>` tags.
- **Simple Text**: Converts Markdown paragraphs to HTML `<p>` tags.
- **Bold and Emphasis Text**: Converts Markdown bold and emphasis syntax to HTML `<b>` and `<em>` tags.
- **Special Syntax**: Implements special syntax conversion as per requirements.

## Execution Examples

Include examples of script execution and generated HTML files.

## File Structure

- `markdown2html.py`: Main Python script file.
- `README.md`: This file, providing an overview of the project and instructions.
- Other files and folders as necessary.

## License

This project is licensed under the [MIT License](LICENSE).
