# Python Static Site Generator

A lightweight static site generator that transforms Markdown content into fully-templated HTML websites.

## Key Features

- **Markdown Processing**: Converts Markdown to HTML with support for both block-level and inline elements
- **Smart Title Extraction**: Automatically extracts page titles from H1 headings
- **Template System**: Flexible templating with variable substitution (`{{ Title }}`, `{{ Content }}`)
- **Static Asset Management**: Handles CSS, images, and other static files
- **Local Development Server**: Built-in server for immediate testing
- **Clean Architecture**: Modular design with separate components for HTML structure, Markdown processing, and content generation

## Core Components

- **HTML Node System**: Structured representation of HTML elements
- **Markdown Parser**: Full support for standard Markdown syntax
- **Template Processor**: Variable substitution and content injection
- **Asset Handler**: Static file management and directory organization

## Usage

- **./main.sh** - This builds the site and starts a local server at http://localhost:8888 to view the rendered HTML. 

This generator provides a solid foundation for building static websites with a focus on simplicity, performance, and maintainability.
