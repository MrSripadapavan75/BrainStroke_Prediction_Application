
from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained ML pipeline
model = joblib.load("brainstroke_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Please provide valid JSON input"}), 400

        required_features = [
            "gender",
            "age",
            "hypertension",
            "heart_disease",
            "ever_married",
            "work_type",
            "Residence_type",
            "avg_glucose_level",
            "bmi",
            "smoking_status"
        ]

        missing = [
            feature for feature in required_features
            if feature not in data
        ]

        if missing:
            return jsonify({
                "error": "Missing fields",
                "fields": missing
            }), 400

        new_person = pd.DataFrame([{
            "gender": data["gender"],
            "age": float(data["age"]),
            "hypertension": int(data["hypertension"]),
            "heart_disease": int(data["heart_disease"]),
            "ever_married": data["ever_married"],
            "work_type": data["work_type"],
            "Residence_type": data["Residence_type"],
            "avg_glucose_level": float(data["avg_glucose_level"]),
            "bmi": float(data["bmi"]),
            "smoking_status": data["smoking_status"]
        }])

        prediction = model.predict(new_person)

        result = (
            "Person is likely to have a stroke"
            if prediction[0] == 1
            else "Person is not likely to have a stroke"
        )

        return jsonify({
            "prediction": int(prediction[0]),
            "result": result
        })

    except (ValueError, TypeError):
        return jsonify({
            "error": "Invalid input values. Please check your data."
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
