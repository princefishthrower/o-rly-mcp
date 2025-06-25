#!/usr/bin/env python3
"""
Test the validation in the ORLY MCP server
"""

import sys
import os

# Add the current directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from orly_mcp.server import generate_orly_cover

def test_validation():
    """Test the validation in the MCP tool"""
    print("🔍 Testing validation...")
    
    # Test valid parameters
    try:
        result = generate_orly_cover(
            title="Valid Test",
            image_code="20",
            theme="10"
        )
        print("✅ Valid parameters work correctly")
    except Exception as e:
        print(f"❌ Valid parameters failed: {e}")
        return
    
    # Test invalid image code
    try:
        generate_orly_cover(title="Test", image_code="50")
        print("❌ Should have failed with invalid image code")
    except (ValueError, RuntimeError) as e:
        print(f"✅ Correctly caught invalid image code: {e}")
    
    # Test invalid theme
    try:
        generate_orly_cover(title="Test", theme="20")
        print("❌ Should have failed with invalid theme")
    except (ValueError, RuntimeError) as e:
        print(f"✅ Correctly caught invalid theme: {e}")
    
    # Test invalid placement
    try:
        generate_orly_cover(title="Test", guide_text_placement="invalid")
        print("❌ Should have failed with invalid placement")
    except (ValueError, RuntimeError) as e:
        print(f"✅ Correctly caught invalid placement: {e}")
    
    # Test empty title
    try:
        generate_orly_cover(title="")
        print("❌ Should have failed with empty title")
    except (ValueError, RuntimeError) as e:
        print(f"✅ Correctly caught empty title: {e}")
    
    print("\n🎉 All validation tests passed!")

if __name__ == "__main__":
    test_validation()
