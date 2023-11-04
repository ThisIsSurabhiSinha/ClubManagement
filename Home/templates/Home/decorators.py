from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django import template
from django.contrib.auth.models import Group

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
       if request.user.is_authenticate:
          return redirect('Homepage')
       else:
          return view_func(request,*args,**kwargs)
    return wrapper_func
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
           group=None
           if request.user.groups.exists():
               group=request.user.groups.all()[0].name
           if group in allowed_roles:
               return view_func(request,*args,**kwargs)
           else:
               return HttpResponse("You are not authorized to view this page")
        return wrapper_func
    return decorator


register = template.Library()


