from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Example API endpoint
@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from Flask API, Testing!!'})

# WSGI callable function for Waitress or Gunicorn
def create_wsgi():
    return app

if __name__ == '__main__':
    app.run(debug=True)
