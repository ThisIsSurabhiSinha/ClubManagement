from django.shortcuts import render,HttpResponse,redirect
from trendles.models import SubClub
from Home.models import Student,Suggestion,MajorClub
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import os
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


from trendles.models import ChitrachayaImages
from Home.models import Event
from django.utils import timezone

# Create your views here.
def index(request):
    # SubClubs=SubClub.objects.all()
    # return render(request,'trendles/trendles.html',{'SubClubs':SubClubs})
    return render(request,'trendles/functionalpage.html',{'club':"Trendles"})
def finance(request):
    return render(request,'trendles/finance.html',{'subclub_name': "Finance",'majorclub':"trendles"})
def chitrachaya(request):
    return render(request,'trendles/chitrachaya.html',{'subclub_name': "Chitrachaya",'majorclub':"Trendles"})
def marketing(request):
    return render(request,'trendles/marketting.html', {'subclub_name': "marketing",'majorclub':"Trendles"})
def designing(request):
    return render(request,'trendles/designing.html',{'subclub_name': "Designing",'majorclub':"Trendles"})
def literature(request):
    return render(request,'trendles/literature.html',{'club': "Literary",'majorclub':"Trendles"})
def debating(request):
    return render(request,'trendles/debating.html',{'subclub_name': "Debate",'majorclub':"Trendles"})

def clubleads(request):
    # Fetch the first SubClub object
    displayClub = SubClub.objects.all()
 
    all_leads = {}
    leader=[]
    leader1={
        'name': displayClub[0].leader1,
                'email': displayClub[0].leader1mail,
                'phone': displayClub[0].leader1phone,
            }
    leader.append(leader1)
    leader2={
        'name': displayClub[0].leader2,
                'email': displayClub[0].leader2mail,
                'phone': displayClub[0].leader2phone,
            }
    leader.append(leader2)
    
    for club in displayClub:

        l=[]
        if club.subleader1.lower()!="none":
            l.append(club.subleader1)
        if club.subleader2.lower()!="none":
            l.append(club.subleader2)
        if club.subleader3.lower()!="none":
            l.append(club.subleader3)
        all_leads[club]=l
    print(all_leads)
  

    return render(request,'trendles/clubleads.html',{'all_leads': all_leads,'majorclub':'Trendles','subclub_name':displayClub,'leader':leader})
def calander(request):
    return render(request,'trendles/calander.html')
def announcement(request):
    return render(request,'trendles/announcements.html')
def elections(request):
    return render(request,'trendles/elections.html')
def settings(request):
    return render(request,'trendles/settings.html')
def profile(request):
    if request.user.is_authenticated:
        user = request.user
        first_name = user.first_name
        last_name = user.last_name
        email = user.email
        student = Student.objects.get(email=email)
        suggestion_by_student=Suggestion.objects.filter(student=student)
        suggestion_count=len(suggestion_by_student)
        student_info = {
                'phone': student.phone_number,
                'program': student.program,
                'department': student.department,
                'batch': student.batch,
                'linkedin_profile': student.linkedin_profile,
                'first_name' : user.first_name,
                'last_name' :user.last_name,
                'email' : user.email,
                'suggestion_count':suggestion_count
            }
    return render(request,'trendles/profile.html',student_info)
def subclubleads(request):

    subclub_name = request.GET.get('subclub_name')
    majorclub = request.GET.get('majorclub')
    print(subclub_name,majorclub)
    displayClub = SubClub.objects.filter(club_name=subclub_name).first()
    print(SubClub.objects.all())
    
    all_leads = []

    # Define a list of leader fields to iterate through
    leader_fields = ['leader1', 'leader2', 'subleader1', 'subleader2', 'subleader3']

    for field in leader_fields:
        leader_name = getattr(displayClub, field)
        leader_email = getattr(displayClub, f"{field}mail")
        leader_phone = getattr(displayClub, f"{field}phone")

        if leader_name.lower() != "none" and leader_name:
            field = {
                'name': leader_name,
                'email': leader_email,
                'phone': leader_phone,
            }
            print(field)
            all_leads.append(field)

    return render(request, 'trendles/subclubleadstemp.html', {'displayClub': displayClub, 'all_leads': all_leads, 'subclub_name': subclub_name,'majorclub':majorclub})


def upload_image(request):
    if request.method == "POST":
        
        if 'file_name' in request.POST:
            uploaded_file_name = request.POST['file_name']
            l = uploaded_file_name.split('.')
            if len(l) > 1:
                file_extension = l[-1].lower()
            else:
                # Handle the case where there is no file extension
                file_extension = ''
    
        student = get_object_or_404(Student, student_id=request.user.username)
       
        if file_extension in ('.jpg', '.jpeg', '.png'):
            media_type = 'image'
        elif file_extension in ('.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm'):
            media_type = 'video'
        else:
            # Handle other file types or raise an error if necessary
            media_type = 'unknown'
        club_id=SubClub.objects.filter(club_name="Chitrachaya").first()
        majorlcub_id=MajorClub.objects.filter(club_name="Trendles").first()

        event_name = request.POST.get('eventName')
        event_date = request.POST.get('eventDate')
        event, created = Event.objects.get_or_create(
            event_name=event_name,
            event_date=event_date,
            byClub=majorlcub_id,
        )

        image = ChitrachayaImages(
            event=event,
            uploaded_by=student,
            media_type=media_type,
            media_file=uploaded_file_name,
            upload_date=timezone.now(),
            subclub_name=club_id,
            majorclub_name=majorlcub_id,
        )
        image.save()
        messages.success(request, 'Upload complete! Your pictures and videos are now part of our collection.')
        return redirect('chitrachaya')
        
    messages.error(request, 'Attempt failed !! Please try again.')
    return redirect( 'chitrachaya')

    