#Step 1: Import Libraries
import pandas as pd
import numpy as np
import joblib
from pandas.api.types import is_numeric_dtype

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import f1_score, classification_report
from sklearn.utils.class_weight import compute_sample_weight

#Step 2: Load the 50K Dataset
df = pd.read_csv("accident_50k.csv")

print("Dataset Loaded Successfully")
print(df.shape)

#Step 3: Select Important Columns
selected_columns = [
    'Weather_Conditions',
    'Road_Surface_Conditions',
    'Light_Conditions',
    'Speed_limit',
    'Urban_or_Rural_Area',
    'Number_of_Vehicles',
    'Number_of_Casualties',
    'Accident_Severity'
]

df = df[selected_columns]

print(df.head())

#Step 4: Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

#Step 5: Handle Missing Values
for col in df.columns:
    if is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].median())
    else:
        mode = df[col].mode()
        fill_value = mode.iloc[0] if not mode.empty else "Unknown"
        df[col] = df[col].fillna(fill_value)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

#Step 6: Label Encode Features
encoders = {}

categorical_cols = [
    'Weather_Conditions',
    'Road_Surface_Conditions',
    'Light_Conditions',
    'Urban_or_Rural_Area'
]

for col in categorical_cols:

    le = LabelEncoder()

    df[col] = le.fit_transform(df[col])

    encoders[col] = le

#Step 7: Encode Target Variable
severity_encoder = LabelEncoder()

df['Accident_Severity'] = severity_encoder.fit_transform(
    df['Accident_Severity']
)

print("\nTarget Classes:")
print(severity_encoder.classes_)

#Step 8: Create Features and Target
X = df.drop('Accident_Severity', axis=1)

y = df['Accident_Severity']

print("\nFeature Shape:", X.shape)
print("Target Shape:", y.shape)

#Step 9: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

#Step 10: Create Balanced Sample Weights
sample_weights = compute_sample_weight(
    class_weight='balanced',
    y=y_train
)

print("Sample Weights Created")

#Step 11: Train Gradient Boosting Classifier
model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    random_state=42
)

model.fit(
    X_train,
    y_train,
    sample_weight=sample_weights
)

print("\nModel Training Complete")

#Step 12: Make Predictions
y_pred = model.predict(X_test)

#Step 13: Calculate Weighted F1 Score
weighted_f1 = f1_score(
    y_test,
    y_pred,
    average='weighted'
)

print("\nWeighted F1 Score:")
print(weighted_f1)

#Step 14: Classification Report
print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=severity_encoder.classes_
    )
)

#Step 15: Save the Model
joblib.dump(
    model,
    "severity_model.pkl"
)

print("Model Saved")

#Step 16: Save Encoders
joblib.dump(
    encoders,
    "encoders.pkl"
)

joblib.dump(
    severity_encoder,
    "severity_encoder.pkl"
)

print("Encoders Saved")

