from enum import Enum
from typing import Dict, List
from fastapi import Query
from pydantic import BaseModel, Field, EmailStr

###########
# Login
###########
class Login(BaseModel):
    username: EmailStr = Field(..., description="Registered Email ID")
    password: str = Field(..., description="Password")


###########
# Add Vehicle
###########
class AddVehicle(BaseModel):
    # Required fields
    registration_number: str = Field(..., description="Registration number")
    bike_brand: str = Field(..., description="Brand name")
    bike_model: str = Field(..., description="Model name")
    ownership_status: str = Field(..., description="Bike owner")
    year: int = Field(..., description="Year of manufacture")
    location: str = Field(..., description="Location")
    kms_driven: int = Field(..., description="No. of kilometers driven")
    power: int = Field(..., description="Bike power")
    timestamp: int = Field(..., description="Current timestamp")

    # Optional fields
    age: int = Field(default=None, description="Bike age")
    manufactured_date: str = Field(default=None, description="Date of manufacture")
    dealer_id: str = Field(default=None, description="Dealer's id")
    dealership_name: str = Field(default=None, description="Dealer's id")
    purchase_date: str = Field(default=None, description="Date of purchase")
    color: str = Field(default=None, description="Color of bike")
    purchase_price: str = Field(default=None, description="Purchase price")
    source: str = Field(default=None, description="Source of bike")
    sale_date: str = Field(default=None, description="Date of sale")
    sale_price: int = Field(default=None, description="Selling price")
    financier: str = Field(default=None, description="Financier")
    refurbish_date: str = Field(default=None, description="Refurbished date")
    variant: str = Field(default=None, description="Variant of bike")
    part_description: str = Field(default=None, description="Part description")
    part_cost: int = Field(default=None, description="Part cost")
    labour_description: str = Field(default=None, description="Labour description")
    labour_amount: int = Field(default=None, description="Labour amount")
    total_amount: int = Field(default=None, description="Total amount")
    sub_source: str = Field(default=None, description="Sub source")
    delivery_date: str = Field(default=None, description="Date of delivery")
    audio_files_path: Dict = Field(
        default=None, description="List of path of all audio files"
    )
    video_files_path: List = Field(
        default=None, description="List of path of all video files"
    )

class DeleteFile(BaseModel):
    file_path: str = Query(..., description="File path in s3 bucket")

###########
# Get Vehicle
###########
class GetVehicle(BaseModel):
    registration_number: str = Field(..., description="Registration number")

###########
# Get Vehicle
###########
class GetVehicle(BaseModel):
    registration_number: str = Field(..., description="Registration number")


class Trigger(str, Enum):
    Audio = "Audio"
    Video = "Video"


###########
# S3 upload
###########
class S3Upload(BaseModel):
    filename: str = Field(..., description="Filenames")
    trigger: Trigger = Field(..., description="Audio or Video")
    timestamp: str = Field(..., description="Current timestamp")


###########
# Registration number verification
###########
class VerifyNumber(BaseModel):
    registration_number: str = Field(..., description="Registration number")


###########
# Get downlodable link
###########
class GetDownloadLink(BaseModel):
    registration_number: str = Field(..., description="Registration number")
    trigger: Trigger = Field(..., description="Audio or Video")
