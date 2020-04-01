from django.shortcuts import render
from django.core.mail import EmailMessage, send_mass_mail
from django.http import JsonResponse
from login_register.models import Register
import pymysql


def login(request):
    return render(request, 'login.temp.html')


def req_register(request):
    return render(request, 'register.temp.html')


def register(request):
    return "test"
