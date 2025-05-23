from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Product

# Create your views here.
def index(req):
    products = Product.objects.all()
    return render(req,'test.html',{'product':products})
def register(req):
    print(req)
    if req.method == "POST":
       print(req)
       fullName:str =  req.POST.get("fullName")
       print('This is your full name: ',fullName)
    return render(req,'signup.html')

def login(req):
    return render(req,'signin.html')
