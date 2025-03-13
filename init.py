from flask import Flask
from app.route import Router  # Import Router class

app = Flask(__name__)  # Initialize Flask app

# Sample configuration 
app.config["DEBUG"] = True

# Register routes within app context
with app.app_context():
    router = Router()
    router.init_app_routes()  # Register routes

@app.route("/")
def home():
    return "Welcome to the Web App"

# Run the app
if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
