"""
ORLY MCP Server
"""

from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent

# Initialize FastMCP server
mcp = FastMCP("ORLY")

@mcp.tool(
    description="""This is a placeholder tool for ORLY.
    It takes a prompt and returns a dummy response.

    Args:
        prompt (str): The input prompt for the ORLY tool.

    Returns:
        TextContent: A TextContent object containing the dummy response.
    """
)
def run_orly_tool(prompt: str) -> TextContent:
    if not prompt:
        # MCP tools should handle errors gracefully or use make_error if available
        # For simplicity, returning a TextContent error message here.
        return TextContent(type="text", text="Error: Prompt cannot be empty.")

    # In a real scenario, this is where you would integrate with your ORLY tool's logic.
    # For now, it just returns a dummy response.
    dummy_response = f"ORLY has processed your prompt: '{prompt}'. This is a placeholder response."
    return TextContent(type="text", text=dummy_response)

def main():
    """Run the MCP server"""
    print("Starting ORLY MCP server...")
    mcp.run()

if __name__ == "__main__":
    main()
