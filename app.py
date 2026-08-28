# Step 15 of the roadmap - Streamlit UI
# Run this file with the command:  streamlit run app.py

import pandas as pd
import streamlit as st

from step4_prediction import predict_student

st.set_page_config(page_title="Student Performance Prediction", page_icon="🎓")

st.title("🎓 Student Performance Prediction")
st.write("This app predicts whether a student will PASS or FAIL the CSE111 subject.")
st.write("(A student is considered Pass if the final marks are 80 or more.)")

menu = st.sidebar.radio("Go to", ["Prediction", "Dataset", "Graphs"])

if menu == "Prediction":
    st.header("Enter the student details")

    attendance = st.slider("Attendance (%)", 0.0, 100.0, 85.0)
    internal_marks = st.slider("Internal / CA marks (out of 30)", 0.0, 30.0, 23.0)
    study_hours = st.slider("Study hours per week", 0.0, 40.0, 8.0)
    mth165_marks = st.slider("MTH165 marks (%)", 0.0, 100.0, 90.0)

    if st.button("Predict"):
        result, probability, pass_probability = predict_student(
            attendance, internal_marks, study_hours, mth165_marks)

        st.subheader("Result")
        if result == "PASS":
            st.success("Prediction: PASS")
        else:
            st.error("Prediction: FAIL")

        st.write("Probability:", probability, "%")
        st.progress(int(pass_probability))
        st.write("Chance of passing:", pass_probability, "%")

        # simple suggestions for the student
        if internal_marks < 20:
            st.warning("Internal marks are low, try to score more in CA.")
        if study_hours < 6:
            st.warning("Study hours are less, try to study at least 6 hours in a week.")
        if mth165_marks < 80:
            st.warning("MTH165 marks are low, work on the other subjects also.")

elif menu == "Dataset":
    st.header("Dataset used in the project")
    df = pd.read_csv("clean_student_data.csv")
    st.write("Total students:", len(df))
    st.write("Pass students:", int((df["result"] == 1).sum()))
    st.write("Fail students:", int((df["result"] == 0).sum()))
    st.dataframe(df.head(20))
    st.write("Basic details of the data:")
    st.dataframe(df.describe())

else:
    st.header("Graphs")
    st.image("images/pass_fail_count.png")
    st.image("images/correlation_heatmap.png")
    st.image("images/feature_histograms.png")
    st.image("images/study_hours_boxplot.png")
    st.image("images/model_comparison.png")
    st.image("images/decision_tree.png")
