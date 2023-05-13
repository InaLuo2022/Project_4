import json
import pandas as pd
import numpy as np

# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

# Flask setup
app = Flask(__name__, static_url_path='/static')

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
# 'or' allows us to later switch from 'sqlite' to an external database like 'postgres' easily
# os.environ is used to access 'environment variables' from the operating system
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    insurance_basic = db.Column(db.Float)
    insurance_standard = db.Column(db.Float)
    insurance_premium = db.Column(db.Float)
    insurance_option = db.Column(db.Float)

    def __repr__(self):
        return '<client %r>' % (self.name)
    
with app.app_context():
    db.create_all()

#################################################
# Model Setup
#################################################

from joblib import load
model_path = os.environ.get('MODEL_PATH', '') or "model_DecisionTreeRegressor.joblib"
print("Loading model...")
model = load(model_path)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact_us.html")

@app.route("/estimator", methods = ['GET','POST'])
def estimator(): 
    if request.method == 'POST':
        estimate = []

        #create library of all categories
        library = {'gender': ['Female', 'Male'], 'smoker': ['No', 'Yes'], 'region': ['Northeast', 'Northwest','Southeast', 'Southwest'], 'medical_history': ['Diabetes', 'Heart disease', 'High blood pressure', 'None'], 'family_medical_history': ['Diabetes', 'Heart disease', 'High blood pressure', 'None'], 'exercise_frequency': ['Frequently', 'Never', 'Occasionally', 'Rarely'], 'occupation': ['Blue collar', 'Student', 'Unemployed', 'White collar'], 'coverage_level': ['Basic', 'Premium', 'Standard']}
        #identify  the original column headers (also in library - used for lookup
        column = ['gender','smoker', 'region', 'medical_history', 'family_medical_history', 'exercise_frequency', 'occupation', 'coverage_level']
    
        #retrieve dta from html form
        client_age = request.form['client_age']
        bmi = request.form['bmi']
        children_no = request.form['children_no']
        gender = request.form['gender']
        smoker = request.form['smoker']
        region = request.form['region']
        medical_history = request.form['medical_history']
        family_medical_history= request.form['family_medical_history']
        exercise_frequency = request.form['exercise_frequency']
        occupation = request.form['occupation']
        coverage_level = request.form['coverage_level']
        
        #Create a list of categorical form answers
        form_input = [gender, smoker, region, medical_history, family_medical_history, exercise_frequency, occupation, coverage_level]
        
        #enter  numerical values for prediction
        estimate.append(client_age)
        estimate.append(bmi)
        estimate.append(children_no)
        
        #create numerical values for categories for prediction
        for j in range(len(column)):
            item = column[j]
            temp = []
            for selection in range(len(library[item])):
                temp.append(0)
            for i in range(len(library[item])):
                if library[item][i] == form_input[j]:
                    temp[i] = 1
            estimate.extend(temp)
     
        client_data_list_Basic=estimate.copy()
        client_data_list_Basic[27:30]=[1, 0, 0]
            
        client_data_list_Standard=estimate.copy()
        client_data_list_Standard[27:30]=[0, 0, 1]
            
        client_data_list_Premium=estimate.copy()
        client_data_list_Premium[27:30]=[0, 1, 0]
            
        client_data_list_Option=estimate.copy()
           
        index1 = model.predict([client_data_list_Basic])
        index2 = model.predict([client_data_list_Standard])
        index3 = model.predict([client_data_list_Premium])
        index4 = model.predict([client_data_list_Option])
        
        # response = jsonify(f"Predicted Insurance Basic: {index1}, Predicted Insurance Standard: {index2}, Predicted Insurance Premium:{index3}")
        client_insurance = client(insurance_basic=index1, insurance_standard=index2, insurance_premium=index3, insurance_option=index4)

        db.session.add(client_insurance)
        db.session.commit()

        # return jsonify(f"Predicted Insurance Basic: {index1}, Predicted Insurance Standard: {index2}, Predicted Insurance Premium:{index3}")
        return render_template("insurance_analysis.html")
    return render_template('insurance_estimator.html')

# jsonify(f"Predicted Insurance Basic: {index1}, Predicted Insurance Standard: {index2}, Predicted Insurance Premium:{index3}")

@app.route("/analysis")
def analysis():

    insurance_results = db.session.query(client.insurance_basic, client.insurance_standard, client.insurance_premium, client.insurance_option).all()
     # Create a dictionary from the row data and append to a list
    insurance_basic = [result[0] for result in insurance_results]
    insurance_standard = [result[1] for result in insurance_results]
    insurance_premium = [result[2] for result in insurance_results]
    insurance_option = [result[3] for result in insurance_results]
    data_length = len(insurance_results)-1

    insurance_data = [{'Basic': insurance_basic[data_length], 'Standard': insurance_standard[data_length], 'Premium': insurance_premium[data_length], 'Client_option': insurance_option[data_length]}]
    response = jsonify(insurance_data)

    # jsonify(f"Predicted Insurance Basic: {response[0]}, Predicted Insurance Standard: {response[1]}, Predicted Insurance Premium:{response[2]}")
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
  app.run()
  