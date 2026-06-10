from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

package = joblib.load("road_accident_model_final.pkl")

model = package["model"]
encoders = package["encoders"]
severity_encoder = package["severity_encoder"]


@app.route("/")
def home():
    return render_template("index.html")


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

        road_type_encoded = encoders["Road_Type"].transform(
            [road_type]
        )[0]

        weather_encoded = encoders["Weather_Conditions"].transform(
            [weather]
        )[0]

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

        probabilities = model.predict_proba(input_data)

        severity = severity_encoder.inverse_transform(
            prediction
        )[0]

        confidence = round(
            float(max(probabilities[0])) * 100,
            2
        )

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