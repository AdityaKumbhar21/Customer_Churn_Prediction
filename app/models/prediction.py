import joblib
import pandas as pd

MODEL_VERSION = '1.0.0'

with open(f'/Users/adityakumbhar/Developer/Customer_Churn_Prediction/app/models/churn_prediction_pipeline.joblib', 'rb') as f:
    loaded_model = joblib.load(f)


def predict_output(user_input: dict):
    df = pd.DataFrame([user_input])
    output = loaded_model.predict(df)[0]
    return output