# O-RLY-Book-Generator

Python tool for generating O RLY? Book Covers

## Local Development

First create a virtual environment:

```bash
uv venv .venv
```

Install the required dependencies:

```bash
uv pip install -r requirements.txt
```

**For MCP server development, you can also install in editable mode:**

```bash
uv pip install -e .
```

Test a sample image:

```bash
uv run python main.py
```

You should see a `.png` generated within the `slack` directory where the filename is the datetime of generation.

## MCP Server Local Development

To run the MCP server locally for development, you have two options:

### Option 1: Using the helper script (recommended)
```shell
cd /path/to/your/local/clone/O-RLY-Book-Generator
python start_server.py
```

### Option 2: Direct command
```shell
cd /path/to/your/local/clone/O-RLY-Book-Generator
uv run python orly_mcp/server.py
```

The server will start and listen for MCP requests. You should see "Starting ORLY MCP server..." when it's running.

### Testing the MCP Server

You can test the server functionality with:

```shell
# Basic functionality test
uv run python test_mcp.py

# Comprehensive image conversion test
uv run python test_image_conversion.py

# Input validation test
uv run python test_validation.py

# Comprehensive setup test (recommended)
uv run python test_comprehensive.py
```


## ORLY MCP Server

This project includes an MCP (Model Context Protocol) server that allows ORLY to be used as a tool by other systems, such as Claude Desktop. The generated book cover images are displayed directly in the chat interface!

### Installation

To install the ORLY MCP server and its dependencies, you can use `uv` (or `pip`). From the root of this repository:

```bash
uv pip install .
```

Alternatively, if you are developing the tool, you can install it in editable mode:

```bash
uv pip install -e .
```

### Running the Server

Once installed, you can run the MCP server using `uvx` (or directly if your environment is set up):

```bash
uvx orly-mcp
```

This will start the server, and it will listen for requests.

### Claude Desktop Configuration for Local Development

For local development, you have two options:

#### Option 1: Using the installed package approach (Recommended)

First, install the package in editable mode:
```bash
cd /Users/chris/enterprise/O-RLY-Book-Generator
uv pip install -e .
```

Then configure Claude Desktop:
```json
{
  "mcpServers": {
    "orly-local": {
      "command": "uvx",
      "args": ["--from", "/Users/chris/enterprise/O-RLY-Book-Generator", "orly-mcp"]
    }
  }
}
```

#### Option 2: Direct script execution

Make sure dependencies are installed first:
```bash
cd /Users/chris/enterprise/O-RLY-Book-Generator
uv pip install -r requirements.txt
```

Then configure Claude Desktop:
```json
{
  "mcpServers": {
    "orly-local": {
      "command": "uv",
      "args": [
        "run", 
        "--with", "fastmcp",
        "python", 
        "/Users/chris/enterprise/O-RLY-Book-Generator/orly_mcp/server.py"
      ],
      "cwd": "/Users/chris/enterprise/O-RLY-Book-Generator"
    }
  }
}
```

**Note:** Replace `/Users/chris/enterprise/O-RLY-Book-Generator` with the actual absolute path to your O-RLY-Book-Generator directory.

## Troubleshooting

### "ModuleNotFoundError: No module named 'mcp'" Error

If you see this error when Claude Desktop tries to run the MCP server, it means the MCP dependencies aren't available. Here are the solutions:

1. **Ensure dependencies are installed:**
   ```bash
   cd /path/to/your/O-RLY-Book-Generator
   uv pip install -r requirements.txt
   ```

2. **Use Option 1 from the Claude Desktop configuration above** (recommended) - install the package in editable mode and use `uvx`

3. **For Option 2**, make sure your Claude Desktop configuration includes `--with fastmcp`:
   ```json
   {
     "mcpServers": {
       "orly-local": {
         "command": "uv",
         "args": [
           "run", 
           "--with", "fastmcp",
           "python", 
           "/your/path/to/O-RLY-Book-Generator/orly_mcp/server.py"
         ],
         "cwd": "/your/path/to/O-RLY-Book-Generator"
       }
     }
   }
   ```

### Flask Import Errors

The MCP server is designed to work independently of Flask. If you encounter Flask-related import errors, this should be automatically resolved as the code has been updated to import only the necessary modules without going through Flask dependencies.

### Example Claude Desktop Configuration for Installed Package

You can add this server to your Claude Desktop configuration like so:

```json
{
  "mcpServers": {
    "mcp-orly": {
      "command": "uvx",
      "args": [
        "orly-mcp"
      ]
    }
  }
}
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
