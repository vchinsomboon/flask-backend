from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Flask!'}
    return jsonify(data)

# WSGI callable function for Waitress or Gunicorn
def create_wsgi():
    return app

if __name__ == '__main__':
    app.run(debug=True)
