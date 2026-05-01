from twilio.rest import Client
import os
import dotenv

dotenv.load_dotenv()


class notification:
    def __init__(self, text):
        self.from_num = os.getenv("FROM_NUM")
        self.to_num = os.getenv("TO_NUM")
        self.text = text
        self.sid = os.getenv("SID")
        self.auth = os.getenv("TWI_AUTH")


    def sendMessage(self):
        client = Client(self.sid, self.auth)

        client.messages.create(
            to=self.to_num,
            from_= self.from_num,
            body=self.text
        )

