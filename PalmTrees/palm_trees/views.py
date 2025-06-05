from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Product
import json
from palm_trees.models import Register,Order,Product

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
    return render(req,'signin.html')


