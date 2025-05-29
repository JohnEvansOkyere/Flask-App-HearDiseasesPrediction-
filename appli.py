# appli.py
from flask import Flask, render_template, request
from app import get_prediction_from_features

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        # Get data from form submission
        age = int(request.form["age"])
        sex = int(request.form["sex"])
        chest_pain_type = int(request.form["chest_pain_type"])
        resting_blood_pressure = int(request.form["resting_blood_pressure"])
        cholestoral = int(request.form["cholestoral"])
        fasting_blood_sugar = int(request.form["fasting_blood_sugar"])
        resting_electrocardiographic_results = int(request.form["resting_electrocardiographic_results"])
        max_heart_rate_achieved = int(request.form["max_heart_rate_achieved"])
        exercise_induced_angina = int(request.form["exercise_induced_angina"])
        st_depression = float(request.form["st_depression"])
        st_slope = int(request.form["st_slope"])
        number_of_major_vessels = int(request.form["number_of_major_vessels"])
        thalassemia = int(request.form["thalassemia"])

        # Create features list
        features = [age, sex, chest_pain_type, resting_blood_pressure, cholestoral,
                    fasting_blood_sugar, resting_electrocardiographic_results, max_heart_rate_achieved,
                    exercise_induced_angina, st_depression, st_slope, number_of_major_vessels, thalassemia]

        # Get the prediction
        prediction = get_prediction_from_features(features)

        # Interpret the result
        if prediction == 1:
            result = "The model predicts heart disease."
        else:
            result = "The model predicts no heart disease."

    return render_template("index.html", result=result)




# appli.py
from flask import Flask, render_template, request
from app import get_prediction  # Import the prediction function from app.py

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None  # Variable to hold the prediction result
    if request.method == "POST":
                # Get data from form submission
        age = int(request.form["age"])
        sex = int(request.form["sex"])
        chest_pain_type = int(request.form["chest_pain_type"])
        resting_blood_pressure = int(request.form["resting_blood_pressure"])
        cholestoral = int(request.form["cholestoral"])
        fasting_blood_sugar = int(request.form["fasting_blood_sugar"])
        resting_electrocardiographic_results = int(request.form["resting_electrocardiographic_results"])
        max_heart_rate_achieved = int(request.form["max_heart_rate_achieved"])
        exercise_induced_angina = int(request.form["exercise_induced_angina"])
        st_depression = float(request.form["st_depression"])
        st_slope = int(request.form["st_slope"])
        number_of_major_vessels = int(request.form["number_of_major_vessels"])
        thalassemia = int(request.form["thalassemia"])

        # Create features list
        features = [age, sex, chest_pain_type, resting_blood_pressure, cholestoral,
                    fasting_blood_sugar, resting_electrocardiographic_results, max_heart_rate_achieved,
                    exercise_induced_angina, st_depression, st_slope, number_of_major_vessels, thalassemia]
        # Get data from the form submission
        result = get_prediction()  # Call the get_prediction function from app.py
        
    # Return the rendered HTML page with the result
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
