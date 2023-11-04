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
    return render(request,'betalabs/clubleads.html',{'all_leads': all_leads,'majorclub':'Betalabs','subclub_name':displayClub,'leader':leader})
def subclubleads(request):

    subclub_name = request.GET.get('subclub_name')
    majorclub = request.GET.get('majorclub')
    
    displayClub = SubClub.objects.filter(club_name=subclub_name).first()
    
    
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

    return render(request, 'betalabs/subclubleadstemp.html', {'displayClub': displayClub, 'all_leads': all_leads, 'subclub_name': subclub_name,'majorclub':majorclub})
