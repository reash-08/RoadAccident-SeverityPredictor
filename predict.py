import pandas as pd
import joblib

model = joblib.load("severity_model.pkl")
encoders = joblib.load("encoders.pkl")
severity_encoder = joblib.load("severity_encoder.pkl")

feature_columns = [
    "Road_Type",
    "Weather_Conditions",
    "Road_Surface_Conditions",
    "Light_Conditions",
    "Speed_limit",
    "Urban_or_Rural_Area",
    "Number_of_Vehicles",
    "Number_of_Casualties",
]

cases = pd.DataFrame([
    [3, 2, 1, 5, 30, 2, 2, 1],   # Case 1
    [0, 6, 5, 3, 70, 0, 4, 3],   # Case 2
    [2, 3, 0, 1, 40, 2, 1, 1]    # Case 3
], columns=feature_columns)

# If input values are raw category labels instead of already encoded numbers,
# encode the categorical columns before prediction.
categorical_columns = [
    "Road_Type",
    "Weather_Conditions",
    "Road_Surface_Conditions",
    "Light_Conditions",
    "Urban_or_Rural_Area",
]

for col in categorical_columns:
    if cases[col].dtype == object:
        cases[col] = cases[col].apply(lambda x: encoders[col].transform([x])[0])

predictions = model.predict(cases[feature_columns])

for i, p in enumerate(predictions):
    severity = severity_encoder.inverse_transform([p])[0]
    print(f"Case {i+1}: {severity}")