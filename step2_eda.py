# Step 5 of the roadmap - Data Analysis (EDA)
# In this file we study the data and save some graphs in the images folder.

import matplotlib
matplotlib.use("Agg")   # so that graphs get saved without opening a window

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("clean_student_data.csv")

features = ["attendance", "internal_marks", "study_hours", "mth165_marks"]

print("Total students:", len(df))
print("\nBasic details of the data:")
print(df[features].describe())

print("\nHow much each column is related to the result:")
print(df[features + ["result"]].corr()["result"].sort_values(ascending=False))

print("\nAverage values of Pass students and Fail students:")
print(df.groupby("result")[features].mean())

# Graph 1 - how many students passed and failed
sns.countplot(x="result", data=df)
plt.xticks([0, 1], ["Fail", "Pass"])
plt.title("Number of Pass and Fail students")
plt.savefig("images/pass_fail_count.png")
plt.close()

# Graph 2 - histogram of every feature
df[features].hist(figsize=(10, 8))
plt.suptitle("Distribution of the features")
plt.savefig("images/feature_histograms.png")
plt.close()

# Graph 3 - correlation heatmap
plt.figure(figsize=(7, 5))
sns.heatmap(df[features + ["result"]].corr(), annot=True, cmap="Blues")
plt.title("Correlation heatmap")
plt.tight_layout()
plt.savefig("images/correlation_heatmap.png")
plt.close()

# Graph 4 - box plot of study hours for pass and fail students
sns.boxplot(x="result", y="study_hours", data=df)
plt.xticks([0, 1], ["Fail", "Pass"])
plt.title("Study hours of Pass and Fail students")
plt.savefig("images/study_hours_boxplot.png")
plt.close()

print("\nAll graphs are saved in the images folder")
