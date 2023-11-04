from django.db import models
from django.db.models import Model
from datetime import date 
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from Home.models import Event
from Home.models import Student

class SubClub(models.Model):
    id=models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='betalabs/images',default="")
    about = models.TextField(default="")
    leader1 = models.CharField(max_length=100,default="")
    leader2 = models.CharField(max_length=100,default="")
    subleader1 = models.CharField(max_length=100,default="")
    subleader2 = models.CharField(max_length=100,default="")
    subleader3 = models.CharField(max_length=100,default="",null=True)
    past_events = models.TextField(default="",null=True)
    upcoming_event = models.CharField(max_length=500,default="",null=True)
    instagram_handle = models.URLField(max_length=500,default="",null=True)  
    facebook_handle = models.URLField(max_length=500,default="",null=True)  
    youtube_handle = models.URLField(max_length=500,default="",null=True) 
    linkedin=models.URLField(max_length=500,default="",null=True)
    email = models.EmailField(max_length=100,default="",null=True)            
    suggestion_box = models.TextField(default="",null=True)
    tagline=models.TextField(default="",null=True)
    logo=models.ImageField(upload_to='betalabs/images',default="")
    leader1mail = models.EmailField(max_length=100,default="",null=True,blank=True)
    leader2mail = models.EmailField(max_length=100,default="",null=True,blank=True)
    subleader1mail = models.EmailField(max_length=100,default="",null=True,blank=True)
    subleader2mail = models.EmailField(max_length=100,default="",null=True,blank=True)
    subleader3mail = models.EmailField(max_length=100,default="",null=True,blank=True)
    leader1phone = PhoneNumberField(null=True,blank=True)
    leader2phone = PhoneNumberField(null=True,blank=True)
    subleader1phone = PhoneNumberField(null=True,blank=True)
    subleader2phone = PhoneNumberField(null=True,blank=True)
    subleader3phone = PhoneNumberField(null=True,blank=True)
    def __str__(self):
        return self.club_name
