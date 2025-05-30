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
       data = json.load(req)
       fullName:str =  data.get('fullName')
       email:str = data.get('email')
       password:str = data.get('password')
       confirmPassword:str = data.get('confirmPassword')
       print("name: ",fullName,"email :",email,"password :", password,"confirm password: ",confirmPassword)
       
       if password != confirmPassword:
        return JsonResponse({"confirmPassword":"password mismatch !"})
    #    if confirmPassword != password:
    #     return JsonResponse({'message':'password mismatch !'}),400
    return render(req,'signup.html')

def login(req):
    return render(req,'signin.html')


