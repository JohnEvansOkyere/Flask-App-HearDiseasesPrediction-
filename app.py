# app.py
from heart_disease_model import predict_heart_disease
from flask import request

def get_prediction():
    """
    Retrieves user input from the Flask request and predicts heart disease.
    
    Returns:
        str: A message indicating whether heart disease is predicted or not.
    """
    try:
        # Retrieve input values from the form submission
        age = int(request.form["age"])
        sex = int(request.form["sex"])
        chest_pain_type = int(request.form["chest_pain_type"])
        resting_blood_pressure = int(request.form["resting_blood_pressure"])
        cholesterol = int(request.form["cholesterol"])  # Fixed naming issue
        fasting_blood_sugar = int(request.form["fasting_blood_sugar"])
        resting_electrocardiographic_results = int(request.form["resting_electrocardiographic_results"])
        max_heart_rate_achieved = int(request.form["max_heart_rate_achieved"])
        exercise_induced_angina = int(request.form["exercise_induced_angina"])
        st_depression = float(request.form["st_depression"])
        st_slope = int(request.form["st_slope"])
        number_of_major_vessels = int(request.form["number_of_major_vessels"])
        thalassemia = int(request.form["thalassemia"])

        # Create a feature list from user input
        features = [
            age, sex, chest_pain_type, resting_blood_pressure, cholesterol,
            fasting_blood_sugar, resting_electrocardiographic_results, max_heart_rate_achieved,
            exercise_induced_angina, st_depression, st_slope, number_of_major_vessels, thalassemia
        ]

        # Make prediction using the model
        prediction = predict_heart_disease(features)

        # Return a result message based on the prediction
        if prediction == 1:
            return "The model predicts heart disease."
        else:
            return "The model predicts no heart disease."

    except ValueError:
        return "Error: Please enter valid numerical values."
    except Exception as e:
        return f"Error: {str(e)}"




