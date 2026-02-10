from flask import Flask

def create_app():
    """Application factory pattern for creating Flask app."""
    app = Flask(__name__)
    
    # Import and register routes
    from app import routes
    app.register_blueprint(routes.bp)
    
    return app
