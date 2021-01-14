from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counselordetails/', views.counselordetails, name='counselordetails'),
    path('farmerdetails/', views.farmerdetails, name='farmerdetails'),
]
