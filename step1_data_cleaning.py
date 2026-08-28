# Step 4 of the roadmap - Data Cleaning
# Here we read the dataset, clean it and make the Pass/Fail column.

import pandas as pd

# read the dataset
df = pd.read_csv("student_data.csv")
print("Rows in the file:", df.shape[0])
print("Columns:", list(df.columns))
print(df.head())

# check missing values
print("\nMissing values:")
print(df.isnull().sum())

# remove duplicate students
print("\nDuplicate StudentID:", df.duplicated(subset="StudentID").sum())
df = df.drop_duplicates(subset="StudentID")

# give the columns short names so they are easy to use
df = df.rename(columns={
    "Attendance_Percentage": "attendance",
    "Weekly_Study_Hours": "study_hours",
    "CA_Marks": "internal_marks",
    "MTH165_Final_Grade": "mth165_marks",
    "CSE111_Final_Grade": "cse111_marks"
})

# fill missing values with the median of that column (if any)
for col in ["attendance", "study_hours", "internal_marks", "mth165_marks", "cse111_marks"]:
    df[col] = df[col].fillna(df[col].median())

# remove wrong values (example - attendance can never be more than 100)
df = df[(df["attendance"] >= 0) & (df["attendance"] <= 100)]
df = df[(df["internal_marks"] >= 0) & (df["internal_marks"] <= 30)]
df = df[(df["study_hours"] >= 0) & (df["study_hours"] <= 40)]

# The dataset does not have a Pass/Fail column, so we make it ourselves.
# A student passes CSE111 if the final marks are 80 or more.
df["result"] = 0
df.loc[df["cse111_marks"] >= 80, "result"] = 1

print("\nAfter cleaning:", df.shape[0], "students")
print("Pass students:", (df["result"] == 1).sum())
print("Fail students:", (df["result"] == 0).sum())

# save the clean file, we will use this file in the next steps
df.to_csv("clean_student_data.csv", index=False)
print("\nClean file saved as clean_student_data.csv")
