from fastapi import FastAPI
import pickle
import sklearn

app = FastAPI()

def predict_result():
    pickled_model = pickle.load(open('model.pkl', 'rb'))

    si1 = [[0,0,0,0,0,0,0,0,0,0,0,0,2.0,1.30,103.0,106.0]]
    result = pickled_model.predict(si1)

    s = "Still trying to predict"

    if result[0] == 0:
        s = "Congrats! Thyroid Not Detected."
    else:
        s = "Sorry! It's Thyroid."

    return s


@app.get("/")
async def root():
    s = predict_result()
    return s
