import json
from flask import Flask, request, jsonify, render_template

# Flask setup
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("insurance_estimator.html")

import joblib

# Load the machine learning model from the .joblib file
model = joblib.load('model_LinearRegression.joblib')

# create route for model prediction
@app.route('/estimator', methods = ['POST'])

def estimator():
    # Get the client data from "insurance_estimator.html"
    data = json.loads(request.data)

    # transform data to feature to fit the model
    features = [[data["age"], data["bmi"], data["children"], data["female"], data["male"], data['No'], data["Yes"],  \
                 data['Diabetes'], data['Heart_disease'], data['High_blood_pressure'], data['None'], \
                 data['Family_Diabetes'], data['Family_Heart_disease'], data['Family_High_blood_pressure'], \
                 data['Family_None'], data['Frequently'], data['exercise_Never'], data['Occasionally'], data['Rarely'], \
                 data['Blue_collar'], data['Student'], data['Unemployed'], data['White_collar'], \
                 data['Basic'], data['Premium'], data['Standard']]] 

    # make predition by using model
    estimator = model.predict (features)

    return jsonify({'prediction': estimator[0]})

if __name__ == '__main__':
  app.run()