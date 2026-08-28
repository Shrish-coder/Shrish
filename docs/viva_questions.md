# Viva Questions and Answers

Common questions that can be asked in the viva of this project.

---

**1. What is your project about?**
My project predicts whether a student will pass or fail the CSE111 subject using their
attendance, internal marks, weekly study hours and MTH165 marks. I used Logistic
Regression and Decision Tree, and made a Streamlit app for the prediction.

**2. Is it classification or regression?**
Classification, because the output is a category (Pass or Fail), not a number. If I had
predicted the marks, then it would be regression.

**3. What is supervised learning?**
In supervised learning we give the model both the input and the correct answer while
training. Here the input is the marks and attendance, and the answer is Pass or Fail.

**4. Which dataset did you use and how many records?**
The dataset given to us has 1000 rows. 5 rows had duplicate StudentIDs, so after cleaning
995 students are left.

**5. There is no Pass/Fail column in the dataset. How did you get the target?**
I made it myself from the CSE111 marks. If the marks are 80 or more, the student is Pass
(1), otherwise Fail (0).

**6. Why did you take 80 marks and not 40?**
Because the lowest marks in the dataset are 59. If I take 40, every student becomes Pass
and the model cannot learn anything, as there would be only one class.

**7. Why did you not use CSE111 marks as an input?**
Because the Pass/Fail column is made from the CSE111 marks itself. If I give it as an
input, the model will already know the answer and the accuracy will be 100%, which is
meaningless.

**8. What are features and target?**
Features are the input columns — attendance, internal marks, study hours and MTH165
marks. The target is the output column — result (Pass/Fail).

**9. What cleaning did you do?**
I checked the missing values, removed 5 duplicate students, renamed the columns to short
names, and removed the values which were out of range like attendance more than 100.

**10. What did you find in the EDA?**
Study hours and MTH165 marks are most related to the result. Pass students study around
9 hours a week and Fail students only 5 hours. Attendance did not make any difference
because every student in the file already has more than 75% attendance.

**11. What is correlation?**
It tells how strongly two columns are related. Its value goes from -1 to +1. Here MTH165
marks have a correlation of 0.74 with the result, which is the highest.

**12. Why did you do scaling?**
Because attendance is out of 100 and internal marks are out of 30. Logistic Regression
compares the numbers directly, so without scaling the bigger numbers get more importance.
I used StandardScaler.

**13. Does the Decision Tree need scaling?**
No. A tree only checks conditions like "study hours > 6", and this condition does not
change if we scale the values.

**14. What is train-test split and why 80-20?**
We train the model on one part of the data and test it on the other part which the model
has never seen. 80-20 is the common ratio. I used random_state=42 so that the split is
the same every time, and stratify so that the Pass-Fail ratio stays the same in both
parts.

**15. What is Logistic Regression?**
It is a classification algorithm. It calculates a value from the inputs and passes it
through the sigmoid function, which gives a probability between 0 and 1. If it is more
than 0.5, the prediction is Pass.

**16. What is a Decision Tree?**
It divides the data by asking yes/no questions on the features, like "are the MTH165
marks more than 88?", until it reaches a leaf which gives the answer.

**17. Why did you give max_depth = 4?**
To stop overfitting. If the tree grows fully, it remembers the training data and gives
poor results on the new data.

**18. What is overfitting?**
When the model learns the training data too well, including the noise, so it gives high
training accuracy but low testing accuracy.

**19. What is accuracy? What are precision and recall?**
Accuracy is the number of correct predictions out of the total predictions. Precision is
how many of the students we called Pass were really Pass. Recall is how many of the real
Pass students we found.

**20. What is a confusion matrix?**
It is a table showing correct and wrong predictions. My Logistic Regression matrix is
[[48, 1], [1, 149]] — 48 Fail and 149 Pass are correct, and only 2 students are wrong.

**21. Which model is better and why?**
Logistic Regression, with 98.99% accuracy against 96.48% of the Decision Tree. The Pass
and Fail groups in this data can be separated almost by a straight line, and that is
exactly what Logistic Regression does.

**22. Your accuracy is 99%. Is it not too high?**
Yes, and I have written the reason in my report. The MTH165 marks and CSE111 marks are
very similar in this dataset (correlation 0.94), so the model mostly looks at the MTH165
marks. If I remove that column, the accuracy comes down to around 85%.

**23. How did you save the model?**
Using joblib, in `models/student_model.pkl`. I saved the model, the scaler and the column
names together, because the app also needs the scaler to give the correct answer.

**24. What is Streamlit?**
It is a Python library to make a simple web app without HTML or CSS. I run it with the
command `streamlit run app.py`.

**25. How did you test the project?**
In `step5_testing.py` I checked a good student (gives PASS), a weak student (gives FAIL),
that the probability stays between 0 and 100, and that a wrong input like attendance 150
gives an error.

**26. What are the limitations of your project?**
The pass mark 80 is my own assumption and not the official college rule. The dataset does
not have assignment marks or previous semester marks. Attendance did not help because all
students have good attendance.

**27. What can you do in future?**
Use real college data, add assignment and previous semester marks, try Random Forest and
KNN, and host the app online so teachers can use it.
