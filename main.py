from typing import List
from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
# from controllers.authentication.login import auth0_login
# from controllers.authentication.logout import auth0_logout
# from controllers.routes.add_vehicle import add_vehicle
# from controllers.routes.all_bikes import get_bikes
# from controllers.routes.delete_bike import delete_bike
# from controllers.routes.delete_file import delete_file
# from controllers.routes.edit_bike_data import edit_field
# from controllers.routes.fetch_all import fetch_vehicles
# from controllers.routes.fetch_initial_data import fetch_first_500
# from controllers.routes.fetch_one import fetch_vehicle
# from controllers.routes.fetch_brands import get_brands
# from controllers.routes.get_download_link import get_url
# from controllers.routes.verify_number import number_verification
from models.models import (
    DeleteFile,
    GetDownloadLink,
    GetVehicle,
    Login,
    AddVehicle,
    S3Upload,
    VerifyNumber,
)
from middleware.islogin import oauth2_scheme
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


# AUTHENTICATION
@app.post("/login", tags=["Authentication"])
def login(login: Login):
    return auth0_login(login.username, login.password)


@app.get("/logout", tags=["Authentication"])
def logout(token: List = Depends(oauth2_scheme)):
    return auth0_logout(token[0])


# ROUTES
@app.post(
    "/add_vehicle",
    tags=["Vehicle details"],
    summary=["User can add a new bike in the database"],
)
def attach_vehicle(
    add_vehicle_model: AddVehicle,
    token: List = Depends(oauth2_scheme),
):
    return add_vehicle(add_vehicle_model)


@app.get(
    "/show_all",
    tags=["Vehicle details"],
    summary=["All the available bikes in the database will be displayed"],
)
def show_all(token: List = Depends(oauth2_scheme)):
    return fetch_vehicles()


@app.post(
    "/show_vehicle",
    tags=["Vehicle details"],
    summary=["All the details related to the selected bike will be displayed"],
)
def show_one(get_vehicle_model: GetVehicle, token: List = Depends(oauth2_scheme)):
    return fetch_vehicle(get_vehicle_model)


# Model for bike details
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

    # Add other fields as needed


@app.get("/", tags=["Default route"])
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/get_bike_details", tags=["Vehicle details"])
def get_bike_details(bike_info: BikeDetails):
    # Perform database query or any other logic to get bike details based on registration number
    registration_number = bike_info.registration_number
    # Assuming you have a function to get bike details, update the logic below accordingly
    bike_details = get_bike_details_from_database(registration_number)
    return bike_details


def get_bike_details_from_database(registration_number: str):
    # Assuming you have a database connection and query to fetch bike details
    # Replace the code below with your actual database query logic
    bike_details = {
        "registration_number": registration_number,
        "bike_brand": "Example Brand",
        "bike_model": "Example Model",
        "ownership_status": "Example Owner",
        "year": 2022,
        "location": "Example Location",
        "kms_driven": 5000,
        "power": 150,
        "timestamp": 1621375879,
    }
    return bike_details

# Add more routes or functions as needed


# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
