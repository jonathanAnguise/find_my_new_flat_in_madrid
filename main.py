from api_idealista import *

filters_param = {
    "operation": "rent",
    "propertyType": "homes",
    "center": "40.4404001917469,-3.7229795812848607",
    "distance": "6000",
    "maxPrice": "750"
}
new_request = FlatAppManager(filters_param).get_request()
print(new_request)
