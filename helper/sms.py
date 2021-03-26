from twilio.rest import Client
from helper import helper


def sendSMS(to, message):
    account_sid = helper.settings.TWILIO_SID
    auth_token = helper.settings.TWILIO_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message, from_='+918708254761', to="8607454820")
    print(message.sid)
    return True
