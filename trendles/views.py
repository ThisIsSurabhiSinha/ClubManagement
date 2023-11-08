from django.shortcuts import render,HttpResponse,redirect
from trendles.models import SubClub,LiteraryDocument,ChitrachayaImages,DesignClubFile,MarketingOutreachClubFile,FinanceClubFile
from Home.models import Student,Suggestion,MajorClub
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import os
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from trendles.models import Announcement 

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
    pic=ChitrachayaImages.objects.all()
    return render(request,'trendles/chitrachaya.html',{'subclub_name': "Chitrachaya",'majorclub':"Trendles","pic":pic})
def marketing(request):
    return render(request,'trendles/marketting.html', {'subclub_name': "Marketing and Outreach",'majorclub':"Trendles"})
def designing(request):
    return render(request,'trendles/designing.html',{'subclub_name': "Design",'majorclub':"Trendles"})
def literature(request):
    return render(request,'trendles/literature.html',{'subclub_name': "Literary",'majorclub':"Trendles"})
def debating(request):
    return render(request,'trendles/debating.html',{'subclub_name': "Debate and Quizes",'majorclub':"Trendles"})

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
 
   

    return render(request,'trendles/clubleads.html',{'all_leads': all_leads,'majorclub':'Trendles','subclub_name':displayClub,'all_leads1': all_leads1,'announcements_two_days_ago':announcements_two_days_ago})
def calander(request):
    return render(request,'trendles/calander.html')
def quizclub(request):
    return render(request,'trendles/quizpage.html')
def announcement(request):
    two_days_ago = timezone.now() - timezone.timedelta(days=2)
    announcements_two_days_ago = Announcement.objects.filter(date__gte=two_days_ago)
    print(announcements_two_days_ago)
    return render(request,'trendles/announcements.html',{'announcements_two_days_ago':announcements_two_days_ago})
def elections(request):
     
     majorclub = request.GET.get('majorclub', None)
     
     return render(request,'trendles/elections.html',{'majorclub':majorclub})
def settings(request):
    return render(request,'trendles/settings.html')
@login_required
def profile(request):
    if request.user.is_authenticated:
        user = request.user
        first_name = user.first_name
        last_name = user.last_name
        email = user.email
        student = Student.objects.get(email=email)
        suggestion_by_student=Suggestion.objects.filter(student=student)
        ChitrachayaImages_count=len(ChitrachayaImages.objects.filter(uploaded_by=student))
        Literary_upload_document_count=len(LiteraryDocument.objects.filter(uploaded_by=student))
        desgin_upload_document_count=len(DesignClubFile.objects.filter(uploaded_by=student))
        market_upload_document_count=len(MarketingOutreachClubFile.objects.filter(uploaded_by=student))
        Finance_upload_document_count=len(FinanceClubFile.objects.filter(uploaded_by=student))
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
                

            }
        contributions={'Suggestions':suggestion_count,
                'Chitrachaya':ChitrachayaImages_count,
                'Literature Club':Literary_upload_document_count,
                'Market and Outreach Club':market_upload_document_count,
                'Design Club':desgin_upload_document_count,
                'Finace Club':Finance_upload_document_count

        }
      
        return render(request,'trendles/profile.html',{'student_info': student_info,'contributions':contributions})
    else:
        return HttpResponse("404 Not found")
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
    return render(request, 'trendles/subclubleadstemp.html', {'displayClub': displayClub, 'all_leads': all_leads, 'subclub_name': subclub_name,'majorclub':majorclub,'announcements_two_days_ago':announcements_two_days_ago})

@login_required
def upload_image(request):
    if request.method == "POST":
        if 'file_name' in request.FILES:
           uploaded_file = request.FILES['file_name']
           uploaded_file_name = uploaded_file.name
           l = uploaded_file_name.split('.')
           if len(l) > 1:
                file_extension = l[-1].lower()
           else:
                # Handle the case where there is no file extension
                file_extension = ''
        else:
         
            messages.error(request, 'No file attached. Please select a file to upload.')
            return redirect("chitrachaya")
        
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
            media_file=uploaded_file,
            upload_date=timezone.now(),
            subclub_name=club_id,
            majorclub_name=majorlcub_id,
        )
        image.save()
        messages.success(request, '🙌 Upload complete! Your pictures and videos are now part of our collection. 📸🎥')
        return redirect('chitrachaya')
        
    messages.error(request, 'Attempt failed !! Please try again.')
    return redirect( 'chitrachaya')
