from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

# Model Loading
with open ('artifacts/random_forest_model.pkl', "rb") as file:
    model = pickle.load(file)


# Initialize the model
app = Flask(__name__)

@app.route('/predict', methods = ['POST'])
def predict():
    data = request.get_json() 
    features = np.array([data['GRE Score'], data['TOEFL Score'], data['University Rating'], 
                         data['SOP'], data['LOR'], data['CGPA'], data['Research']]).reshape(1, -1)
    
    # Make prediction

    pred = model.predict(features)[0]
    return jsonify({'Chance of Admit': round(pred, 2)})

if __name__ == '__main__':
     app.run(debug=True)