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
    image = models.ImageField(upload_to='trendles/images',default="")
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
    email = models.EmailField(max_length=100,default="",null=True,blank=True)            
    suggestion_box = models.TextField(default="",null=True)
    tagline=models.TextField(default="",null=True)
    logo=models.ImageField(upload_to='trendles/images',default="")
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
class ChitrachayaImages(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(Student, on_delete=models.CASCADE)
    media_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])
    media_file = models.FileField(upload_to='trendles/images/',blank=True, null=True, default='/media/trendles/images/unknown.png', help_text='Upload an image file.')
    upload_date = models.DateTimeField(auto_now_add=True)
    image_id=models.AutoField(primary_key=True)
    subclub_name=models.CharField(max_length=100,blank=True,null=True,default="")
    majorclub_name=models.CharField(max_length=100,blank=True,null=True)
    uploaded_on = models.DateField(auto_now=True, editable=False)
    def __str__(self):
        return   self.upload_date

class LiteraryDocument(models.Model):
    doc_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,blank=True,null=True,default="")
    document = models.FileField(upload_to='trendles/literaryclubdocs/',blank=True, null=True, default='trendles/literaryclubdocs/default.txt', help_text='Upload a document (JPG, JPEG, PNG, PDF, Word)')
    uploaded_by = models.ForeignKey(Student, on_delete=models.CASCADE)
    upload_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link the document to a user
    time_of_upload = models.TimeField(auto_now_add=True)
    description = models.TextField(default="",blank=True, null=True)
    subclub_name=models.CharField(max_length=100,blank=True,null=True,default="")
    majorclub_name=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.title+ " by  " +  self.user.first_name  # Provide a string representation for better display in the admin interface

    class Meta:
        verbose_name = "Literary Document"
        verbose_name_plural = "Literary Documents"
class DesignClubFile(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True,default="")
    description = models.TextField(default="",blank=True, null=True)
    file = models.FileField(upload_to='trendles/designclubfile/',blank=True, null=True,default="")
    uploaded_by = models.ForeignKey(Student, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    subclub_name=models.CharField(max_length=100,blank=True,null=True,default="")
    majorclub_name=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
         return self.title+ " by  " +  self.user.first_name
    class Meta:
        verbose_name = "Design Club File"
        verbose_name_plural = "Design Club Files"
class FinanceClubFile(models.Model):
    title = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='trendles/financefile/',blank=True, null=True,default="")
    uploaded_by = models.ForeignKey(Student, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Link the file to a user
    upload_date = models.DateTimeField(auto_now_add=True)
    subclub_name=models.CharField(max_length=100,blank=True,null=True,default="")
    majorclub_name=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
         return self.title+ " by  " +  self.user.first_name

    class Meta:
        verbose_name = "Finance Club File"
        verbose_name_plural = "Finance Club Files"
class MarketingOutreachClubFile(models.Model):
    title = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='trendles/marketting/',blank=True, null=True,default="")
    uploaded_by = models.ForeignKey(Student, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Link the file to a user
    upload_date = models.DateTimeField(auto_now_add=True)
    subclub_name=models.CharField(max_length=100,blank=True,null=True,default="")
    majorclub_name=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
         return self.title+ " by  " +  self.user.first_name

    class Meta:
        verbose_name = "Marketing & Outreach Club File"
        verbose_name_plural = "Marketing & Outreach Club Files"
class Announcement(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    uploaded_by = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.TextField(default="")  # The content of the announcement
    timestamp = models.DateTimeField(auto_now_add=True)
    date=models.DateField(auto_now_add=True)  # The date and time the announcement was created

    def __str__(self):
        return self.id