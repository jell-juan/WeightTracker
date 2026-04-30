from sheet_data import DataManager
from pixelaShit import sendData

dm = DataManager()
data = dm.getData()
final_data = data["weightTracker"]

sendData(data= final_data)
