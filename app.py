import warnings
warnings.filterwarnings("ignore")  # Suppress all warnings


from flask import Flask
import sys
from core.routes import configure_routes  # Import setup_routes function

# Initialize the Flask application
app = Flask(__name__, static_folder='core/static', template_folder='core/templates')

# Set up the routes
configure_routes(app)


# If the script is executed directly, run the app
if __name__ == '__main__':
    app.run(debug=True)

