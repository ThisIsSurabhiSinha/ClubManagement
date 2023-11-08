from django.contrib import admin
from django.urls import path,include,re_path
from wildbeats import views
urlpatterns = [
    path('',views.index,name="wildbeatsHome"),
    path('handle_suggestion/<str:subClub_slug>',views.handle_suggestion,name="handle_suggestion"),
    re_path(r'^clubleads/$', views.subclubleads, name="Wclubleads"),
    path('<str:subClub_slug>', views.subClub_detail, name='subClub_detail'),
    path('allclubleads/', views.clubleads, name="Wallclubleads"),
]