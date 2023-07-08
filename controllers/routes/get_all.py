from database.connect import db
from bson.json_util import dumps
import json

sample_data_coll = db.sample_data


def get_all_vehicles():
    data = sample_data_coll.find(
        filter={},
        projection={
            "registration_number": 1,
            "brand": 1,
            "brand_id": 1,
            "model": 1,
            "location": 1,
            "kms_driven": 1,
            "ownership_status": 1,
            "age": 1,
            "power": 1,
            "_id": 0,
        },
    ).limit(500)
    data = json.loads(dumps(data))

    return {"success": True, "data": data}
