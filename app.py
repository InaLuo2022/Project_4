import json
import pandas as pd

from flask import Flask, request, jsonify, render_template, session
from flask_session import Session

# Flask setup
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("insurance_estimator.html")

@app.route("/estimator", methods = ['POST'])
def estimator(): 
  
    client_age = request.form['client_age']
    bmi = request.form['bmi']
    children_no = request.form['children_no']
    gender = request.form['gender']
    smoker = request.form['smoker']
    medical_history = request.form['medical_history']
    family_medical_history= request.form['family_medical_history']
    exercise_frequency = request.form['exercise_frequency']
    occupation = request.form['occupation']
    coverage_level = request.form['coverage_level']

    client_data = {
        "age": client_age,
        "gender": gender,
        "bmi": bmi,
        "children": children_no,
        'smoker': smoker,
        'medical_history': medical_history,
        'family_medical_history': family_medical_history,
        'exercise_frequency': exercise_frequency,
        'occupation': occupation,
        'coverage_level': coverage_level
    } 


    json_string = json.dumps(client_data)
    print(json_string)

    return json_string

   
if __name__ == '__main__':
  app.run(debug=True)

