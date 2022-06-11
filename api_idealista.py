import requests
from dotenv import load_dotenv
import os, base64, json

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
   print(token_response.json())
   return token_response.json()

token = get_new_token()

param = {
    "operation": "rent",
    "propertyType": "homes",
    "center": "40.123,-3.242",
    "distance": "10000"
}
api_call_headers = {'Authorization': f"Bearer {token['access_token']}"}
# Try to limit request and work with local jsonfile (./request_answer.json)
if debug_mode:
    api_call_response = requests.post(END_POINT, headers=api_call_headers, params=param)

print(api_call_response.json())
print(api_call_response.text)

# #TODO 2: Create a class
# class flatAppManager:
#
#     def __init__(self):
#         self.answer_dict = {}
# #TODO 2.1: Class has json has property
