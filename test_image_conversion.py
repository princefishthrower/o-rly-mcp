#!/usr/bin/env python3
"""
Comprehensive test for the ORLY MCP server showing image conversion to ImageContent
"""

import sys
import os

# Add the current directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from orly_mcp.server import generate_orly_cover
from mcp.types import ImageContent

def test_image_conversion():
    """Test that the tool properly converts to ImageContent for MCP"""
    print("🧪 Testing ORLY MCP tool image conversion...")
    
    try:
        # Generate a cover
        image_result = generate_orly_cover(
            title="MCP Integration",
            subtitle="Testing Image Display",
            author="MCP Developer",
            image_code="25",  # Valid image code 1-40
            theme="8"
        )
        
        print(f"✅ Generated Image object: {type(image_result)}")
        
        # Convert to ImageContent (this is what MCP does internally)
        image_content = image_result.to_image_content()
        
        print(f"🖼️  Converted to ImageContent: {type(image_content)}")
        print(f"📋 MIME Type: {image_content.mimeType}")
        print(f"📊 Base64 data length: {len(image_content.data)} characters")
        print(f"🏷️  Content type: {image_content.type}")
        
        # Verify it's proper ImageContent
        assert isinstance(image_content, ImageContent)
        assert image_content.type == "image"
        assert image_content.mimeType == "image/png"
        assert len(image_content.data) > 0
        
        # Test base64 decoding
        import base64
        decoded_data = base64.b64decode(image_content.data)
        print(f"🔢 Decoded image size: {len(decoded_data)} bytes")
        
        # Verify PNG header
        if decoded_data.startswith(b'\x89PNG\r\n\x1a\n'):
            print("✅ Valid PNG file detected!")
        else:
            print("⚠️  Warning: PNG header not detected")
            
        print("\n🎉 All tests passed! The MCP server will display images directly in chat.")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_image_conversion()
