from django.contrib import admin

# Register your models here.
from Home.models import MajorClub,RelatedClub
admin.site.register(MajorClub)
admin.site.register(RelatedClub)
