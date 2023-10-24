from django.db import models
from django.db.models import Model
from datetime import date 
class SubClub(models.Model):
    id=models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sportec/images',default="")
    about = models.TextField(default="")
    leader1 = models.CharField(max_length=100,default="")
    leader2 = models.CharField(max_length=100,default="")
    subleader1 = models.CharField(max_length=100,default="")
    subleader2 = models.CharField(max_length=100,default="")
    subleader3 = models.CharField(max_length=100,default="")
    past_events = models.TextField(default="")
    upcoming_event = models.CharField(max_length=500,default="")
    instagram_handle = models.URLField(max_length=500,default="")  
    facebook_handle = models.URLField(max_length=500,default="")  
    youtube_handle = models.URLField(max_length=500,default="") 
    linkedin=models.URLField(max_length=500,default="")
    email = models.EmailField(max_length=100,default="")            
    suggestion_box = models.TextField(default="")
    tagline=models.TextField(default="")
    logo=models.ImageField(upload_to='sportec/images',default="")
    def __str__(self):
        return self.club_name
