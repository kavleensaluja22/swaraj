from django.urls import reverse
from twilio.rest import Client
import random
from .models import OTP

account_sid = 'AC1abd6b5767a3a8171f3ae628cf2a1fef'
auth_token = 'c987e6c19c60f6736442da61836c5e02'
client = Client(account_sid, auth_token)


def generate_otp():
    return random.randint(100000, 999999)


def send_otp(phone_number):
    try:
        otp = generate_otp()
        message = client.messages.create(
            body=f"SWARAJ TRACTOR HARYANA WELCOMES YOU ,Your OTP is {otp}", from_="+13157132751", to=phone_number
        )

        return otp , True
        
    except Exception as e:
        print(e)
    
    return '' , False