# Steps 6 to 13 of the roadmap
# Preprocessing, Train-Test Split, Logistic Regression, Decision Tree,
# Model Evaluation, Model Comparison, Selecting the best model and Saving it.

import joblib
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree

df = pd.read_csv("clean_student_data.csv")

features = ["attendance", "internal_marks", "study_hours", "mth165_marks"]

X = df[features]
y = df["result"]

# Step 7 - Train Test Split (80% for training and 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
print("Training students:", len(X_train))
print("Testing students:", len(X_test))

# Step 6 - Preprocessing (scaling the values so that all columns come in same range)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 8 - Logistic Regression
log_model = LogisticRegression()
log_model.fit(X_train_scaled, y_train)
log_pred = log_model.predict(X_test_scaled)
log_accuracy = accuracy_score(y_test, log_pred)

print("\n----- Logistic Regression -----")
print("Accuracy:", round(log_accuracy * 100, 2), "%")
print(classification_report(y_test, log_pred, target_names=["Fail", "Pass"]))
print("Confusion matrix:")
print(confusion_matrix(y_test, log_pred))

# Step 9 - Decision Tree
# max_depth is given so that the tree does not become too big (overfitting)
tree_model = DecisionTreeClassifier(max_depth=4, random_state=42)
tree_model.fit(X_train, y_train)     # tree does not need scaling
tree_pred = tree_model.predict(X_test)
tree_accuracy = accuracy_score(y_test, tree_pred)

print("\n----- Decision Tree -----")
print("Accuracy:", round(tree_accuracy * 100, 2), "%")
print(classification_report(y_test, tree_pred, target_names=["Fail", "Pass"]))
print("Confusion matrix:")
print(confusion_matrix(y_test, tree_pred))

# Step 11 - Model Comparison
print("\n----- Comparison -----")
print("Logistic Regression accuracy:", round(log_accuracy * 100, 2), "%")
print("Decision Tree accuracy      :", round(tree_accuracy * 100, 2), "%")

plt.bar(["Logistic Regression", "Decision Tree"], [log_accuracy, tree_accuracy],
        color=["skyblue", "orange"])
plt.ylabel("Accuracy")
plt.title("Model comparison")
plt.savefig("images/model_comparison.png")
plt.close()

# picture of the decision tree (helps to explain in the viva)
plt.figure(figsize=(16, 8))
plot_tree(tree_model, feature_names=features, class_names=["Fail", "Pass"], filled=True)
plt.savefig("images/decision_tree.png")
plt.close()

# Step 12 - Select the best model
if log_accuracy >= tree_accuracy:
    best_model = log_model
    best_name = "Logistic Regression"
    uses_scaler = True
else:
    best_model = tree_model
    best_name = "Decision Tree"
    uses_scaler = False

print("\nBest model is:", best_name)

# Step 13 - Save the trained model (we also save the scaler and the column names)
joblib.dump({"model": best_model, "scaler": scaler, "features": features,
             "name": best_name, "uses_scaler": uses_scaler},
            "models/student_model.pkl")
print("Model saved in models/student_model.pkl")
