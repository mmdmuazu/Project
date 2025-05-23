from django.shortcuts import *
from django.http import *
from django.contrib import * 
import json
from dollarCoin.models import Myusers as user

def index(request: json) -> any:
    data = request.GET.get
    user_id:str  = data('user_id')
    username: str = data('username')
    name:str = data('name')
 
    if not username or username == "None":
        if name and name != 'None':
            username = name
        else:
            return HttpResponse("<h1 style='text-align:center;margin-top:100px; padding:50px; color:red';>USERNAME CAN'T BE NONE</h1>")
    
    if not user_id or user_id == 'None':
        return HttpResponse("<h1 style='text-align:center;margin-top:100px; padding:50px; color:red';>USER ID CAN'T BE NONE</h1>")
    
    dataBase = user.objects.get
    try:
        if dataBase(userId=user_id):
            pass
    except Exception:
        user(username=username,userId=user_id).save()
        pass
    info = dataBase(userId=user_id)  
    return render(request,'dashboard.html',{'info':info})

def dashboard(request: json,userid) -> any:
    try:
        if user.objects.get(userId=userid):
            return JsonResponse({'dashboard':userid,'message':'good'})
    except Exception as e:
        print(e)
        return JsonResponse({'dashboard':userid,'message':'Bad'})

def update_balance(request: json) -> any:
    data = request.POST.get('body')
    print(data)
    return JsonResponse({'update_balance':True})

def transfer(request: json) -> any:
    return JsonResponse({'transfer':True})

def get_link_states(request: json) -> any:
    return JsonResponse({'get_link_states':True})

def mark_link_used(request: json) -> any:
    return JsonResponse({'mark_link_as_used':True})