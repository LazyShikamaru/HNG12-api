from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET'])
def get_info():
    email = "joshbosseisfresh@gmail.com"
    current_datetime = datetime.utcnow().isoformat() + "Z"
    github_url = "https://github.com/LazyShikamaru/HNG12-api"
    return jsonify({
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    })

if __name__ == '__main__':
    app.run(debug=True)
