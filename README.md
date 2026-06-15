# 🚦 Smart City Road Accident Severity Prediction System

## 📌 Project Overview

The Smart City Road Accident Severity Prediction System is a Machine Learning-powered web application developed to predict the severity of road accidents using historical UK Road Safety data.

The system analyzes accident-related factors such as weather conditions, road type, road surface conditions, lighting conditions, speed limits, vehicle information, and casualty information to classify accident severity into:

* 🟢 Slight
* 🟠 Serious
* 🔴 Fatal

The project supports Smart City initiatives by providing data-driven insights that can help improve road safety, traffic management, accident prevention strategies, and decision-making.

---

# 🎯 Objectives

* Predict accident severity using Machine Learning.
* Provide real-time accident severity assessment.
* Store prediction history in a database.
* Visualize accident insights through dashboards.
* Build a complete end-to-end AI-powered web application.

---

# ✨ Key Features

## 🤖 Machine Learning

* Gradient Boosting Classifier
* Multi-Class Severity Prediction
* Confidence Score Calculation
* Feature Encoding Pipeline
* Model Serialization using Joblib

## 🌐 Flask Web Application

* Real-Time Severity Prediction
* Confidence Percentage Display
* Safety Recommendations
* Responsive User Interface
* Interactive Dashboard

## 🗄️ Database Integration

* SQLite Database
* Automatic Prediction Storage
* Historical Prediction Records
* Prediction Search & Filtering

## 📈 Analytics Dashboard

* Confusion Matrix Visualization
* Model Performance Analysis
* Dataset Insights
* Evaluation Charts

## 📄 Additional Pages

* Home Dashboard
* Prediction History
* Analytics Dashboard
* Model Information
* About Project
* Contact Page

---

# 📂 Dataset Information

### Dataset Used

UK Road Safety Accident Dataset

### Dataset Statistics

* Original Records: 2,000,000+
* Training Dataset: 50,000 Records
* Features Available: 34+
* Features Used: 8

### Features Used For Prediction

* Road Type
* Weather Conditions
* Road Surface Conditions
* Light Conditions
* Speed Limit
* Urban or Rural Area
* Number of Vehicles
* Number of Casualties

### Target Variable

Accident Severity

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

## Database

* SQLite

## Data Analysis

* Pandas
* NumPy
* Matplotlib
* Seaborn

## Frontend

* HTML5
* CSS3
* JavaScript

---

# 📊 Project Workflow

User Input

↓

HTML Form

↓

Flask Backend

↓

Feature Encoding

↓

Gradient Boosting Model (.pkl)

↓

Severity Prediction

↓

Confidence Score Generation

↓

SQLite Database Storage

↓

History & Analytics Dashboard

---

# 📈 Project Development Stages

## M1 – Exploratory Data Analysis (EDA)

### Tasks Completed

* Dataset Loading
* Dataset Inspection
* Missing Value Analysis
* Severity Distribution Analysis
* Weather Condition Analysis
* Road Surface Analysis
* Light Condition Analysis
* Urban/Rural Area Analysis
* Speed Limit Analysis
* Data Visualization

### Visualizations Generated

* Accident Severity Distribution
* Weather vs Severity
* Road Surface vs Severity
* Light Conditions vs Severity
* Speed Limit vs Severity
* Urban/Rural Area vs Severity

---

## M2 – Machine Learning Model Development

### Data Preprocessing

* Missing Value Handling
* Feature Selection
* Label Encoding
* Train-Test Split (80:20)

### Model Training

Models Evaluated:

* Decision Tree Classifier
* Gradient Boosting Classifier

### Final Selected Model

✅ Gradient Boosting Classifier

### Model Performance

| Metric              | Value       |
| ------------------- | ----------- |
| Weighted F1 Score   | ~77.5%      |
| Training Samples    | 40,000      |
| Testing Samples     | 10,000      |
| Classification Type | Multi-Class |

---

## M3 – Flask Web Application & Deployment

### Functionalities Implemented

✅ Machine Learning Model Integration

✅ Real-Time Prediction

✅ Confidence Score Display

✅ SQLite Database Storage

✅ Prediction History Page

✅ Search & Filter Functionality

✅ Analytics Dashboard

✅ About Project Page

✅ Model Information Page

✅ Contact Page

✅ Responsive User Interface

---

# 📊 Model Performance

The dataset contains class imbalance because Slight accidents occur much more frequently than Fatal accidents.

Therefore, Weighted F1 Score was selected as the primary evaluation metric instead of simple accuracy.

| Metric              | Value                  |
| ------------------- | ---------------------- |
| Algorithm           | Gradient Boosting      |
| Weighted F1 Score   | ~77.5%                 |
| Classification Type | Multi-Class            |
| Classes             | Slight, Serious, Fatal |

---

# 📂 Project Structure

```text
RoadAccident-SeverityPredictor/

│
├── app.py
├── predict.py
├── accident_50k.csv
├── road_accident_model_final.pkl
├── accidents.db
│
├── templates/
│   ├── index.html
│   ├── history.html
│   ├── analytics.html
│   ├── model_info.html
│   ├── about.html
│   └── contact.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── charts/
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

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

# 📷 Application Modules

* Home Dashboard
* Severity Prediction System
* Prediction History
* Analytics Dashboard
* Model Information
* About Project
* Contact Page

---

# 🔮 Future Enhancements

* Live Traffic Data Integration
* Weather API Integration
* GPS-Based Risk Prediction
* Accident Hotspot Detection
* Interactive Maps & Heatmaps
* Mobile Application Support
* Cloud Deployment
* Smart City Traffic Management Integration

---

# 👨‍💻 Author

Developed as part of the Innolift Ventures Machine Learning Internship Program.

Project Title:
Smart City Road Accident Severity Prediction System

Built using Machine Learning, Data Analytics, Flask Web Development, and SQLite Database Integration.

---

# 📄 License

This project is developed for educational, research, and internship purposes.
