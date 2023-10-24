# from django.db import models
# from django.db.models import Model
# from datetime import date 
# from wildbeats.models import SubClub
# from trendles.models import SubClub
# from betalabs.models import SubClub
# from sportec.models import SubClub
# class MajorClub(models.Models):
#     id=models.AutoField(primary_key=True)
#     club_name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='Home/images',default="")
#     about = models.TextField(default="")
#     leader1 = models.CharField(max_length=100,default="")
#     leader2 = models.CharField(max_length=100,default="")
#     past_events = models.TextField(default="",null=True)
#     upcoming_event = models.CharField(max_length=500,default="",null=True)
#     instagram_handle = models.URLField(max_length=500,default="",null=True)  
#     facebook_handle = models.URLField(max_length=500,default="",null=True)  
#     youtube_handle = models.URLField(max_length=500,default="",null=True) 
#     linkedin=models.URLField(max_length=500,default="",null=True)
#     email = models.EmailField(max_length=100,default="",null=True)            
#     suggestion_box = models.TextField(default="",null=True)
#     tagline=models.TextField(default="",null=True)
#     logo=models.ImageField(upload_to='Home/images',default="")
#     subclubs = models.ManyToManyField(SubClub,SubClub,SubClub,SubClub)
#     def __str__(self):
#         return self.club_name
