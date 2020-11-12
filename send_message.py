
import os

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
FROM = os.getenv('TELEPHONE_NUMBER_FROM_TWILIO')
TO = os.getenv('YOUR_TELEPHONE_NUMBER')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def new_message(text):
    message = client.messages.create(
        body=str(text),  # текст сообщения
        from_=FROM,  # номер, который был получен
        to=TO,  # твой номер, на который придёт sms
        )
    return message.sid
