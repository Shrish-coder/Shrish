# PPT Points — Student Performance Prediction

10 slides. Each point can be written directly on the slide.

---

**Slide 1 — Title**

* Student Performance Prediction using Machine Learning
* B.Tech 2nd Year Mini Project
* Name, Roll No., Branch, Guide name

---

**Slide 2 — Problem Definition**

* We know a student is weak only after the result comes.
* Attendance, internal marks and study hours are known before the exam.
* Aim: predict PASS or FAIL of CSE111 in advance.
* Type of problem: Classification.

---

**Slide 3 — Technology and Algorithms**

* Python, Pandas, NumPy
* Matplotlib, Seaborn (graphs)
* Scikit-learn (models)
* Streamlit (web app)
* Algorithms: Logistic Regression and Decision Tree

---

**Slide 4 — Dataset**

* 1000 rows, 6 columns. After removing 5 duplicate StudentIDs → 995 students.
* Columns: StudentID, Attendance, Weekly Study Hours, CA Marks, MTH165 marks,
  CSE111 marks.
* No Pass/Fail column in the file, so we made it:
  CSE111 marks ≥ 80 → PASS, else FAIL.
* Why 80: the lowest marks are 59, so with 40 everybody would pass.
* Result: 750 Pass and 245 Fail.

---

**Slide 5 — Data Cleaning**

* Checked missing values — none.
* Removed 5 duplicate students.
* Renamed the columns to short names.
* Removed out-of-range values (like attendance > 100).
* Saved `clean_student_data.csv`.

---

**Slide 6 — EDA (put the heatmap here)**

* Correlation with result: MTH165 0.74, study hours 0.56, internal marks 0.25,
  attendance 0.05.
* Pass students study 8.9 hours/week, Fail students 5.3 hours/week.
* Attendance does not help here because all students already have 75%+ attendance.

---

**Slide 7 — Model Building**

* Scaling with StandardScaler (needed for Logistic Regression).
* Train-Test split 80% - 20% → 796 training and 199 testing students.
* Logistic Regression → gives probability using the sigmoid function.
* Decision Tree (max_depth = 4) → asks yes/no questions on the marks.

---

**Slide 8 — Results (put the comparison graph here)**

| Model | Accuracy |
|-------|----------|
| Logistic Regression | 98.99 % |
| Decision Tree | 96.48 % |

* Best model: Logistic Regression, saved as `student_model.pkl`.
* Accuracy is high because MTH165 and CSE111 marks are very similar (0.94).

---

**Slide 9 — Streamlit App (put a screenshot here)**

* Enter attendance, internal marks, study hours and MTH165 marks with sliders.
* Output: PASS/FAIL + probability + suggestions.
* Example: 85%, 23/30, 8 hours, 90% → PASS with 99% probability.

---

**Slide 10 — Conclusion and Future Work**

* The project completes all the steps: data → cleaning → EDA → models → app.
* Logistic Regression works best with 98.99% accuracy.
* Limitations: pass mark 80 is our own assumption, attendance did not help.
* Future: real college data, assignment marks, previous semester marks, Random Forest,
  and hosting the app online.
