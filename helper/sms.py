from twilio.rest import Client
import requests
from django.conf import settings


def sendSMS(to, message):
    account_sid = settings.TWILIO_SID
    auth_token = settings.TWILIO_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message, from_="+918708254761", to="8607454820"
    )
    print(message.sid)
    return True


def sendTGMessage(bot_message, bot_chatID=settings.TG_PURHCASE_ID):
    send_text = (
        "https://api.telegram.org/bot"
        + settings.TG_BOT_TOKEN
        + "/sendMessage?chat_id="
        + bot_chatID
        + "&parse_mode=Markdown&text="
        + bot_message.replace("#", "@")
    )

    print(send_text)

    response = requests.get(send_text)
    return response.json()