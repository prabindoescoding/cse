from mailjet_rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

# To retrieving authentication detail


def sendMail(reciever, heading='Got mail from someone', subject="default body", messageBody='default message bdy'):
    api_key = os.getenv('key')
    api_secret = os.getenv('secret')
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "helloworldearth8@gmail.com",
                    "Name": heading
                },
                "To": [
                    {
                        "Email": reciever,
                        # "Name": "name"
                    }
                ],
                "Subject": subject,
                "TextPart": messageBody,
                # "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    # print(result.status_code)
    if str(result.status_code) == '200':
        return 'Mail sent sucessfull'
    else:
        return "Something went wrong try later"

    # print(result.json())
from _sqlite3 import *