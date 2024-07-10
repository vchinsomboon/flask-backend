from flask import Flask, request, jsonify
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

@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.json  # Assuming data is sent as JSON
    # Process the data
    print(data)  # Print to see data received in the console
    return jsonify({'message': 'Data received successfully'}), 200

# WSGI callable function for Waitress or Gunicorn
def create_wsgi():
    return app

if __name__ == '__main__':
    app.run(debug=True)
