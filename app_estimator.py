""" This is a flask application called 'Estimator'
with both UI and API components
"""

# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request
)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

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

# TODO: Add data models if needed

with app.app_context():
    db.create_all()

#################################################
# Model Setup
#################################################

from joblib import load
model_path = os.environ.get('MODEL_PATH', '') or "model_LinearRegression.joblib"
print("Loading model...")
model = load(model_path)

#################################################
# Web User Interface - Front End
#################################################
# note that UI routes return a html response
# you can add as many html pages as you need
# below is an example to get you started...

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("insurance_estimator.html")

# TODO: Add more routes if needed

#################################################
# API - Back End
#################################################
# we will use '/api/..' for our api within flask application
# note that api returns a JSON response
# you can add as many API routes as you need
# below is an example to get you started...

@app.route("/prediction", methods=["POST"])
def predict():
    labels = ['setosa', 'versicolor', 'virginica']
    index = model.predict(
        [
            [
            float(request.form["Sepal length"]),
            float(request.form["Sepal width"]),
            float(request.form["Petal length"]),
            float(request.form["Petal width"]),
            ],
        ]
    )[0]
    return jsonify(f"Predicted Iris Species: {labels[index]}")


if __name__ == "__main__":

    # run the flask app
    app.run()
