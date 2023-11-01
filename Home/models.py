from django.db import models
from django.db.models import Model
from datetime import date 
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
class MajorClub(models.Model):
    id=models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Home/images',default="")
    about = models.TextField(default="")
    leader1 = models.CharField(max_length=100,default="")
    leader2 = models.CharField(max_length=100,default="")
    past_events = models.TextField(default="",null=True)
    upcoming_event = models.CharField(max_length=500,default="",null=True)
    instagram_handle = models.URLField(max_length=500,default="",null=True)  
    facebook_handle = models.URLField(max_length=500,default="",null=True)  
    youtube_handle = models.URLField(max_length=500,default="",null=True) 
    linkedin=models.URLField(max_length=500,default="",null=True)
    email = models.EmailField(max_length=100,default="",null=True)            
    suggestion_box = models.TextField(default="",null=True)
    tagline=models.TextField(default="",null=True)
    logo=models.ImageField(upload_to='Home/images',default="")
    related_club = GenericRelation('RelatedClub')
    suggestion=GenericRelation('Suggestion')
 
    def __str__(self):
        return self.club_name
class RelatedClub(models.Model): 
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    major_club = models.ForeignKey(MajorClub, on_delete=models.CASCADE)
class Student(models.Model):
   
    student_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,null=True)
    program = models.CharField(max_length=50,null=True)
    batch = models.CharField(max_length=4,null=True)
    department = models.CharField(max_length=50,null=True)
    linkedin_profile = models.URLField(max_length=200, blank=True, null=True)
    student_suggestion=GenericRelation('Suggestion')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Suggestion(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    club = GenericForeignKey('content_type', 'object_id')
    suggestion_text = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)
    exact_subclub_name=models.CharField(null=True,blank=True,max_length=100)
    

    def __str__(self):
        return f"Suggestion by {self.student.student_id} for {self.club.club_name}"