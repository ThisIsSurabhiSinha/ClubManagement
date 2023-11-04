from django.contrib import admin

# Register your models here.
from Home.models import MajorClub,RelatedClub,Suggestion,Event,Student
admin.site.register(MajorClub)
admin.site.register(RelatedClub)
admin.site.register(Suggestion)
admin.site.register(Event)
admin.site.register(Student)
