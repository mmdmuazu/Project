from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard/<userid>/',views.dashboard,name='dashboard'),
    path('transfer/',views.transfer , name = 'transfer'),
    path('update_balance/',views.update_balance, name = 'update balance'),
    path('get_link_states/', views.get_link_states , name = 'get link states' ),
    path('mark_link_used/',views.mark_link_used,name='mark link as used')
]