from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from schema.user_input import UserInput
import pandas as pd
from models.prediction import predict_output, loaded_model, MODEL_VERSION


def classify_tenure(tenure_val):
    labels = ['0-19', '20-39','40-59','60-72']
    bins = [0,19,39, 59, 72]
    tenure_group_series = pd.cut(
        pd.Series([tenure_val]),
        bins=bins,
        labels=labels,
        include_lowest=True
    )
    return tenure_group_series.iloc[0]


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return {'Welcome'}



@app.post('/predict')
def predict(data: UserInput):
    input = {
        'tenure':data.tenure,
        'tenure_group':classify_tenure(data.tenure),
        'Contract':data.Contract,
        'InternetService':data.InternetService,
        'PaymentMethod':data.PaymentMethod,
        'MonthlyCharges':data.MonthlyCharges,
        'TotalCharges':data.TotalCharges,
        'OnlineBackup':  data.OnlineBackup
    }
    try:
        prediction = predict_output(input)
        return JSONResponse(status_code=200, content={'predicted_charges':round(prediction, 2)})
    
    except Exception as e:
        return JSONResponse(st)
