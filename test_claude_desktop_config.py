#!/usr/bin/env python3
"""
Test script to verify the exact Claude Desktop configuration works
"""

import subprocess
import sys
import os

def test_claude_desktop_command():
    """Test the exact command that Claude Desktop will use"""
    print("🧪 Testing Claude Desktop MCP configuration...")
    
    # Change to the project directory
    os.chdir("/Users/chris/enterprise/O-RLY-Book-Generator")
    
    # The exact command from Claude Desktop config
    cmd = [
        "uv", "run",
        "--with", "fastmcp",
        "--with", "pillow", 
        "--with", "fonttools",
        "--with", "requests",
        "python", "-c",
        "from orly_generator.models import generate_image; print('✅ All imports successful')"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print("✅ Claude Desktop command works!")
            print(f"   Output: {result.stdout.strip()}")
            return True
        else:
            print("❌ Claude Desktop command failed!")
            print(f"   Error: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("❌ Command timed out")
        return False
    except Exception as e:
        print(f"❌ Error running command: {e}")
        return False

def test_server_startup():
    """Test that the server can start with the exact command"""
    print("\n🚀 Testing MCP server startup...")
    
    # Test import of the server module
    cmd = [
        "uv", "run",
        "--with", "fastmcp",
        "--with", "pillow", 
        "--with", "fonttools", 
        "--with", "requests",
        "python", "-c",
        """
import sys
sys.path.insert(0, '/Users/chris/enterprise/O-RLY-Book-Generator')
try:
    from orly_mcp.server import app
    print('✅ MCP server can be imported')
except Exception as e:
    print(f'❌ Server import failed: {e}')
    sys.exit(1)
"""
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print("✅ MCP server startup test passed!")
            print(f"   Output: {result.stdout.strip()}")
            return True
        else:
            print("❌ MCP server startup failed!")
            print(f"   Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error testing server: {e}")
        return False

if __name__ == "__main__":
    print("🎯 Testing Claude Desktop MCP configuration...")
    
    test1 = test_claude_desktop_command()
    test2 = test_server_startup()
    
    if test1 and test2:
        print("\n🎉 All tests passed! Claude Desktop configuration is ready!")
        print("\n📋 Next steps:")
        print("1. Restart Claude Desktop")
        print("2. Ask Claude to generate an O'RLY book cover!")
    else:
        print("\n❌ Some tests failed. Check the configuration.")
        sys.exit(1)
