# Step 14 of the roadmap - Prediction System
# This file takes the marks of one student and tells Pass or Fail.
# The Streamlit app also uses the predict_student function from this file.

import joblib
import pandas as pd


def predict_student(attendance, internal_marks, study_hours, mth165_marks):
    data = joblib.load("models/student_model.pkl")
    model = data["model"]

    # check that the values entered are correct
    if attendance < 0 or attendance > 100:
        raise ValueError("Attendance should be between 0 and 100")
    if internal_marks < 0 or internal_marks > 30:
        raise ValueError("Internal marks should be between 0 and 30")
    if study_hours < 0 or study_hours > 40:
        raise ValueError("Study hours should be between 0 and 40")
    if mth165_marks < 0 or mth165_marks > 100:
        raise ValueError("MTH165 marks should be between 0 and 100")

    student = pd.DataFrame([[attendance, internal_marks, study_hours, mth165_marks]],
                           columns=data["features"])

    # if the best model is Logistic Regression then we have to scale the values
    if data["uses_scaler"]:
        student_values = data["scaler"].transform(student)
    else:
        student_values = student

    prediction = model.predict(student_values)[0]
    pass_probability = model.predict_proba(student_values)[0][1]

    if prediction == 1:
        result = "PASS"
        probability = pass_probability
    else:
        result = "FAIL"
        probability = 1 - pass_probability

    return result, round(probability * 100, 2), round(pass_probability * 100, 2)


# this part runs only when we run this file directly
if __name__ == "__main__":
    print("Student Performance Prediction")
    attendance = float(input("Enter attendance (%): "))
    internal_marks = float(input("Enter internal / CA marks (out of 30): "))
    study_hours = float(input("Enter study hours per week: "))
    mth165_marks = float(input("Enter MTH165 marks (%): "))

    result, probability, pass_probability = predict_student(
        attendance, internal_marks, study_hours, mth165_marks)

    print("\nPrediction:", result)
    print("Probability:", probability, "%")
