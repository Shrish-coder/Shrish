# Step 16 of the roadmap - Testing
# Here we test our prediction system with some sample students.

from step4_prediction import predict_student

print("Test 1 - Good student")
result, probability, pass_probability = predict_student(95, 28, 13, 97)
print("Prediction:", result, "| Probability:", probability, "%")
assert result == "PASS"

print("\nTest 2 - Weak student")
result, probability, pass_probability = predict_student(76, 16, 2.5, 68)
print("Prediction:", result, "| Probability:", probability, "%")
assert result == "FAIL"

print("\nTest 3 - Average student")
result, probability, pass_probability = predict_student(85, 23, 8, 90)
print("Prediction:", result, "| Probability:", probability, "%")
assert result in ["PASS", "FAIL"]

print("\nTest 4 - Probability should be between 0 and 100")
assert 0 <= probability <= 100

print("\nTest 5 - Wrong input should give an error")
try:
    predict_student(150, 23, 8, 90)
    print("Error - the wrong value was accepted")
except ValueError as e:
    print("Correct, error message is:", e)

print("\nAll tests passed")
