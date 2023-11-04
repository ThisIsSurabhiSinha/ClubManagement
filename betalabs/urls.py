from django.contrib import admin
from django.urls import path,include,re_path
from betalabs import views

urlpatterns = [
   
    path('',views.index,name="betalabsHome"),
    path('weeklycoding/',views.weeklycoding,name="weeklycoding"),
    path('webdevelopment/',views.webdevelopment,name="webdevelopment"),
    path('streak/',views.streak,name="streak"),
    path('registration/',views.registration,name="registration"),
    path('profile/',views.profile,name="profile"),
    path('dp/',views.dp,name="dp"),
    path('advancecoding/',views.advancecoding,name="advancecoding"),
    path('profile/',views.codingprofile,name="codingprofile"),
    re_path(r'^clubleads/$', views.subclubleads, name="Bclubleads"),
    path('allclubleads/', views.clubleads, name="Ballclubleads"),
    path('<str:subClub_slug>', views.subClub_detail, name='subClub_detail'),
]
