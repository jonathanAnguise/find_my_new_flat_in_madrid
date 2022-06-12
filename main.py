from api_idealista import *
from data_manager import *

REPORT_FILE_NAME = "./flat_report.md"

filters_param = {
    "operation": "rent",
    "propertyType": "homes",
    "center": "40.4404001917469,-3.7229795812848607",
    "distance": "6000",
    "maxPrice": "750"
}


def write_in_report(flat_list):
    for flat in flat_list:
        with open(file=REPORT_FILE_NAME, mode='a') as f:
            # MarkDown table report format:
            # Direction|price|size|link|Comment|
            flat_info_formatted = f"{flat['neighborhood']} - {flat['district']}|{flat['price']}€|" \
                                 f"{flat['size']}m²||{flat['url']}|" \
                                 f"To contact\n"
            f.write(flat_info_formatted)


# Catch flat information
flat_api = FlatAppManager(filters_param)
flat_data = flat_api.get_request()

# manage flat information
data_management = DataManager(flat_data)
data_management.get_useful_data()
data_management.register_flat_id_to_avoid_duplicate()

# generate report
write_in_report(data_management.flat_to_add)
