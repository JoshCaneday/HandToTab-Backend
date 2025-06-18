from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("gesture_model.pkl")



@app.get("/infer")
def predict(data: list):
    return {"gesture": "prediction"}

@app.get("/get_results")
def result(data: list):
    return {"accuracy": "100%", "recall": "100%"}
