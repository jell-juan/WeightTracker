from sheet_data import DataManager
from pixelaShit import sendData
from NotificationsManager import notification

dm = DataManager()
data = dm.getData()
final_data = data["weightTracker"]

result = sendData(data= final_data)

nm = notification(text=result)
nm.sendMessage()