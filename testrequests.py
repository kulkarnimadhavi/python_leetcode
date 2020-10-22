import json
import requests

#create a notification using the unique access code.
def create_notiification():
    body = json.dumps({
    "notification": "Hello World!",
    "accessCode": "amzn1.ask.account.AEQLEPVK227JLF3JJ4KO2KMFDGZ7MJXEBHFYWPFNDKZQHTGBYQDC4G5YSPO6B2FP54663U7NT724XGIIFE6UH4DOB3PK7M7TXYD2RN73LOPUXT5UMRHENMF57XD7FXNOHQB2J3NY7JXC2VW6PZMY4NXXTJU32N4H644LZZ4PWNT3DB4XRNYDBVKQOQ3GNU6TGVDEDAMZ2TMNTPQ"
    })
    requests.post(url = "https://api.notifymyecho.com/v1/NotifyMe", data = body)


#Verify the voice status whether it shows the notification status
def verify_notification():
 validate_voice_status(caller.riviera_utils, "Notification")


def cancel_notification():
 #can not cancel it using voice
    print("cant cancel it")


def verify_cancel_notiifcation():
 validate_voice_status(caller.riviera_utils, "IDLE")

 if __name__ == "__main__":
  create_notiification( )