from flask import Flask, request, jsonify
import joblib
import pandas as pd


app = Flask(__name__)

MODEL_PATH = "models/model.pkl"

model = joblib.load(MODEL_PATH)


@app.route("/health", methods=["GET"])
def health():
   return jsonify({"status": "ok"})


@app.route("/predict", methods=["POST"])
def predict():
  try:
    data = request.get_json()

    if data is None:
     return jsonify({"error": "Данные не переданы"}), 400

    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0]

    result = {"prediction": int(prediction),
              "prediction_text": "default" if prediction == 1 else "no_default",
              "probability_no_default": float(prediction_proba[0]),
              "probability_default": float(prediction_proba[1])}

    return jsonify(result)

  except Exception as e:
    return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
