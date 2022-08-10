from fastapi import FastAPI, Request

import pandas as pd 
import joblib

model = joblib.load('./model/model.pkl') # importando el modelo
app = FastAPI()

@app.post("/predict", status_code = 200)
async def root(request: Request):

    data = await request.json()

    df_pred = pd.DataFrame([data])

    prediction = model.predict_proba(df_pred)

    response = {"prob" : round(prediction[0][1],2)}

    return response