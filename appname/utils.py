from django.urls import reverse
from twilio.rest import Client
import random
from .models import OTP

account_sid = 'AC2dd2d7696a8b5c24627cbe7807030029'
auth_token = '2f92b57e0f63522bb6cd3be1e1bced21'
client = Client(account_sid, auth_token)


def generate_otp():
    return random.randint(100000, 999999)


def send_otp(phone_number):
    try:
        otp = generate_otp()
        message = client.messages.create(
            body=f"SWARAJ TRACTOR HARYANA WELCOMES YOU ,Your OTP is {otp}", from_="+12706373277", to=phone_number
        )

        return otp , True
        
    except Exception as e:
        print(e)
    
    return '' , False