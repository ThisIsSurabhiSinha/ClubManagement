from django.shortcuts import render,HttpResponse
from betalabs.models import SubClub
# Create your views here.
def index(request):
    SubClubs=SubClub.objects.all()
    return render(request,'betalabs/index.html',{'SubClubs':SubClubs})
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
    return render(request, 'betalabs/betalabs_subclub.html', {'displayClub': displayClub,'all_leads':all_leads})

def weeklycoding(request):
    return render(request,"betalabs/weeklycoding.html")
def webdevelopment(request):
    return render(request,"betalabs/webdevelopment.html")
def streak(request):
    return render(request,"betalabs/streak.html")
def registration(request):
    return render(request,"betalabs/registration.html")
def profile(request):
    return render(request,"betalabs/profile.html")
def dp(request):
    return render(request,"betalabs/dp.html")
def advancecoding(request):
    return render(request,"betalabs/advancedcoding.html")
def codingprofile(request):
    return render(request,"betalabs/profile.html")