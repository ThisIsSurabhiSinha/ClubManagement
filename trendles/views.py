from django.shortcuts import render,HttpResponse
from trendles.models import SubClub
from Home.models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def index(request):
    # SubClubs=SubClub.objects.all()
    # return render(request,'trendles/trendles.html',{'SubClubs':SubClubs})
    return render(request,'trendles/functionalpage.html',{'club':"Trendles"})
'''def subClub_detail(request,subClub_slug):
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
    return render(request, 'trendles/trendles_subclub.html', {'displayClub': displayClub,'all_leads':all_leads})'''
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
   


    # Create a list to store leader and sub-leader information
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
        student_info = {
                'phone': student.phone_number,
                'program': student.program,
                'department': student.department,
                'batch': student.batch,
                'linkedin_profile': student.linkedin_profile,
                'first_name' : user.first_name,
                'last_name' :user.last_name,
                'email' : user.email,
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
