"""
ORLY MCP Server
"""

from mcp.server.fastmcp import FastMCP, Image
from mcp.types import TextContent
import sys
import os
import tempfile
import json

# Add the parent directory to the path to import from orly_generator.models
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from orly_generator.models import generate_image

# Initialize FastMCP server
mcp = FastMCP("ORLY")

@mcp.tool(
    description="""Generate an O'RLY? book cover image.
    
    This tool creates a parody book cover in the style of O'Reilly books with custom title, subtitle, author, and styling options.
    The generated image will be displayed directly in the chat.

    Args:
        title (str): The main title for the book cover
        subtitle (str): The subtitle text (appears at the top)
        author (str): The author name (appears at the bottom right)
        image_code (str, optional): Image code 1-40 for the animal/object on the cover. Defaults to random.
        theme (str, optional): Color theme 0-16. Defaults to random.
        guide_text_placement (str, optional): Where to place "The Definitive Guide" text - 'top_left', 'top_right', 'bottom_left', 'bottom_right'. Defaults to 'bottom_right'.
        guide_text (str, optional): The guide text to display. Defaults to 'The Definitive Guide'.

    Returns:
        Image: The generated O'RLY? book cover image that will be displayed in chat.
    """
)
def generate_orly_cover(
    title: str, 
    subtitle: str = "", 
    author: str = "Anonymous", 
    image_code: str = None, 
    theme: str = None,
    guide_text_placement: str = "bottom_right",
    guide_text: str = "The Definitive Guide"
) -> Image:
    if not title.strip():
        raise ValueError("Title cannot be empty.")
    
    try:
        # Set defaults if not provided
        if image_code is None:
            import random
            import time
            # Seed the random number generator with current time to improve randomness
            random.seed(time.time())
            image_code = str(random.randrange(1, 41))
        else:
            # Validate image_code is in range 1-40
            try:
                img_num = int(image_code)
                if not (1 <= img_num <= 40):
                    raise ValueError(f"Image code must be between 1 and 40, got {image_code}")
                image_code = str(img_num)
            except ValueError as ve:
                if "Image code must be between" in str(ve):
                    raise ve
                raise ValueError(f"Image code must be a number between 1 and 40, got '{image_code}'")
                
        if theme is None:
            import random
            theme = str(random.randrange(0, 17))
        else:
            # Validate theme is in range 0-16
            try:
                theme_num = int(theme)
                if not (0 <= theme_num <= 16):
                    raise ValueError(f"Theme must be between 0 and 16, got {theme}")
                theme = str(theme_num)
            except ValueError as ve:
                if "Theme must be between" in str(ve):
                    raise ve
                raise ValueError(f"Theme must be a number between 0 and 16, got '{theme}'")
        
        # Validate guide_text_placement
        valid_placements = ['top_left', 'top_right', 'bottom_left', 'bottom_right']
        if guide_text_placement not in valid_placements:
            raise ValueError(f"guide_text_placement must be one of {valid_placements}, got '{guide_text_placement}'")
        
        # Generate the image
        image_path = generate_image(
            title=title,
            topText=subtitle,
            author=author,
            image_code=image_code,
            theme=theme,
            guide_text_placement=guide_text_placement,
            guide_text=guide_text
        )
        
        # Return the image using the Image helper class for direct display
        return Image(path=image_path)
        
    except Exception as e:
        raise RuntimeError(f"Error generating book cover: {str(e)}") from e

def main():
    """Run the MCP server"""
    print("Starting ORLY MCP server...")
    mcp.run()

if __name__ == "__main__":
    main()
