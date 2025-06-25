# O-RLY-Book-Generator
Python tool for generating O RLY? Book Covers

## ORLY MCP Server

This project includes an MCP (Multi-Capability Proxy) server that allows ORLY to be used as a tool by other systems, such as Claude Desktop.

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

### Example Claude Desktop Configuration

You can add this server to your Claude Desktop configuration like so:

```json
{
    "mcp-orly": {
        "command": "uvx",
        "args": [
            "orly-mcp"
        ]
    }
}
```
