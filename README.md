# House Prices Predictor API

This project is a machine learning model to predict house prices using the California housing dataset. The model is deployed as a REST API using FastAPI.

# Project Structure

1. machine_learning_model/house_prices_predictor_model_1.pkl: The trained machine learning model saved as a pickle file.
2. main.py: The FastAPI application script.
3. .gitignore: Git ignore file to exclude unnecessary files from the repository.
4. README.md: This readme file.

# Model Details
The model is a Linear Regression model trained on the California housing dataset. It predicts house prices based on features like the number of rooms, crime rate, etc.

# Dataset
The dataset used for training is the California housing dataset, which includes the following features:

1. MedInc: Median income in block group
2. HouseAge: Median house age in block group
3. AveRooms: Average number of rooms per household
4. AveBedrms: Average number of bedrooms per household
5. Population: Block group population
6. AveOccup: Average number of household members
7. Latitude: Block group latitude
9. Longitude: Block group longitude

# Running the API

## API Endpoints

1. URL: /predict
2. Method: POST
3. Request Body Sample:
{
    "MedInc": 8.3,
    "HouseAge": 41.0,
    "AveRooms": 6.9,
    "AveBedrms": 1,
    "Population": 322.0,
    "AveOccup": 2.5,
    "Latitude": 37.88,
    "Longitude": -122.23
}

## Prerequisites

Python 3.6+
FastAPI
Uvicorn
Joblib
Numpy
Pydantic

## Cloning this project and running
1. git clone <url> to clone this project
2. Create a virtual environment and activate it as
 **python3 -m venv venv
source venv/bin/activate**  # On Windows use `venv\Scripts\activate`
4. Install the required packages
**pip install fastapi uvicorn joblib numpy pydantic**
5. To start the API server, run:
**uvicorn main:app --reload**

![image](https://github.com/user-attachments/assets/9dabf18d-b822-4374-bddc-9895e483046a)




