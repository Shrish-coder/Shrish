# Student Performance Prediction — Project Report

B.Tech 2nd Year Mini Project

---

## 1. Problem Definition

In college, we come to know that a student is weak only after the final exam result
comes out. But things like attendance, internal (CA) marks and study hours are already
known before the exam.

So in this project we make a machine learning model which tells in advance whether a
student will **Pass** or **Fail** the CSE111 subject. This is a **classification**
problem because the answer is Pass or Fail and not a number.

**Input (features):** attendance, internal marks (out of 30), weekly study hours,
MTH165 marks.

**Output:** PASS or FAIL with the probability.

---

## 2 & 3. Dataset and Data Collection

The dataset `student_data.csv` was given for the project. It has 1000 rows and these
columns:

StudentID, Attendance_Percentage, Weekly_Study_Hours, CA_Marks, MTH165_Final_Grade,
CSE111_Final_Grade.

The dataset **does not have a Pass/Fail column**, so we made it from the CSE111 marks:

```
result = 1 (PASS)  if CSE111_Final_Grade >= 80
result = 0 (FAIL)  if CSE111_Final_Grade < 80
```

We first tried 40 marks as the pass mark, but the lowest marks in the file are 59, so
all the 995 students became Pass and the model had nothing to learn. That is why we
took 80 marks. Now we get 750 Pass students and 245 Fail students.

The CSE111 marks are used only to make the Pass/Fail column. They are **not** used as an
input feature, otherwise the model would already know the answer.

---

## 4. Data Cleaning

File: `step1_data_cleaning.py`

1. Checked the missing values with `isnull().sum()` — there were no missing values.
2. Found 5 rows with the same StudentID and removed them, so 1000 rows became
   **995 rows**.
3. Changed the long column names into short names (`attendance`, `internal_marks`,
   `study_hours`, `mth165_marks`, `cse111_marks`).
4. Wrote code to fill missing values with the median and to remove wrong values like
   attendance more than 100. (Our file was already correct, but this code will work if
   the data is dirty.)
5. Made the `result` column (Pass/Fail).

The clean data is saved as `clean_student_data.csv`.

---

## 5. Data Analysis (EDA)

File: `step2_eda.py`

Relation of each column with the result:

| Column | Correlation with result |
|--------|------------------------|
| MTH165 marks | 0.74 |
| Study hours | 0.56 |
| Internal marks | 0.25 |
| Attendance | 0.05 |

Average values:

| | Attendance | Internal marks | Study hours | MTH165 marks |
|---|---|---|---|---|
| Fail students | 84.5 | 20.6 | 5.3 | 81.2 |
| Pass students | 85.2 | 23.2 | 8.9 | 93.3 |

Points we noticed:

* Study hours make a big difference — Pass students study almost 9 hours in a week and
  Fail students only 5 hours.
* MTH165 marks have the highest relation with the result. It means a student who is good
  in one subject is normally good in the other subject also.
* Attendance is almost the same for both the groups. The reason is that in this dataset
  every student already has more than 75% attendance, so there is no difference to learn.

Graphs saved in the `images` folder: `pass_fail_count.png`, `feature_histograms.png`,
`correlation_heatmap.png`, `study_hours_boxplot.png`.

---

## 6. Data Preprocessing

All the columns are numbers, so we only did **scaling** using `StandardScaler`.
Scaling is needed because attendance is out of 100 and internal marks are out of 30, and
Logistic Regression gives wrong importance if the ranges are different.

The Decision Tree does not need scaling because it only checks conditions like
"study_hours > 6", so we gave it the normal data.

---

## 7. Train-Test Split

We divided the data into 80% training and 20% testing using `train_test_split` with
`random_state=42` (so that we get the same result every time) and `stratify=y` (so that
the Pass and Fail ratio remains the same in both parts).

* Training students: 796
* Testing students: 199

---

## 8. Logistic Regression

Logistic Regression draws a line between the two classes and gives the probability of
passing using the sigmoid function. If the probability is more than 0.5, it says PASS.

---

## 9. Decision Tree

The Decision Tree asks questions like "are the MTH165 marks more than 88?" and keeps
dividing the data until it reaches the answer. We used `max_depth=4` so that the tree
does not become too big and overfit.

The picture of the tree is saved in `images/decision_tree.png`.

---

## 10. Model Evaluation

Logistic Regression:

| | precision | recall | f1-score |
|---|---|---|---|
| Fail | 0.98 | 0.98 | 0.98 |
| Pass | 0.99 | 0.99 | 0.99 |

Confusion matrix `[[48, 1], [1, 149]]` — only 2 students out of 199 were predicted
wrongly.

Decision Tree:

| | precision | recall | f1-score |
|---|---|---|---|
| Fail | 0.92 | 0.94 | 0.93 |
| Pass | 0.98 | 0.97 | 0.98 |

Confusion matrix `[[46, 3], [4, 146]]` — 7 students were predicted wrongly.

---

## 11. Model Comparison

| Model | Accuracy |
|-------|----------|
| Logistic Regression | 98.99 % |
| Decision Tree | 96.48 % |

Graph: `images/model_comparison.png`

Logistic Regression is better here because the difference between Pass and Fail students
is almost like a straight line, and a straight line is exactly what Logistic Regression
draws.

**One important point:** the accuracy is very high because the MTH165 marks and the
CSE111 marks are very similar in this dataset (relation 0.94). So the model is mostly
looking at the MTH165 marks. If we remove the MTH165 column and use only attendance,
internal marks and study hours, the accuracy comes down to about 85%.

---

## 12 & 13. Best Model and Saving

Logistic Regression got more accuracy, so it is selected. It is saved with the scaler and
the column names using `joblib` in `models/student_model.pkl`.

---

## 14. Prediction System

File: `step4_prediction.py`

The function `predict_student()` takes the four values, checks that they are correct
(for example attendance cannot be 150), scales them, and returns PASS or FAIL with the
probability. The same function is used by the Streamlit app, so both give the same
answer.

---

## 15. Streamlit UI

File: `app.py`

The app has three pages in the sidebar:

* **Prediction** — sliders to enter the details and a Predict button. It shows PASS in
  green or FAIL in red with the probability, and also gives suggestions like "study hours
  are less".
* **Dataset** — shows the clean data and the basic details.
* **Graphs** — shows all the graphs made in the EDA and training steps.

---

## 16. Testing

File: `step5_testing.py`

| Test | Result |
|------|--------|
| Good student (95%, 28/30, 13 hours, 97%) | PASS ✔ |
| Weak student (76%, 16/30, 2.5 hours, 68%) | FAIL ✔ |
| Average student | works ✔ |
| Probability between 0 and 100 | ✔ |
| Wrong input (attendance 150) | gives an error ✔ |

---

## 17. Final Improvements

* Added checking of wrong inputs in the prediction system.
* Added suggestions in the app so the student knows what to improve.
* Saved the scaler along with the model, otherwise the app gives wrong answers.
* Used `random_state=42` everywhere so that the result does not change every time.

---

## 18. Documentation

`README.md`, this report, the PPT points (`presentation_outline.md`) and the viva
questions (`viva_questions.md`).

---

## Conclusion

We made a complete machine learning project which predicts whether a student will pass
CSE111. Logistic Regression gave 98.99% accuracy and the Decision Tree gave 96.48%, so
Logistic Regression was selected and used in the Streamlit app.

Limitations: the pass mark 80 is decided by us, and the attendance column did not help
because all students in the file have good attendance.

In future we can use real college data, add assignment marks and previous semester marks,
and try other algorithms like Random Forest.
