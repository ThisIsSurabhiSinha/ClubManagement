from django.contrib import admin
from django.urls import path,include,re_path
from trendles import views
urlpatterns = [
    
    path('',views.index,name="trendlesHome"),
    # path('funtionalpage',views.fuctionalpage,name="functionalpage"),
    path('finance/',views.finance,name="finance"),
    path('chitrachaya',views.chitrachaya,name="chitrachaya"),
    path('marketing',views.marketing,name="marketing"),
    path('designing',views.designing,name="designing"),
    path('literature',views.literature,name="literature"),
    path('debating',views.debating,name="debating"),
    re_path(r'^clubleads/$', views.subclubleads, name="clubleads"),
    path('allclubleads/', views.clubleads, name="allclubleads"),
    path('profile',views.profile,name="userprofile"),
    path('calander',views.calander,name="calander"),
    path('announcement',views.announcement,name="announcement"),
    path('settings',views.settings,name="settings"),
    # path('elections',views.elections,name="elections"),
    re_path(r'^elections/$', views.elections, name="elections"),
    path('upload_image',views.upload_image,name="upload_image"),
    path('quizclub',views.quizclub,name="quizclub"),
    path('Literary_upload_document',views.Literary_upload_document,name="Literary_upload_document"),
    path('design_club_upload_document',views.design_club_upload_document,name="design_club_upload_document"),
    path('finance_club_upload_document',views.finance_club_upload_document,name="finance_club_upload_document"),
    path('market_club_upload_document',views.market_club_upload_document,name="market_club_upload_document"),
    path('create_announcement', views.create_announcement, name='create_announcement'),
]