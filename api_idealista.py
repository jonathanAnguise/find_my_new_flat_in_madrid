import requests
#TODO 1: load .env date
from dotenv import load_dotenv
import os

project_folder = os.path.expanduser('.')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

APIKEY = os.getenv("APIKEY")
SECRET = os.getenv("SECRET")

#TODO 2: Create a class
#TODO 2.1: Class has json has property

#To set in .env file when it's working well
END_POINT = ""