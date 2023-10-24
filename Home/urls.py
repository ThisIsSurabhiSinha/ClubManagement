from django.contrib import admin
from django.urls import path,include
from Home import views

urlpatterns = [
   
    path('',views.index,name="Homepage")
]
