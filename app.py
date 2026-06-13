from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import sqlite3

app = Flask(__name__)

# ==========================
# LOAD MODEL
# ==========================

package = joblib.load("road_accident_model_final.pkl")

model = package["model"]
encoders = package["encoders"]
severity_encoder = package["severity_encoder"]

DB_PATH = "database/accidents.db"


# ==========================
# DATABASE CONNECTION
# ==========================

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# ==========================
# ROUTES
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/history")
def history():

    import sqlite3

    conn = sqlite3.connect("database/accidents.db")

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM predictions
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    conn.close()

    return render_template(
        "history.html",
        records=records
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/model-info")
def model_info():
    return render_template("model_info.html")


@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


# ==========================
# PREDICT
# ==========================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        road_type = data["road_type"]
        weather = data["weather"]
        road = data["road"]
        light = data["light"]
        area = data["area"]

        speed = float(data["speed"])
        vehicles = int(data["vehicles"])
        casualties = int(data["casualties"])

        road_type_encoded = encoders[
            "Road_Type"
        ].transform([road_type])[0]

        weather_encoded = encoders[
            "Weather_Conditions"
        ].transform([weather])[0]

        road_encoded = encoders[
            "Road_Surface_Conditions"
        ].transform([road])[0]

        light_encoded = encoders[
            "Light_Conditions"
        ].transform([light])[0]

        area_encoded = encoders[
            "Urban_or_Rural_Area"
        ].transform([area])[0]

        input_data = pd.DataFrame(
            [[
                road_type_encoded,
                weather_encoded,
                road_encoded,
                light_encoded,
                speed,
                area_encoded,
                vehicles,
                casualties
            ]],
            columns=[
                "Road_Type",
                "Weather_Conditions",
                "Road_Surface_Conditions",
                "Light_Conditions",
                "Speed_limit",
                "Urban_or_Rural_Area",
                "Number_of_Vehicles",
                "Number_of_Casualties"
            ]
        )

        prediction = model.predict(input_data)

        probabilities = model.predict_proba(
            input_data
        )

        severity = severity_encoder.inverse_transform(
            prediction
        )[0]

        confidence = round(
            float(max(probabilities[0])) * 100,
            2
        )

        # ==========================
        # SAVE TO SQLITE
        # ==========================

        conn = get_db_connection()

        conn.execute(
            """
            INSERT INTO predictions
            (
                road_type,
                weather_conditions,
                road_surface_conditions,
                light_conditions,
                speed_limit,
                urban_or_rural_area,
                number_of_vehicles,
                number_of_casualties,
                prediction
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                road_type,
                weather,
                road,
                light,
                speed,
                area,
                vehicles,
                casualties,
                severity
            )
        )

        conn.commit()
        conn.close()

        # ==========================
        # UI COLORS
        # ==========================

        if severity == "Fatal":

            color = "#ff1744"

            recommendation = (
                "⚠ High Risk: Immediate emergency response recommended."
            )

        elif severity == "Serious":

            color = "#ff9100"

            recommendation = (
                "⚠ Moderate Risk: Medical and traffic assistance may be required."
            )

        else:

            color = "#00e676"

            recommendation = (
                "✓ Low Risk: Minor impact predicted."
            )

        return jsonify({

            "severity": severity,
            "confidence": confidence,
            "color": color,
            "recommendation": recommendation

        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)