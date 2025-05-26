from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Product
import json

# Create your views here.
def index(req):
    products = Product.objects.all()
    return render(req,'test.html',{'product':products})
def register(req:json):
    if req.method == "POST":
       fullName =  user("",'fullName')
       print('This is your full name: ',fullName,fullName)
    return render(req,'signup.html')

def login(req):
    return render(req,'signin.html')

def user(req,info:any) -> any:
    try:
        data = json.load(req)
        information = data.get(info)
        return information
    except Exception as e:
        return e
    
