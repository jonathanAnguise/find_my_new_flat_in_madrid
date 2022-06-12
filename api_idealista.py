import requests
import os
import base64
import json
from dotenv import load_dotenv

project_folder = os.path.expanduser('.')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

# Oauth token part
APIKEY = os.getenv("APIKEY")
SECRET = os.getenv("SECRET")
AUTH_URL = "https://api.idealista.com/oauth/token"
base64_credential = str(base64.b64encode(f"{APIKEY}:{SECRET}".encode("utf-8")), "utf-8")
auth_header = f"Basic {base64_credential}"

END_POINT = "https://api.idealista.com/3.5/es/search"

debug_mode = True


def get_new_token():
    header = {
        "Authorization": auth_header,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    param = {
        "grant_type": "client_credentials"
    }

    token_response = requests.post(AUTH_URL, headers=header, params=param)
    return token_response.json()


token = get_new_token()
api_call_headers = {'Authorization': f"Bearer {token['access_token']}"}


class FlatAppManager:

    def __init__(self, parameters):
        self.api_call_response = {}
        self.param = parameters

    def get_request(self):
        if debug_mode:
            print("debug mode")
            # Try to limit request and work with local jsonfile (./request_answer.json)
            with open("./request_answer.json") as f:
                self.api_call_response = json.load(f)
        else:
            self.api_call_response = requests.post(END_POINT, headers=api_call_headers, params=self.param).json()
        return self.api_call_response
