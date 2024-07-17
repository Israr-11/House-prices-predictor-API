from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load the trained model
model_path = 'machine_learning_model/house_prices_predictor_model_1.pkl'
model = joblib.load(model_path)

class PredictionRequest(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.post("/predict")
def predict(features: PredictionRequest):
    # Convert the features to a numpy array and reshape for the model
    try:
        features_array = np.array([[features.MedInc, features.HouseAge,
                                    features.AveRooms, features.AveBedrms,
                                    features.Population, features.AveOccup,
                                    features.Latitude, features.Longitude]]).reshape(1, -1)
        prediction = model.predict(features_array)
        
        # Assuming prediction is in hundreds of thousands of dollars
        predicted_value_in_dollars = prediction[0] * 100000
        
        return {
            "prediction": prediction[0],
            "predicted_value_in_dollars": f"${predicted_value_in_dollars:,.2f}"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Welcome to the House Prices Prediction API"}



#SAMPLE DATA
# MedInc: 8.3252 (Median income in block group)
# HouseAge: 41.0 (Median house age in block group)
# AveRooms: 6.984127 (Average number of rooms per household)
# AveBedrms: 1.023810 (Average number of bedrooms per household)
# Population: 322.0 (Block group population)
# AveOccup: 2.555556 (Average number of household members)
# Latitude: 37.88 (Block group latitude)
# Longitude: -122.23 (Block group longitude)


# {
#     "MedInc": 8.3,
#     "HouseAge": 41.0,
#     "AveRooms": 6.9,
#     "AveBedrms": 1,
#     "Population": 322.0,
#     "AveOccup": 2.5,
#     "Latitude": 37.88,
#     "Longitude": -122.23
# }



