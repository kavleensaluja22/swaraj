from django.urls import path, reverse
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import login, logout
from django.conf import settings
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime
import json

from .models import Feedback, OTP, GalleryImage
# from .utils import send_otp


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        OTP.objects.create(
            name=name,
            phone_number=phone_number,
            address=address,
        )
        return redirect('/')

    return render(request, 'home.html')


def location(request):
    return render(request, 'location.html')


def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        if not name:
            return HttpResponse('Please enter your name')

        feedback = Feedback(name=name, phone=phone, desc=desc, date=datetime.today())
        feedback.save()
        return render(request, 'home.html')

    return render(request, 'feedback.html')


def gallery(request):
    if request.method == "GET":
        images = GalleryImage.objects.all()
        return render(request, 'photos.html', {'images': images})


def g_try(request):
    return render(request, 'g_try.html')


def s724(request): return render(request, 's724.html')
def s733(request): return render(request, 's733.html')
def s735(request): return render(request, 's735.html')
def s744(request): return render(request, 's744.html')
def s855(request): return render(request, 's855.html')
def s969(request): return render(request, 's969.html')
def s963(request): return render(request, 's963.html')
def s717(request): return render(request, 's717.html')
def combine1(request): return render(request, 'combine1.html')
def combine2(request): return render(request, 'combine2.html')
def combine3(request): return render(request, 'combine3.html')
def index(request): return render(request, 'index.html')
def xt(request): return render(request, 'xt.html')
