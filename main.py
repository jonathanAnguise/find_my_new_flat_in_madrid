from api_idealista import *

filters_param = {
    "operation": "rent",
    "propertyType": "homes",
    "center": "40.123,-3.242",
    "distance": "10000"
}
new_request = FlatAppManager(filters_param).get_request()
print(new_request)
