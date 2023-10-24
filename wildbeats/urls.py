from django.contrib import admin
from django.urls import path,include
from wildbeats import views
urlpatterns = [
    path('',views.index,name="wildbeatsHome"),
    path('<str:subClub_slug>', views.subClub_detail, name='subClub_detail'),
]