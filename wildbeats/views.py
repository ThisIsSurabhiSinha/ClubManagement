from django.shortcuts import render,HttpResponse,redirect
from wildbeats.models import SubClub
from Home.models import Suggestion,Student
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.contrib import messages
from trendles.models import Announcement
# Create your views here.
def index(request):
    SubClubs=SubClub.objects.all()
    return render(request,'wildbeats/functional.html',{'SubClubs':SubClubs})
def subClub_detail(request,subClub_slug):
   
    slug=subClub_slug[0].upper()+subClub_slug[1:]
    displayClub = SubClub.objects.filter( club_name=slug).first()
    all_leads=[]
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
def clubleads(request):
    # Fetch the first SubClub object
    displayClub = SubClub.objects.all()
    displayClub1 = SubClub.objects.all().first()
    all_leads = {}
    all_leads1=[]
    leader_fields = ['leader1', 'leader2']
    k=1
    for field in leader_fields:
        leader_name = getattr(displayClub1, field)
        leader_email = getattr(displayClub1, f"{field}mail")
        leader_phone = getattr(displayClub1, f"{field}phone")
        leader_id = k
        k+=1
        if leader_name.lower() != "none" and leader_name:
            field = {
                'name': leader_name,
                'email': leader_email,
                'phone': leader_phone,
                'id':leader_id
            }
            
            all_leads1.append(field)

    
    for club in displayClub:

        l=[]
        if club.subleader1.lower()!="none":
            l.append(club.subleader1)
        if club.subleader2.lower()!="none":
            l.append(club.subleader2)
        if club.subleader3.lower()!="none":
            l.append(club.subleader3)
        all_leads[club]=l
        two_days_ago = timezone.now() - timezone.timedelta(days=2)
        announcements_two_days_ago = Announcement.objects.filter(date__gte=two_days_ago)
 
   

    return render(request,'wildbeats/clubleads.html',{'all_leads': all_leads,'majorclub':'Wildbeats','subclub_name':displayClub,'all_leads1': all_leads1,'announcements_two_days_ago':announcements_two_days_ago})
def subclubleads(request):

    subclub_name = request.GET.get('subclub_name')
  
    majorclub = request.GET.get('majorclub')
 
    displayClub = SubClub.objects.filter(club_name=subclub_name).first()
   
    
    all_leads = []

    # Define a list of leader fields to iterate through
    leader_fields = ['leader1', 'leader2', 'subleader1', 'subleader2', 'subleader3']
    k=1
    for field in leader_fields:
        leader_name = getattr(displayClub, field)
        leader_email = getattr(displayClub, f"{field}mail")
        leader_phone = getattr(displayClub, f"{field}phone")

        if leader_name.lower() != "none" and leader_name:
            field = {
                'name': leader_name,
                'email': leader_email,
                'phone': leader_phone,
                'id':k
            }
            k+=1
        
            all_leads.append(field)
    two_days_ago = timezone.now() - timezone.timedelta(days=2)
    announcements_two_days_ago = Announcement.objects.filter(date__gte=two_days_ago)
    return render(request, 'wildbeats/subclubleadstemp.html', {'displayClub': displayClub, 'all_leads': all_leads, 'subclub_name': subclub_name,'majorclub':majorclub,'announcements_two_days_ago':announcements_two_days_ago})