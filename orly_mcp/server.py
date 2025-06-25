"""
ORLY MCP Server
"""

from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent
from o_rly_book_generator.models import generate_image
import tempfile
import os

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
    image_bytes = generate_image(prompt)

    # Save the image to a temporary file
    temp_dir = tempfile.gettempdir()
    temp_file_path = os.path.join(temp_dir, "orly_image.png")
    with open(temp_file_path, "wb") as f:
        f.write(image_bytes)

    return TextContent(type="text", text=f"Image saved to {temp_file_path}")

def main():
    """Run the MCP server"""
    print("Starting ORLY MCP server...")
    mcp.run()

if __name__ == "__main__":
    main()
