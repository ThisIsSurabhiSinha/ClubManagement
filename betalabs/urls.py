from django.contrib import admin
from django.urls import path,include
from betalabs import views

urlpatterns = [
   
    path('',views.index,name="betalabsHome"),
    path('<str:subClub_slug>', views.subClub_detail, name='subClub_detail'),
]
