import random

def predict(model=None, text: str = "text input"):
    prediction = random.randint(0, 2) - 1
    probability = random.random()
    return prediction, probability