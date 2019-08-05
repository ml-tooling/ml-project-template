#!/usr/bin/python
'''
This script defines our inference service app with a single endpoint "/inference".
The service is a mock-up sentiment analyser: input is a text, output is it's sentiment (pos/neg)
'''
from fastapi import FastAPI
from pydantic import  BaseModel

import os
import random

from utils.inference import predict

app = FastAPI()

# load model
# def load_model(path):
#     return Model(path)
# 
# model = load_model("/model/model.pth")

model = None # mock-up model

int_to_label = {0: "positive", 1: "negative"}

class Input(BaseModel):
    text: str


def get_prediction(input: str):
    """Return prediction for `input`"""

    label_id, probability = predict(model, input)
    return {"prediction": int_to_label[label_id], 
            "probability": probability}

@app.get("/")
def root():
    return {"message": "Not much here. Check out http://0.0.0.0:80/docs!"}    

@app.post("/inference")
def inference(input: Input):
    pred = get_prediction(input.text)
    return pred