from django.contrib import admin
from django.urls import path,include
from Home import views


urlpatterns = [
   
    path('',views.index,name="Homepage"),
    path('logout/',views.handle_logout,name="handle_logout"),
    path('signup/handle_signup/',views.handle_signup,name="signup"),
    path('signup/',views.view_signup,name="view_signup"),
    path('login/',views.view_login,name='login'),
    path('login/handle_login/',views.handle_login,name="handlelogin"),
  
]
