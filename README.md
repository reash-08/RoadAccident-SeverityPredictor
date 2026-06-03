# Road Accident Severity Predictor 🚗⚠️

## Project Overview

The Road Accident Severity Predictor is a machine learning-based web application developed to predict the severity of road accidents using historical UK Road Safety data. The system analyzes accident-related factors such as weather conditions, road surface conditions, lighting conditions, speed limits, and vehicle information to classify accident severity into:

* Slight
* Serious
* Fatal

The project aims to support smart city initiatives by providing data-driven insights that can help improve road safety and accident prevention strategies.

---

## Features

* Exploratory Data Analysis (EDA) on UK Road Safety Dataset
* Data preprocessing and handling of missing values
* Label Encoding of categorical variables
* Accident severity prediction using Gradient Boosting Classifier
* Weighted F1-Score evaluation for imbalanced data
* Probability-based severity prediction
* Flask-based web interface
* Model serialization using Pickle (.pkl)
* Smart City road safety application

---

## Dataset

Dataset: UK Road Safety Accident Dataset

The dataset contains accident-related information including:

* Weather Conditions
* Road Surface Conditions
* Light Conditions
* Speed Limit
* Number of Vehicles
* Number of Casualties
* Urban/Rural Area
* Accident Severity

Original dataset contains over 2 million accident records.

For model training, a sample of 50,000 records is used as specified in the project requirements.

---

## Technology Stack

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* Gradient Boosting Classifier

### Data Analysis

* Pandas
* NumPy
* Matplotlib
* Seaborn

### Frontend

* HTML
* CSS
* JavaScript

### Database

* SQLite

---

## Project Workflow

### M1: Data Analysis

* Load UK Road Safety dataset
* Null value analysis
* Weather condition analysis
* Road condition analysis
* Severity distribution analysis

### M2: Model Training

* Label Encoding
* Feature Selection
* Gradient Boosting Classification
* Weighted F1-Score Evaluation
* Save model and encoders using Pickle

### M3: Web Application

User enters:

* Weather Condition
* Road Surface Condition
* Light Condition
* Speed Limit
* Driver/Road Factors

Output:

* Predicted Severity
* Prediction Probability

### M4: Deployment

* Flask deployment
* Live prediction service
* Demo presentation

---

## Model Performance

Evaluation Metric:

* Weighted F1-Score

Reason:
The dataset is highly imbalanced, with Slight accidents occurring much more frequently than Fatal accidents. Weighted F1-Score provides a more reliable evaluation than accuracy.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/RoadAccident-SeverityPredictor.git
cd RoadAccident-SeverityPredictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Repository Structure

```text
RoadAccident-SeverityPredictor/
│
├── accident_50k.csv
├── train_model.py
├── app.py
├── severity_model.pkl
├── encoders.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## Future Enhancements

* Integration with real-time traffic data
* Advanced ensemble models (XGBoost, LightGBM)
* Interactive dashboard for accident analytics
* GIS-based accident hotspot visualization
* Smart city traffic management integration

---

## Author

Developed as a Smart City Machine Learning Project using the UK Road Safety Dataset.
