from django.shortcuts import render,HttpResponse
from betalabs.models import SubClub
from trendles.models import Announcement
from django.utils import timezone
# Create your views here.
def index(request):
    SubClubs=SubClub.objects.all()
    return render(request,'betalabs/index.html',{'SubClubs':SubClubs})
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
  
    return render(request,'betalabs/clubleads.html',{'all_leads': all_leads,'majorclub':'Betalabs','subclub_name':displayClub,'all_leads1': all_leads1,'announcements_two_days_ago':announcements_two_days_ago})
def subclubleads(request):

    subclub_name = request.GET.get('subclub_name')
    majorclub = request.GET.get('majorclub')
    
    displayClub = SubClub.objects.filter(club_name=subclub_name).first()
 
    
    all_leads = []
    
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
    return render(request, 'betalabs/subclubleadstemp.html', {'displayClub': displayClub, 'all_leads': all_leads, 'subclub_name': subclub_name,'majorclub':majorclub,'announcements_two_days_ago':announcements_two_days_ago})
def Bsettings(request):
    return render(request,'Bsettings.html')