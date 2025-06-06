from django.core.mail import send_mail
from django.template.loader import render_to_string
# from django.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Product
import json
from palm_trees.models import Register,Order,Product

def send_email_verification(user, req):
    token = default_token_generator.make_token(user)
    return token

def check(name):
    try:
        Register.objects.get(email=name)
        return True
    except Exception:
        return False
# Create your views here.
def index(req):
    products = Product.objects.all()
    return render(req,'test.html',{'product':products})
def register(req:json):
    if req.method == "POST":
       data = json.load(req)
       fullName:str =  data.get('fullName')
       email:str = data.get('email')
       password:str = data.get('password')
       confirmPassword:str = data.get('confirmPassword')

       if check(email):
         return JsonResponse({"fullName":"user already exists"})

       if password != confirmPassword:
        return JsonResponse({"confirmPassword":"password mismatch !"})
       
       
    return render(req,'signup.html')

def login(req):
    send_email_verification("amir",req)
    return render(req,'signin.html')



