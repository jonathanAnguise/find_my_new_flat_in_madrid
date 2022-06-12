from api_idealista import *
from data_manager import *

filters_param = {
    "operation": "rent",
    "propertyType": "homes",
    "center": "40.4404001917469,-3.7229795812848607",
    "distance": "6000",
    "maxPrice": "750"
}


def write_in_report(flat):
    print(flat)
    # TODO 2.1: Load file report
    # TODO 2.2: Edit file report
    pass


flat_api = FlatAppManager(filters_param)
flat_data = flat_api.get_request()

data_management = DataManager(flat_data)
data_management.get_useful_data
data_management.register_flat_id_to_avoid_duplicate()
print(data_management.list_added_flat_id)
print(data_management.flat_to_add)
