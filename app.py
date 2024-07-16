from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Load the saved model
model = joblib.load('titanic-survival-model.joblib')

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Flask!'}
    return jsonify(data)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json  # Assuming data is sent as JSON
    print(data)
    # Convert the received data to a DataFrame
    df = pd.DataFrame([data])
    # Ensure the DataFrame has the same structure as the training data
    df = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]

    # Make predictions
    prediction = model.predict(df)

     # Map predictions to human-readable labels
    if prediction[0] == 0:
        result = 'NOT SURVIVE'
    elif prediction[0] == 1:
        result = 'SURVIVE'
    else:
        result = 'Unknown'  # Handle unexpected predictions if needed
    
    print(result)
    # Return result as JSON
    return jsonify({'prediction_result': result}), 200

if __name__ == '__main__':
    app.run(debug=True)
