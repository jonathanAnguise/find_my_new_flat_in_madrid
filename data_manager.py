class DataManager:
    def __init__(self, flat_json):
        self.flat_to_add = []
        self.list_added_flat_id = []
        self.flat_json = flat_json

    def get_useful_data(self):
        # TODO 3: Add an exception in case file has been deleted
        with open('./already_sent.txt', mode='r') as f:
            data = [int(property_code) for property_code in f.readlines()]
        for flat in self.flat_json['elementList']:
            if int(flat['propertyCode']) not in data:
                self.flat_to_add.append(flat)
                self.list_added_flat_id.append(int(flat['propertyCode']))

    def register_flat_id_to_avoid_duplicate(self):
        for flat_id in self.list_added_flat_id:
            with open(file="./already_sent.txt", mode='a') as f:
                f.write(f"{str(flat_id)}\n")
