from fastapi import FastAPI, Request

import pandas as pd 
import joblib

model = joblib.load('./model/model.pkl')
app = FastAPI()

@app.post("/")
async def root(request: Request):

    data = await request.json()
    
    values = list(data.values())
    columns = list(data.keys())

    df_pred = pd.DataFrame([values], columns = columns)

    prediction = model.predict_proba(df_pred)

    response = {"prob" : round(prediction[0][1],2)}

    return response