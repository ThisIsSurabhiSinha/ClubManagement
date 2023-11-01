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
    # path('clubleads/', views.subclubleads, name="clubleads"),
    path('profile',views.profile,name="userprofile"),
    path('calander',views.calander,name="calander"),
    path('announcement',views.announcement,name="announcement"),
    path('settings',views.settings,name="settings"),
    path('elections',views.elections,name="elections"),
    path('<str:slug>',views.subclubleads,name="subclubleads"),
    
    #path('<str:subClub_slug>', views.subClub_detail, name='subClub_detail'),
]