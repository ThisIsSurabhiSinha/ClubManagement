"""
URL configuration for Club project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""  
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from Home.views import custom_login_view 

admin.site.login = custom_login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls')),
    path('wildbeats/',include('wildbeats.urls')),
    path('trendles/',include('trendles.urls')),
    path('betalabs/',include('betalabs.urls')),
    path('sportec/',include('sportec.urls')),
    path('handle_suggestion/',include('wildbeats.urls')),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
