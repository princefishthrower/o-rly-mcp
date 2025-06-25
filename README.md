# o-rly-mcp

An MCP (Model Context Protocol) server for generating O'RLY? (O'Reilly parody) book covers that display directly in Claude Desktop application.

## Quick Start

### Install on MCP Server

simply add the following to your mcp configuration:

```shell
"mcp-orly": {
    "command": "uvx",
    "args": [
        "orly-mcp"
    ]
}
```

### Local Development

```shell
# Clone the repository
git clone [your-repo-url]
cd o-rly-mcp

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
        "/path/to/your/o-rly-mcp/orly_mcp/server.py"
      ],
      "cwd": "/path/to/your/o-rly-mcp"
    }
  }
}
```

**Important:** Replace `/path/to/your/o-rly-mcp` with your actual project path.

### Alternative: Package Installation

```shell
# Install in editable mode
uv pip install -e .

# Claude Desktop config
{
  "mcpServers": {
    "orly-local": {
      "command": "uvx",
      "args": ["--from", "/your/path/to/o-rly-mcp", "orly-mcp"]
    }
  }
}
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'mcp'" Error

If you see this error, the MCP dependencies aren't available:

```shell
cd /path/to/your/o-rly-mcp
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

This project builds upon the excellent work by Charles Berlin. The core image generation code in the `orly_generator/` directory is adapted from his original [o-rly-mcp](https://github.com/charleshberlin/o-rly-mcp) repository, updated to work with Python 3 and integrated into an MCP server for Claude Desktop.
