import json


class DataManager:

    @staticmethod
    def get_useful_data(json_file):
        with open('./already_sent.json', mode='r') as f:
            try:
                data = json.loads(f)
            except:
                print("file empty, no need to check")
                data = {}
        # TODO 1: check if unique flat id is in data dictionnary
            # TODO 1.1: if flat id is in data dict, go for next one
            # TODO 1.2: else edit file report
            # TODO 1.3: And write flat it to data dict in order to don't have duplicate



