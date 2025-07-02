import joblib
import pandas as pd
from pathlib import Path

MODEL_VERSION = '1.0.0'


ROOT_DIR = Path(__file__).resolve().parent.parent.parent 
with open(f'{ROOT_DIR}/models/churn_prediction_pipeline.joblib', 'rb') as f:
    loaded_model = joblib.load(f)


def predict_output(user_input: dict):
    df = pd.DataFrame([user_input])
    output = loaded_model.predict(df)[0]
    return output