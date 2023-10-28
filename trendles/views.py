from django.shortcuts import render,HttpResponse
from trendles.models import SubClub
from Home.models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def index(request):
    # SubClubs=SubClub.objects.all()
    # return render(request,'trendles/trendles.html',{'SubClubs':SubClubs})
    return render(request,'trendles/functionalpage.html')
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
    return render(request,'trendles/finance.html')
def chitrachaya(request):
    return render(request,'trendles/chitrachaya.html')
def marketing(request):
    return render(request,'trendles/marketing.html')
def designing(request):
    return render(request,'trendles/designing.html')
def literature(request):
    return render(request,'trendles/literature.html')
def debating(request):
    return render(request,'trendles/debating.html')
def clubleads(request):
    return render(request,'trendles/clubleads.html')
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