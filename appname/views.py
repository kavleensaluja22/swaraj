from django.contrib.auth.forms import UserCreationForm
from django.urls import path
from django.contrib.auth import authenticate,login
import os
from appname.models import Feedback
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth import logout
from appname.models import GalleryImage
from django.http import JsonResponse
import random
from django.shortcuts import render
from twilio.rest import Client
from .models import Feedback
import appname
from django.urls import reverse
import json
from django.views.decorators.csrf import csrf_exempt
from .utils import send_otp
from django.shortcuts import render, redirect
from django.contrib import messages
from twilio.rest import Client
import random
from .models import OTP
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError



@csrf_exempt
def send_otp_to_phone_number(request , phone_number):
    otp , status  = send_otp(phone_number)
    return JsonResponse({
        'status' : True ,
        'message' : 'OTP sent',
        'data' : { 'otp' : otp}
    })


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        OTP.objects.create(
            name =name,
            phone_number =phone_number,
            address =address,
        )
        return redirect('/')

    return render(request, 'home.html')


def location(request):
    return render (request ,'location.html')


def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        print("name:", name)
        print("phone:", phone)
        print("desc:", desc)

        if not name:
            return HttpResponse('Please enter your name')
        
        feedback = Feedback(name=name, phone=phone, desc=desc, date=datetime.today())
        feedback.save()
        return render(request, 'home.html')
        # return HttpResponse ('Thank you for your feedback!')
        
    return render(request, 'feedback.html')



def gallery(request):
    if request.method=="GET":
        images = GalleryImage.objects.all()
        return render(request,'photos.html',{'images':images})



account_sid = 'AC2dd2d7696a8b5c24627cbe7807030029'
auth_token = '2f92b57e0f63522bb6cd3be1e1bced21'
client = Client(account_sid, auth_token)

def generate_otp():
    # Generate a random 6-digit number
    otp = random.randint(100000, 999999)
    return otp


def take_number(request):
    name = request.POST.get('name')
    phone_number = request.POST.get('phone_number')
    address = request.POST.get('address')
    otp = generate_otp()
    message = client.messages.create(
        body="Your OTP is {}".format(otp),
        from_="+12706373277",
        to=phone_number
    )
  
    request.session['name'] = name
    request.session['phone_number'] = phone_number
    request.session['address'] = address
    request.session['otp'] = otp 
    print(message.sid)
    return render(request, 'verify_otp.html')



def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        if otp == str(stored_otp):
            # OTP is correct, create and save the OTP record to the database
            name = request.session.get('name')
            phone_number = request.session.get('phone_number')
            address = request.session.get('address')
            otp = request.session.get('otp')
            
            if phone_number:
                otp_record = OTP(name=name, phone_number=phone_number, address=address)
                otp_record.save()
                # Redirect to home page
                return redirect('/')
            else:
                # Phone number is not provided, send error message
                return render(request, 'verify_otp.html', {'error': 'Phone number is required'})
        else:
            # OTP is incorrect, send error message
            return render(request, 'verify_otp.html', {'error': 'Incorrect OTP'})
    else:
        return render(request, 'verify_otp.html')




def g_try(request):
    return render(request,'g_try.html')

def s724(request):
    return render(request,'s724.html')
def s733(request):
    return render(request,'s733.html')
def s735(request):
    return render(request,'s735.html')
def s744(request):
    return render(request,'s744.html')
def s855(request):
    return render(request,'s855.html')
def s969(request):
    return render(request,'s969.html')
def s963(request):
    return render(request,'s963.html')
def s717(request):
    return render(request, 's717.html')
def combine1(request):
    return render(request,'combine1.html')
def combine2(request):
    return render(request,'combine2.html')
def combine3(request):
    return render(request,'combine3.html')
def index(request):
    return render(request,'index.html')
def xt(request):
    return render(request,'xt.html')