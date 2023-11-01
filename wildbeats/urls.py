from django.contrib import admin
from django.urls import path,include
from wildbeats import views
urlpatterns = [
    path('',views.index,name="wildbeatsHome"),
    path('handle_suggestion/<str:subClub_slug>',views.handle_suggestion,name="handle_suggestion"),
    path('<str:subClub_slug>', views.subClub_detail, name='subClub_detail'),
]