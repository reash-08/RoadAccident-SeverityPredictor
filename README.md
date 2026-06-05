# 🚦 Road Accident Severity Predictor

## Project Overview

The Road Accident Severity Predictor is a Machine Learning and Flask-based web application developed to predict the severity of road accidents using historical UK Road Safety data.

The system analyzes accident-related factors such as weather conditions, road type, road surface conditions, lighting conditions, speed limits, vehicle information, and casualty information to classify accident severity into:

* Slight
* Serious
* Fatal

The project aims to support Smart City initiatives by providing data-driven insights that can help improve road safety, traffic planning, and accident prevention strategies.

---

# ✨ Features

### 📊 Exploratory Data Analysis (EDA)

* Dataset loading and inspection
* Missing value analysis
* Severity distribution analysis
* Weather condition analysis
* Road surface condition analysis
* Light condition analysis
* Urban vs Rural accident analysis
* Speed limit analysis
* Data visualization using Matplotlib and Seaborn

### 🤖 Machine Learning

* Data preprocessing and cleaning
* Missing value handling
* Label Encoding of categorical variables
* Feature selection
* Train-Test Split (80:20)
* Gradient Boosting Classifier
* Weighted F1-Score evaluation
* Model serialization using Joblib

### 🌐 Flask Web Application

* Interactive dashboard
* Real-time accident severity prediction
* Confidence score display
* Probability visualization
* Safety recommendations
* Reset functionality
* Responsive UI

---

# 📁 Dataset

### Dataset Used

UK Road Safety Accident Dataset

### Original Dataset

* Records: 2,047,256+
* Features: 34

### Training Dataset

* Sample Size: 50,000 records

### Features Used

* Road_Type
* Weather_Conditions
* Road_Surface_Conditions
* Light_Conditions
* Speed_limit
* Urban_or_Rural_Area
* Number_of_Vehicles
* Number_of_Casualties

### Target Variable

Accident_Severity

Classes:

* Slight
* Serious
* Fatal

---

# 🛠 Technology Stack

## Backend

* Python
* Flask

## Machine Learning

* Scikit-Learn
* Gradient Boosting Classifier
* Joblib

## Data Analysis

* Pandas
* NumPy
* Matplotlib
* Seaborn

## Frontend

* HTML
* CSS
* JavaScript

---

# 📈 Project Workflow

## M1 – Exploratory Data Analysis

### Tasks Completed

* Dataset loading
* Dataset shape analysis
* Missing value analysis
* Severity distribution analysis
* Weather condition analysis
* Road surface condition analysis
* Light condition analysis
* Urban/Rural area analysis
* Speed limit analysis
* Data visualization

### Generated Visualizations

* Accident Severity Distribution
* Weather vs Severity
* Road Surface vs Severity
* Light Conditions vs Severity
* Speed Limit vs Severity
* Urban/Rural Area vs Severity

---

## M2 – Model Training & Evaluation

### Data Preprocessing

* Missing value handling
* Feature selection
* Label Encoding
* Dataset preparation

### Model Training

Algorithm Used:

**Gradient Boosting Classifier**

### Model Performance

Training Samples: 40,000

Testing Samples: 10,000

Evaluation Metric:

**Weighted F1-Score**

Score:

**63.76%**

### Sample Predictions

Case 1: Slight

Case 2: Fatal

Case 3: Slight

### Saved Model Files

* severity_model.pkl
* encoders.pkl
* severity_encoder.pkl

---

## M3 – Flask Web Application

The dashboard allows users to enter accident-related information and instantly receive severity predictions.

### Input Features

* Road Type
* Weather Condition
* Road Surface Condition
* Light Condition
* Urban/Rural Area
* Speed Limit
* Number of Vehicles
* Number of Casualties

### Output

* Predicted Severity
* Confidence Percentage
* Safety Recommendation

### Dashboard Features

* Modern UI Design
* Real-Time Predictions
* Confidence Progress Bar
* Interactive Forms
* Responsive Layout
* Reset Functionality

---

# 📊 Model Performance

The dataset is highly imbalanced because Slight accidents occur much more frequently than Fatal accidents.

Therefore, **Weighted F1-Score** was used instead of simple accuracy.

| Metric            | Value                        |
| ----------------- | ---------------------------- |
| Weighted F1 Score | 63.76%                       |
| Algorithm         | Gradient Boosting Classifier |
| Training Samples  | 40,000                       |
| Testing Samples   | 10,000                       |

---

# 📂 Project Structure

```text
RoadAccident-SeverityPredictor/
│
├── Accident_Information.csv
├── accident_50k.csv
│
├── m1_eda.py
├── m2_training.py
├── predict.py
├── app.py
│
├── severity_model.pkl
├── encoders.pkl
├── severity_encoder.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── severity_distribution.png
├── weather_vs_severity.png
├── road_surface_vs_severity.png
├── light_conditions_vs_severity.png
├── speed_limit_vs_severity.png
├── urban_rural_vs_severity.png
│
├── README.md
└── requirements.txt
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/RoadAccident-SeverityPredictor.git
cd RoadAccident-SeverityPredictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train Model

```bash
python m2_training.py
```

### Run Test Predictions

```bash
python predict.py
```

### Start Flask Application

```bash
python app.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

---

# 📷 Sample Output

Example Prediction:

```text
Predicted Severity: Serious
Confidence: 38.64%
```

---

# 📌 Dataset Source

The original dataset is too large to host directly on GitHub.

Dataset:
UK Road Safety Accident Dataset (Kaggle)

Download the dataset and place:

```text
Accident_Information.csv
```

inside the project root directory before running the scripts.

---

# 🔮 Future Enhancements

* Real-time traffic data integration
* Weather API integration
* XGBoost and LightGBM models
* GIS-based accident hotspot visualization
* Interactive analytics dashboard
* Cloud deployment
* Smart city traffic management integration

---

# 👨‍💻 Author

Developed as a Smart City Machine Learning Project using the UK Road Safety Dataset.

Road Accident Severity Prediction using Machine Learning, Data Analytics, and Flask Web Development.
