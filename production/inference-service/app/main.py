#!/usr/bin/python
'''
This script defines our service app with a single endpoint "/inference".
'''
from fastapi import FastAPI
from pydantic import  BaseModel

import os
import random

from utils.inference import predict

app = FastAPI()

# load model 
# model = load_model("/model/model.pth")
model = None # mock-up

int_to_label = {0: "A", 1: "B"}

class Input(BaseModel):
    text: str


def get_prediction(input: str):
    """Return prediction for `input`"""

    label_id, probability = predict(model, input)

    return {"prediction": int_to_label[label_id], 
            "probability": probability}

@app.post("/inference")
def inference(input: Input):
    pred = get_prediction(input.text)
    return pred