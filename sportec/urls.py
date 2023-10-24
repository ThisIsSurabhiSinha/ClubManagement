from django.contrib import admin
from django.urls import path,include
from sportec import views
urlpatterns = [
    path('<str:subClub_slug>', views.subClub_detail, name='subClub_detail'),
    path('',views.index,name="sportecHome")
]