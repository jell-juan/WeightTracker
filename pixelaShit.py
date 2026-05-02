#This handles all the pixela stuff
import requests
import dotenv
import datetime
import os


dotenv.load_dotenv()




#"""https://pixe.la/v1/users/fatboi123/graphs/graphweight.html"""



PIXELA_USERNAME=os.environ["PIXELA_USERNAME"]
PIXELA_TOKEN=os.environ["PIXELA_TOKEN"]


# params = {
#     "token" : TOKEN, 
#     "username" : USERNAME,
#     "agreeTermsOfService" : "yes",
#     "notMinor" : "yes"

# }

# answer = requests.post(url="https://pixe.la/v1/users", json=params)

GRAPHENDPOINT = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs"


graph_params = {
    "id" : "graphweight",
    "name" : "Weight",
    "unit" : "kg",
    "type" : "float",
    "color" : "momiji",
}

header = {
    "X-USER-TOKEN" : PIXELA_TOKEN,
}


# ans = requests.post(url= GRAPHENDPOINT, json=graph_params, headers=header)
# print(ans.text)


def sendData(data):
    global header
    weight = data[-1]["weight"]
    date = data[-1]["date"]

    date = datetime.datetime.strptime(date, r"%d/%m/%Y %H:%M:%S")
    formatted_date = datetime.datetime.strftime(date, r"%Y%m%d")



    PIXEL_ENDPOINT = F"{GRAPHENDPOINT}/{graph_params['id']}"
    
    params = {
        "quantity" : str(weight),
        "date" : formatted_date,
    }

    worked = False
    while worked == False:
        pixel = requests.post(url=PIXEL_ENDPOINT, json= params, headers= header)
        tmep = pixel.json()
        worked = not tmep.get("isRejected")

    if pixel.status_code == 200:
        return("Pixel was added successfully")
    else:
        print(pixel.text)

