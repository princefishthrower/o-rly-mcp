#!/usr/bin/env python3
"""
Helper script to start the ORLY MCP server
"""

import subprocess
import sys
import os

def main():
    """Start the ORLY MCP server"""
    # Get the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change to the project root directory
    os.chdir(script_dir)
    
    print("🚀 Starting ORLY MCP Server...")
    print(f"Working directory: {os.getcwd()}")
    print("Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        # Run the server
        subprocess.run([
            "uv", "run", "python", "orly_mcp/server.py"
        ], check=True)
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
        sys.exit(0)
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
