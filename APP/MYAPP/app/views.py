from django.shortcuts import *
from django.urls import *
from django.http import *
import json
from app.models import MyUsers
from django.contrib import *
from django.contrib.auth import *


# Create your views here.
class CheckUser:
    information = 'invalid login details'
    login = False
    verified = None
    def __init__(self,name,logPassword):
    # def search(self,name,logPassword):
        if MyUsers.objects.filter(username=name).exists():
            info = MyUsers.objects.get(username=name)
            self.verified = info.verify
            password = info.userPassword
            if password == logPassword:
                self.login = True
            else:
                self.information = 'incorrect password'

        if MyUsers.objects.filter(userEmail=name).exists():
            info = MyUsers.objects.get(userEmail=name)
            self.verified = info.verify
            password = info.userPassword
            if password == logPassword:
                self.login = True
            else: 
                self.information = 'incorrect password'
        # else:
        # self.information = 'invalid login details'
    # try:
    #     login = False
    #     searching = MyUsers.objects.get(username=name)
    #     if searching.userPassword == logPassword:
    #         login = True
    #     if searching and login:
    #         return  login 
    #     else:
    #         return 'user not found'
    # except Exception as e:
    #     return 'username not in users'

def index(request):
    return render(request,'index.html')

def  verify(request,username):
    if request.method == 'GET':
        if MyUsers.objects.filter(username=username):
            info = MyUsers.objects.get(username=username)
            info.verify = True
            info.save()
            if info.verify == True:
                return JsonResponse({'verify':'good'})
            else:
                return JsonResponse({'username exist':'but not verified'})
            
        else:
            return JsonResponse({'no username':' found'})

def login(request):
    if request.method == 'POST':
        data = json.load(request)
        username:str = data.get('username')
        password:str = data.get('password')
        user = CheckUser(username,password)
        # print(MyUsers.objects.get(username=username).verify)
        
        if user.login:
            # info = login.information
            if not user.verified:
                return JsonResponse({'success':False,'message':'user not verified'})
            request.session['username'] = username  
            # return redirect('dashboard') 
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'success':False,'message':user.information})

    #     user = authenticate(request, username=username, password=password)

    #     if user is not None:
    #         print(user)
    #         login(request, user)
    #         request.session["username"] = username  # Store username in session
    #         return redirect("dashboard")  # Redirect to dashboard

    #     else:
    #         messages.error(request, "Invalid username or password")

    # return render(request, "index.html")
        

def register(request):
    if request.method == 'POST':
        data = json.load(request)
        get = data.get
        fullName:str = get('fullName')
        username:str = get('username')
        email:str = get('email')
        password:str = get('password')
        confirmPassword:str = get('confirmPassword')

        if MyUsers.objects.filter(username=username).exists():
            return JsonResponse({'success':False,'message':'username already exist!'})
        if MyUsers.objects.filter(userEmail=email).exists():
            return JsonResponse({'message':'email already exist !'})

        if password != confirmPassword:
            return JsonResponse({'success':False,'message':'Password mismatch'})
        # else:
        user = MyUsers(fullName=fullName,username=username,userEmail=email,userPassword=password,verify=False)
        user.save()
        return JsonResponse({'success':True,'message':f'Hello username: {username} fullname: {fullName} Email: {email} password:{password}!'})
    return  render(request,'register.html')

def dashboard(request):
    print("Session Data:", request.session.items())  # Debugging
    username = request.session.get('username')
    sessionList = [doc for doc in dict(request.session.items()).values() if username in doc]
    print(sessionList)
    

    if sessionList:
        info = MyUsers.objects.get(username=username)
        password= info.userPassword
        email = info.userEmail
        fullName = info.fullName
        return render(request, 'dashboard.html', {'username': info})
    else:
        return redirect('index')
    # def dashboard_view(request):
    # username = request.session.get("username", "Guest")  # Get username from session
    # return render(request, "dashboard.html", {"username": username})