# init.py
from flask_cors import CORS
import os
from flask import Flask
from app.route import Router

def create_app():
    """Flask app factory."""
    app = Flask(__name__, instance_relative_config=True)
    
    # for react
    CORS(app)  # Enable CORS for all routes

    # Load the configuration from the config file
    app.config.from_pyfile("config.py")  
    
    # Optionally load an environment-specific config
    if "APP_CONFIG_FILE" in os.environ:
        app.config.from_envvar("APP_CONFIG_FILE")
    
    # Register routes within the application 
    with app.app_context():
        router = Router()
        router.init_app_routes()
    
    @app.route("/")
    def home():
        return "Welcome to the Web App"
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
