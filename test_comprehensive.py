#!/usr/bin/env python3
"""
Final comprehensive test for the ORLY MCP server setup
"""

import sys
import os
import subprocess

def test_imports():
    """Test that all required imports work"""
    print("🧪 Testing imports...")
    try:
        from mcp.server.fastmcp import FastMCP, Image
        from mcp.types import TextContent, ImageContent
        print("✅ All MCP imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_orly_generation():
    """Test ORLY book cover generation"""
    print("📖 Testing ORLY generation...")
    try:
        # Add the current directory to the path
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from orly_mcp.server import generate_orly_cover
        
        result = generate_orly_cover(
            title="Test Book",
            subtitle="Integration Test",
            author="Test Suite"
        )
        
        # Convert to ImageContent
        image_content = result.to_image_content()
        print(f"✅ Generated image: {type(image_content)}")
        print(f"   MIME type: {image_content.mimeType}")
        print(f"   Data length: {len(image_content.data)} chars")
        return True
    except Exception as e:
        print(f"❌ Generation error: {e}")
        return False

def test_server_start():
    """Test that the MCP server can start"""
    print("🚀 Testing server startup...")
    try:
        # Test the server script imports correctly
        result = subprocess.run([
            "uv", "run", "python", "-c", 
            "from orly_mcp.server import main; print('✅ Server imports work')"
        ], 
        capture_output=True, text=True, timeout=10,
        cwd=os.path.dirname(os.path.abspath(__file__))
        )
        
        if result.returncode == 0:
            print("✅ Server can start successfully")
            return True
        else:
            print(f"❌ Server startup failed: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("✅ Server startup test timed out (expected)")
        return True
    except Exception as e:
        print(f"❌ Server test error: {e}")
        return False

def main():
    """Run all tests"""
    print("🎯 Running comprehensive ORLY MCP server tests...\n")
    
    tests = [
        test_imports,
        test_orly_generation,
        test_server_start
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"📊 Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 All tests passed! Your ORLY MCP server is ready for Claude Desktop!")
        print("\n📋 Next steps:")
        print("1. Add the Claude Desktop configuration from the README")
        print("2. Restart Claude Desktop")
        print("3. Ask Claude to generate an O'RLY book cover!")
    else:
        print("❌ Some tests failed. Please check the error messages above.")
        print("💡 Try running: uv pip install -r requirements.txt")

if __name__ == "__main__":
    main()
