from django.contrib import admin
from django.urls import path,include,re_path
from Home import views


urlpatterns = [
   
    path('',views.index,name="Homepage"),
    path('logout/',views.handle_logout,name="handle_logout"),
    path('signup/handle_signup/',views.handle_signup,name="signup"),
    path('signup/',views.view_signup,name="view_signup"),
    path('login/',views.view_login,name='login'),
    path('login/handle_login/',views.handle_login,name="handlelogin"),
    path('quizpage/',views.show_quiz,name="quizpage"),
    path('quizpage/analyze/',views.analyze,name="quizresult"),
    path('countdown/',views.countdown,name="countdown"),
    path('details/',views.details,name="details"),
    path('kh/',views.kh,name="kh"),
    re_path(r'^quizpage/analyze/result/$',views.show_full_result,name="quizresult2"),
    #   re_path(r'^clubleads/$', views.subclubleads, name="clubleads"),
  
]