@login_required
def Literary_upload_document(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']

        # Check if a file is attached in the request
        if 'document' in request.FILES:
            document = request.FILES['document']

            # Create a new LiteraryDocument instance and save the file
        student = get_object_or_404(Student, student_id=request.user.username)
        literary_document = LiteraryDocument(
                title=title,
                document=document,
                uploaded_by=student,  # Assuming request.user is the Student instance
                description=description,
                upload_date=timezone.now(),
                subclub_name="Literary",  # Update with the actual subclub name
                majorclub_name="Trendles",
                user=request.user  # Update with the actual major club name
            )
        literary_document.save()

        messages.success(request,'🙌 Thank you for sharing your work with us! Your contribution is greatly appreciated and will help enrich our club\'s collection.📚📖🖋️📝')
    else:
            messages.error(request, 'No file attached. Please select a file to upload.')

    return redirect("literature")



@login_required
def design_club_upload_document(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']

        # Check if a file is attached in the request
        if 'document' in request.FILES:
            document = request.FILES['document']
        else:
             
            messages.error(request, 'No file attached. Please select a file to upload.')
            return redirect("designing")
            # Create a new DesignClubFile instance and save the file
        student = get_object_or_404(Student, student_id=request.user.username)
        design_document = DesignClubFile(
            title=title,
            description=description,
            file=document,
            uploaded_by=student,
            user=request.user,
            upload_date=timezone.now(),
            subclub_name="Design",  # Update with the actual subclub name
            majorclub_name="Trendles",  # Update with the actual major club name
        )
        design_document.save()

        messages.success(request, '🙌 Thank you for sharing your work with us! Your contribution is greatly appreciated and will help enrich our club\'s collection.🎨💡')
    else:
            messages.error(request, 'Unsuccessful attempt.Please try again.')

    return redirect("designing")  # Update the URL pattern name for the design club page
@login_required
def finance_club_upload_document(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']

        # Check if a file is attached in the request
        if 'document' in request.FILES:
            document = request.FILES['document']
        else:
             
            messages.error(request, 'No file attached. Please select a file to upload.')
            return redirect("finance")

            # Create a new FinanceClubFile instance and save the file
        student = get_object_or_404(Student, student_id=request.user.username)
        finance_document = FinanceClubFile(
                title=title,
                description=description,
                file=document,
                uploaded_by=student,
                user=request.user,
                upload_date=timezone.now(),
                subclub_name="Finance",  # Update with the actual subclub name
                majorclub_name="Trendles",  # Update with the actual major club name
            )
        finance_document.save()

        messages.success(request, '🙌 Thank you for sharing your work with us! Your contribution is greatly appreciated and will help enrich our club\'s collection. 📈💰💼')
    else:
            messages.error(request, 'Unsuccessful attempt.Please try again.')

    return redirect("finance")
@login_required
def market_club_upload_document(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']

        # Check if a file is attached in the request
        if 'document' in request.FILES:
            document = request.FILES['document']
        else:
             
            messages.error(request, 'No file attached. Please select a file to upload.')
            return redirect("marketing")

            # Create a new FinanceClubFile instance and save the file
        student = get_object_or_404(Student, student_id=request.user.username)
        market_document = MarketingOutreachClubFile(
                title=title,
                description=description,
                file=document,
                uploaded_by=student,
                user=request.user,
                upload_date=timezone.now(),
                subclub_name="Marketing and Outreach",  # Update with the actual subclub name
                majorclub_name="Trendles",  # Update with the actual major club name
            )
        market_document.save()

        messages.success(request, '🙌 Thank you for sharing your work with us! Your contribution is greatly appreciated and will help enrich our club\'s collection.📣🌐📈💼')
    else:
            messages.error(request, 'Unsuccessful attempt.Please try again.')

    return redirect("marketing") # Import your Announcement model
@login_required
def create_announcement(request):
    if request.method == 'POST':
        displayClub = SubClub.objects.all()
        displayClub1 = SubClub.objects.all().first()
        all_leads1=[1,2]
        for lead in all_leads1:  
            content = request.POST.get('announcement-text-{}'.format(lead))
            print(content)
            if content:
                user = request.user  # Get the currently logged-in user
                student=student = get_object_or_404(Student, student_id=request.user.username)
                announcement = Announcement(user=user, content=content,uploaded_by=student)
                announcement.save()
       
        two_days_ago = timezone.now() - timezone.timedelta(days=2)
        announcements_two_days_ago = Announcement.objects.filter(date=two_days_ago)
        return redirect('Homepage')
    else:
        return HttpResponse("404 Not found")
    # return render(request, 'clubleads.html',{'announcements_two_days_ago':announcements_two_days_ago})
