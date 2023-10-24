from django.contrib import admin
from django.urls import path,include
from trendles import views
urlpatterns = [
    
    path('',views.index,name="trendlesHome"),
     path('<str:subClub_slug>', views.subClub_detail, name='subClub_detail'),
]