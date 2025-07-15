from django.urls import path
from ledger.views.auth_view import LoginView, RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
