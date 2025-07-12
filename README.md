# orly-mcp

[![MCP Tool](https://img.shields.io/badge/MCP-Tool-yellow?labelColor=yellow)](https://modelcontextprotocol.io)
[![PyPI version](https://img.shields.io/pypi/v/orly-mcp.svg)](https://pypi.org/project/orly-mcp/)
[![Python versions](https://img.shields.io/pypi/pyversions/orly-mcp.svg)](https://pypi.org/project/orly-mcp/)

![Cooked myself with my own MCP tool :/](./demo.png)

An MCP (Model Context Protocol) server for generating O'RLY? (O'Reilly parody) book covers that display directly in Claude Desktop application.

## Quick Start

### Install on MCP Server

simply add the following to your mcp configuration:

```json
// ... other MCP servers ...
"mcp-orly": {
    "command": "uvx",
    "args": [
        "orly-mcp@latest"
    ]
}
// ... other MCP servers ...
```

### Local Development

```shell
# Clone the repository
git clone [your-repo-url]
cd orly-mcp

# Create a virtual environment and install dependencies
uv venv .venv
uv pip install -r requirements.txt

# Test a sample image generation
uv run python test_mcp.py

# Run comprehensive tests
uv run python test_comprehensive.py

# Start the MCP server for development
python start_server.py
```

## Claude Desktop Configuration

Add this MCP server to your Claude Desktop configuration file (`claude_desktop_config.json`):

### Recommended Configuration

```json
{
  "mcpServers": {
    "orly-local": {
      "command": "uv",
      "args": [
        "run",
        "--with", "fastmcp",
        "--with", "pillow",
        "--with", "fonttools",
        "--with", "requests",
        "python",
        "/path/to/your/orly-mcp/orly_mcp/server.py"
      ],
      "cwd": "/path/to/your/orly-mcp"
    }
  }
}
```

**Important:** Replace `/path/to/your/orly-mcp` with your actual project path.

### Alternative: Package Installation

```shell
# Install in editable mode
uv pip install -e .

# Claude Desktop config
{
  "mcpServers": {
    "orly-local": {
      "command": "uvx",
      "args": ["--from", "/your/path/to/orly-mcp", "orly-mcp"]
    }
  }
}
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'mcp'" Error

If you see this error, the MCP dependencies aren't available:

```shell
cd /path/to/your/orly-mcp
uv pip install -r requirements.txt
```

Make sure your Claude Desktop configuration includes all required dependencies with `--with` flags.

### "ModuleNotFoundError: No module named 'fontTools'" Error

Ensure all dependencies are specified in your Claude Desktop configuration:

```json
"args": [
  "run",
  "--with", "fastmcp",
  "--with", "pillow",
  "--with", "fonttools", 
  "--with", "requests",
  "python",
  "/your/path/to/orly_mcp/server.py"
]
```

### Testing Your Setup

Run the comprehensive test to verify everything works:

```shell
uv run python test_comprehensive.py
```

### Using the ORLY Tool in Claude

Once configured, you can ask Claude to generate O'RLY book covers like this:

- "Create an O'RLY book cover with the title 'Advanced Debugging' and author 'Jane Developer'"
- "Generate a book cover titled 'Machine Learning Mistakes' with subtitle 'What Could Go Wrong?' by 'AI Enthusiast'"
- "Make an O'RLY cover for 'CSS Grid Mastery' with theme 7 and image 15"

**✨ The generated book cover images will be displayed directly in the chat!**

The tool supports these parameters:
- **title** (required): Main book title
- **subtitle** (optional): Text at the top of the cover
- **author** (optional): Author name (bottom right)
- **image_code** (optional): Animal/object image 1-40 (random if not specified)
- **theme** (optional): Color theme 0-16 (random if not specified)  
- **guide_text_placement** (optional): Position of guide text - 'top_left', 'top_right', 'bottom_left', 'bottom_right'
- **guide_text** (optional): Custom guide text (defaults to "The Definitive Guide")

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

The original O'RLY book cover generation code in the `orly_generator/` directory is based on work by Charles Berlin (2016) and is also licensed under the MIT License - see [orly_generator/LICENSE.txt](orly_generator/LICENSE.txt) for details.

## Acknowledgments

This project builds upon the excellent work by Charles Berlin. The core image generation code in the `orly_generator/` directory is adapted from his original [O-RLY-Book-Generator](https://github.com/charleshberlin/O-RLY-Book-Generator) repository, updated to work with Python 3 and integrated into an MCP tool for usage with MCP clients like Claude Desktop.

## Publish

(More for Chris, the Author, since he never uses Python and will forget this)

You can quickly publish a new version using twine:

```shell
uv run twine upload dist/*
````

You'll be prompted to enter your PyPI API token.


You can quickly publish a new version using twine:

```shell
# Install dev dependencies (includes build and twine)
uv sync --group dev

# Build the package
uv run python -m build

# Check the built package
uv run twine check dist/*

# Publish to TestPyPI first for testing (optional)
uv run twine upload --repository testpypi dist/*

# Publish to PyPI
uv run twine upload dist/*
```

Make sure to:
1. Update the version number in `pyproject.toml`
2. Test the package locally with `uv run python test_comprehensive.py`
3. Build and publish

For authentication, you'll need PyPI API tokens configured in your `~/.pypirc` file or set as environment variables.ons/orly-mcp.svg)](https://pypi.org/project/orly-mcp/)