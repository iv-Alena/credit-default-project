import joblib
import pandas as pd

def load_model(model_path="models/model.pkl"):
  # Загружает обученную модель из файла.
  model = joblib.load(model_path)
  return model

def make_prediction(data, model_path="models/model.pkl"):
  # Делает предсказание по данным клиента.

  model = load_model(model_path)

  if isinstance(data, dict):
    data = pd.DataFrame([data])

  prediction = model.predict(data)
  prediction_proba = model.predict_proba(data)

  return {"prediction": int(prediction[0]),
          "probability_no_default": float(prediction_proba[0][0]),
          "probability_default": float(prediction_proba[0][1])}
