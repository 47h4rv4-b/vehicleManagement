from typing import List
from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from fastapi import HTTPException
from fastapi.responses import JSONResponse
# from controllers.authentication.login import auth0_login
# from controllers.authentication.logout import auth0_logout
# from controllers.routes.add_vehicle import add_vehicle
# from controllers.routes.all_bikes import get_bikes
# from controllers.routes.delete_bike import delete_bike
# from controllers.routes.delete_file import delete_file
# from controllers.routes.edit_bike_data import edit_field
# from controllers.routes.fetch_all import fetch_vehicles

from models.models import (
    GetVehicle,
    # Login,
    AddVehicle,
    # VerifyNumber,
)
# from middleware.islogin import oauth2_scheme
from utilities.utils import *

app = FastAPI(
    title="Vehicle Information Database",
)

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
    # Add more origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")


# MISCELLANEOUS
@app.get("/", tags=["Default route"])
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# # AUTHENTICATION
# @app.post("/login", tags=["Authentication"])
# def login(login: Login):
#     return auth0_login(login.username, login.password)


# @app.get("/logout", tags=["Authentication"])
# def logout(token: List = Depends(oauth2_scheme)):
#     return auth0_logout(token[0])


# ROUTES
@app.post(
    "/add_vehicle",
    tags=["Vehicle details"],
    summary=["User can add a new bike in the database"],
)
# def attach_vehicle(
#     add_vehicle_model: AddVehicle,
#     token: List = Depends(oauth2_scheme),
# ):
#     return add_vehicle(add_vehicle_model)


@app.get(
    "/show_all",
    tags=["Vehicle details"],
    summary=["All the available bikes in the database will be displayed"],
)
# def show_all(token: List = Depends(oauth2_scheme)):
#     return fetch_vehicles()


@app.post(
    "/show_vehicle",
    tags=["Vehicle details"],
    summary=["All the details related to the selected bike will be displayed"],
)
# def show_one(get_vehicle_model: GetVehicle, token: List = Depends(oauth2_scheme)):
#     return fetch_vehicle(get_vehicle_model)


class BikeDetails(BaseModel):
    registration_number: str = Field(..., description="Registration number")
    bike_brand: str = Field(..., description="Brand name")
    bike_model: str = Field(..., description="Model name")
    ownership_status: str = Field(..., description="Bike owner")
    year: int = Field(..., description="Year of manufacture")
    location: str = Field(..., description="Location")
    kms_driven: int = Field(..., description="No. of kilometers driven")
    power: int = Field(..., description="Bike power")
    timestamp: int = Field(..., description="Current timestamp")

def get_dummy_data():
    dummy_data = [
    {
        "registration_number": "ABCD1234",
        "bike_brand": "Example Brand 1",
        "bike_model": "Example Model 1",
        "ownership_status": "Example Owner 1",
        "year": 2022,
        "location": "Example Location 1",
        "kms_driven": 5000,
        "power": 150,
        "timestamp": 1621375879,
    },
    {
        "registration_number": "EFGH5678",
        "bike_brand": "Example Brand 2",
        "bike_model": "Example Model 2",
        "ownership_status": "Example Owner 2",
        "year": 2021,
        "location": "Example Location 2",
        "kms_driven": 8000,
        "power": 200,
        "timestamp": 1621375890,
    },
    {
        "registration_number": "WXYZ9876",
        "bike_brand": "Example Brand 3",
        "bike_model": "Example Model 3",
        "ownership_status": "Example Owner 3",
        "year": 2020,
        "location": "Example Location 3",
        "kms_driven": 10000,
        "power": 180,
        "timestamp": 1621375901,
    },
    {
        "registration_number": "PQRS5432",
        "bike_brand": "Example Brand 4",
        "bike_model": "Example Model 4",
        "ownership_status": "Example Owner 4",
        "year": 2019,
        "location": "Example Location 4",
        "kms_driven": 12000,
        "power": 250,
        "timestamp": 1621375912,
    }
]

    return dummy_data



@app.get("/", tags=["Default route"])
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/get_bike_details", tags=["Vehicle details"])
def get_bike_details(bike_info: GetVehicle):
    registration_number = bike_info.registration_number
    bike_details = get_bike_details_from_database(registration_number)
    if bike_details is None:
        raise HTTPException(status_code=404, detail="Bike details not found")
    return JSONResponse(content=bike_details)


def get_bike_details_from_database(registration_number: str):
    dummy_data=get_dummy_data()
    for bike_details in dummy_data:
        if bike_details["registration_number"] == registration_number:
            # Convert datetime object to string representation
            bike_details["timestamp"] = str(bike_details["timestamp"])
            return bike_details
    return None



# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
