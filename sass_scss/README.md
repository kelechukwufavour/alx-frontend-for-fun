# Sass/Scss Project

This repository contains Sass/Scss files for various tasks related to learning and practicing Sass.

## Requirements

- Ubuntu 18.04 LTS
- Sass 3.7.4 (or higher)

## Setup

1. Install Ruby and Sass:
   ```bash
   sudo apt-get install -y ruby2.5 ruby2.5-dev
   sudo apt-get install ubuntu-dev-tools
   gem install sass -v 3.7.4
   sass --version
Files and Tasks
0-debug_log.scss: Prints "Hello world" in the debug output.
1-color_variable.scss: Assigns the text color #3D3D3D to the HTML tags body and p.
2-color_variables.scss: Assigns text and background colors using Sass variables.
3-nested_tag.scss: Assigns margins using nested declarations.
4-nested_class.scss: Assigns text colors based on nested class selectors.
5-nested_child.scss: Assigns text colors to first child elements.
6-nested_hover.scss: Changes text color on hover using nested declarations.
7-nested_deeper.scss: Assigns font sizes using nested declarations.
8-mixin_margins.scss: Assigns margins using a mixin.
9-extend_list.scss: Uses @extend to apply styles to multiple classes.
10-import_colors.scss: Imports color variables from another file.
11-loop_photos.scss: Uses @each to create classes based on a list.
12-loop_header.scss: Uses @for to create H* tags with font sizes.
100-loop_col.scss: Uses @for to create .col-* classes with different widths.
101-media_query.scss: Uses @media queries for responsive font sizes.
102-media_query.scss: Uses multiple @media queries for responsive font sizes and colors.
103-sort_strings.scss: Sorts a list of strings and prints the sorted list.
