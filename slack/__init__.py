import os

# Only import Flask and create app when needed (for web server)
app = None

def create_app():
    """Create Flask app only when needed for web server"""
    global app
    if app is None:
        from flask import Flask
        app = Flask(__name__)
        from slack import views
    return app
