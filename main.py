from api_idealista import *
from data_manager import *

filters_param = {
    "operation": "rent",
    "propertyType": "homes",
    "center": "40.4404001917469,-3.7229795812848607",
    "distance": "6000",
    "maxPrice": "750"
}

flat_api = FlatAppManager(filters_param)
flat_data = flat_api.get_request()
DataManager.get_useful_data(flat_data)