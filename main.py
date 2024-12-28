from flask import Flask, request, jsonify
import logging
from werkzeug.exceptions import HTTPException

# Initialize Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Sample route to test if the app is running
@app.route('/')
def home():
    return 'Hello, Flask is running!'

# Error handling for HTTP errors
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = f'Error: {e.description}'.encode('utf-8')
    response.content_type = "application/json"
    return response

# You can add more routes and logic below as needed

if __name__ == '__main__':
    app.run(debug=True)  # You can set debug to False in production