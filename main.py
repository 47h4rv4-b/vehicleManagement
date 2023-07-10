from typing import List
from fastapi import FastAPI, Depends, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from fastapi import HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from models.models import GetVehicle

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


# Add Vehicle Form
@app.post("/add_vehicle_form", response_class=HTMLResponse, tags=["Vehicle details"])
async def add_vehicle_form(request: Request):
    return templates.TemplateResponse("add_vehicle.html", {"request": request})


class AddVehicle(BaseModel):
    registration_number: str = Field(..., description="Registration number")
    bike_brand: str = Field(..., description="Brand name")
    bike_model: str = Field(..., description="Model name")
    ownership_status: str = Field(..., description="Bike owner")
    year: int = Field(..., description="Year of manufacture")
    location: str = Field(..., description="Location")
    kms_driven: int = Field(..., description="No. of kilometers driven")
    power: int = Field(..., description="Bike power")
    timestamp: int = Field(..., description="Current timestamp")


def validate_data(add_vehicle: AddVehicle):
    # Perform validation logic here
    if not add_vehicle.registration_number:
        raise HTTPException(status_code=400, detail="Registration number is required")

    # Add more validation rules as needed


@app.post("/add_vehicle", tags=["Vehicle details"])
def add_vehicle(
    registration_number: str = Form(...),
    bike_brand: str = Form(...),
    bike_model: str = Form(...),
    ownership_status: str = Form(...),
    year: int = Form(...),
    location: str = Form(...),
    kms_driven: int = Form(...),
    power: int = Form(...),
    timestamp: int = Form(...),
):
    # Perform validation logic here
    if not registration_number:
        raise HTTPException(status_code=400, detail="Registration number is required")

    # Create a new bike details dictionary
    new_bike = {
        "registration_number": registration_number,
        "bike_brand": bike_brand,
        "bike_model": bike_model,
        "ownership_status": ownership_status,
        "year": year,
        "location": location,
        "kms_driven": kms_driven,
        "power": power,
        "timestamp": timestamp,
    }

    # Add the new bike details to the bike_list
    bike_list.append(new_bike)

    return {"message": "Vehicle details added successfully"}




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


bike_list = get_dummy_data()


@app.post("/get_bike_details", tags=["Vehicle details"])
def get_bike_details(bike_info: GetVehicle):
    registration_number = bike_info.registration_number
    bike_details = get_bike_details_from_database(registration_number)

    if bike_details is None:
        raise HTTPException(status_code=404, detail="Bike details not found")

    return {"bike_details": bike_details}


def get_bike_details_from_database(registration_number: str):
    registration_number = registration_number.lower()  # Convert registration number to lowercase

    for bike_details in bike_list:
        if bike_details["registration_number"].lower() == registration_number:
            # Convert datetime object to string representation
            bike_details["timestamp"] = str(bike_details["timestamp"])
            return bike_details

    return None


# Run the app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
