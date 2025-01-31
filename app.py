from flask import Flask, jsonify  # Import Flask for web server and jsonify for JSON response
from datetime import datetime  # Import datetime to get current time

# Create a Flask application
app = Flask(__name__)

# Define the API endpoint
@app.route('/', methods=['GET'])
def get_info():
    return jsonify({
        "email": "joshbosseisfresh@gmail.com", 
        "current_datetime": datetime.utcnow().isoformat() + "Z",  # Get current UTC time
        "github_url": "https://github.com/LazyShikamaru/HNG12-api"  # Replace with your GitHub repo URL
    })

# Run the Flask app (if this file is run directly)
if __name__ == '__main__':
    app.run(debug=True)
