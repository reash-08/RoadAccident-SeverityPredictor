import pandas as pd
import numpy as np
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, f1_score
from sklearn.utils.class_weight import compute_sample_weight

# ==========================================
# STEP 1: LOAD DATASET
# ==========================================

df = pd.read_csv("accident_50k.csv")

print("Dataset Loaded Successfully")
print(df.shape)

# ==========================================
# STEP 2: SELECT REQUIRED COLUMNS
# ==========================================

df = df[
    [
        "Road_Type",
        "Weather_Conditions",
        "Road_Surface_Conditions",
        "Light_Conditions",
        "Speed_limit",
        "Urban_or_Rural_Area",
        "Number_of_Vehicles",
        "Number_of_Casualties",
        "Accident_Severity",
    ]
]

print(df.head())

# ==========================================
# STEP 3: CHECK MISSING VALUES
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================================
# STEP 4: HANDLE MISSING VALUES
# ==========================================

categorical_columns = [
    "Road_Type",
    "Weather_Conditions",
    "Road_Surface_Conditions",
    "Light_Conditions",
    "Urban_or_Rural_Area",
]

for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

df["Speed_limit"] = df["Speed_limit"].fillna(
    df["Speed_limit"].median()
)

df["Number_of_Vehicles"] = df["Number_of_Vehicles"].fillna(
    df["Number_of_Vehicles"].median()
)

df["Number_of_Casualties"] = df["Number_of_Casualties"].fillna(
    df["Number_of_Casualties"].median()
)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ==========================================
# STEP 5: LABEL ENCODE FEATURES
# ==========================================

encoders = {}

for col in categorical_columns:

    encoder = LabelEncoder()

    df[col] = encoder.fit_transform(df[col])

    encoders[col] = encoder

# ==========================================
# STEP 6: ENCODE TARGET
# ==========================================

severity_encoder = LabelEncoder()

df["Accident_Severity"] = severity_encoder.fit_transform(
    df["Accident_Severity"]
)

print("\nTarget Classes:")
print(severity_encoder.classes_)

# ==========================================
# STEP 7: FEATURES & TARGET
# ==========================================

X = df[
    [
        "Road_Type",
        "Weather_Conditions",
        "Road_Surface_Conditions",
        "Light_Conditions",
        "Speed_limit",
        "Urban_or_Rural_Area",
        "Number_of_Vehicles",
        "Number_of_Casualties",
    ]
]

y = df["Accident_Severity"]

print("\nFeature Shape:", X.shape)
print("Target Shape:", y.shape)

# ==========================================
# STEP 8: TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# ==========================================
# STEP 9: BALANCE CLASSES
# ==========================================

sample_weights = compute_sample_weight(
    class_weight="balanced",
    y=y_train
)

print("Sample Weights Created")

# ==========================================
# STEP 10: TRAIN MODEL
# ==========================================

model = GradientBoostingClassifier(
    random_state=42
)

model.fit(
    X_train,
    y_train,
    sample_weight=sample_weights
)

print("\nModel Training Complete")

# ==========================================
# STEP 11: PREDICTION
# ==========================================

y_pred = model.predict(X_test)

# ==========================================
# STEP 12: EVALUATION
# ==========================================

weighted_f1 = f1_score(
    y_test,
    y_pred,
    average="weighted"
)

print("\nWeighted F1 Score:")
print(weighted_f1)

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=severity_encoder.classes_
    )
)

# ==========================================
# STEP 13: SAVE MODEL
# ==========================================

joblib.dump(
    model,
    "severity_model.pkl"
)

joblib.dump(
    encoders,
    "encoders.pkl"
)

joblib.dump(
    severity_encoder,
    "severity_encoder.pkl"
)

print("\nModel Saved Successfully")
print("Encoders Saved Successfully")

import joblib

encoders = joblib.load("encoders.pkl")

for col, enc in encoders.items():
    print("\n", col)
    print(enc.classes_)