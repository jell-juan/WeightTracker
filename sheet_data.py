import requests
import dotenv
import os

dotenv.load_dotenv()

#this file is responsible for getting latest data from the google sheet 

BEARER = f"Bearer {os.getenv("Bearer")}"

class DataManager:
    def __init__(self):
        self.bearer = BEARER
        self.header = {
            "Authorization" : self.bearer
        }
        self.url = os.getenv("ENDPOINT")


    def getData(self):
        answer = requests.get(url=self.url, headers=self.header)
        data = answer.json()
        return data
    