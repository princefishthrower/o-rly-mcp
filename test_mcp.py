#!/usr/bin/env python3
"""
Test script for the ORLY MCP server tool
"""

import sys
import os

# Add the current directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from orly_mcp.server import generate_orly_cover

def test_generate_cover():
    """Test the generate_orly_cover function directly"""
    print("Testing ORLY cover generation...")
    
    try:
        result = generate_orly_cover(
            title="Python Programming",
            subtitle="Learning the Hard Way",
            author="Test Author",
            image_code="1",
            theme="5"
        )
        
        print("✅ Success! Generated O'RLY book cover image.")
        print(f"📧 Return type: {type(result)}")
        print(f"🖼️  Image format: {result._mime_type}")
        print(f"📁 Image path: {result.path}")
        
        # If we have image data, show size
        if result.data:
            print(f"📊 Image data size: {len(result.data)} bytes")
        elif result.path and os.path.exists(result.path):
            size = os.path.getsize(result.path)
            print(f"📊 Image file size: {size} bytes")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_generate_cover()
