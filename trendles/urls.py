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
    path('elections',views.elections,name="elections"),
    path('upload_image',views.upload_image,name="upload_image"),
    # re_path(r'^allclubleads/$', views.subclubleads, name="clubleads2"),
    # re_path(r'^allclubleads/(?P<subclub_name>[\w\s-]+)/(?P<majorclub>[\w\s-]+)/$', views.subclubleads, name="clubleads2")

    # path('<str:slug>',views.subclubleads,name="subclubleads"),
    
    #path('<str:subClub_slug>', views.subClub_detail, name='subClub_detail'),
]