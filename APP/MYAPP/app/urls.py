from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('login/',views.login, name = 'login'),
    path('register/',views.register , name = 'register'),
    path('verify/<username>/',views.verify , name= 'verify'),
    path('dashboard/',views.dashboard , name='dashboard')
]