from django.shortcuts import render,HttpResponse,redirect
from wildbeats.models import SubClub
from Home.models import Suggestion,Student
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.contrib import messages
# Create your views here.
def index(request):
    SubClubs=SubClub.objects.all()
    return render(request,'wildbeats/wildbeats.html',{'SubClubs':SubClubs})
def subClub_detail(request,subClub_slug):
   
    slug=subClub_slug[0].upper()+subClub_slug[1:]
    displayClub = SubClub.objects.filter( club_name=slug).first()
    print(displayClub)
    all_leads=[]
    # if displayClub.leader1.lower()!= "none":
    #     all_leads.append(displayClub.leader1)
    # if displayClub.leader2.lower()!= "none":
    #     all_leads.append(displayClub.leader2)
    if displayClub.subleader1.lower()!= "none":
        all_leads.append(displayClub.subleader1)
    if displayClub.subleader2.lower()!= "none":
        all_leads.append(displayClub.subleader2)
    if displayClub.subleader3.lower()!= "none":
        all_leads.append(displayClub.subleader3)
    return render(request, 'wildbeats/wildbeats_subclubs.html', {'displayClub': displayClub,'all_leads':all_leads,'slug':slug})
def handle_suggestion(request,subClub_slug):
     if request.method=="POST":
          suggestion_content=request.POST.get('floatingTextarea')
          user_id = request.user.id
          sub_club = SubClub.objects.get(club_name=subClub_slug)
          sub_club_id = sub_club.id
          user = User.objects.get(username=request.user)
          student=Student.objects.get(student_id=user.username)
          content_type = ContentType.objects.get_for_model(SubClub)
          club = SubClub.objects.get(id=sub_club_id)
          suggestion = Suggestion.objects.create(
            student=Student.objects.get(student_id=user.username),
            content_type=ContentType.objects.get_for_model(SubClub),
            object_id=sub_club.id,
            suggestion_text=suggestion_content,
            submission_date=timezone.now(),
            exact_subclub_name=subClub_slug
        )
          suggestion.save()
          messages.success(request,"Thank you for your feedback. Your input is valuable!")
          return redirect('subClub_detail', subClub_slug=subClub_slug)
     else:
         return HttpResponse("Error")
     
