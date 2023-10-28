from django.shortcuts import render,HttpResponse,redirect
from Home.models import MajorClub,RelatedClub,Student
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout


# Create your views here.
def index(request):
   major_clubs=MajorClub.objects.all()
   return render(request,'Home/home.html',{'major_clubs':major_clubs})


def handle_signup(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            fname =  request.POST.get('fname')
            lname = request.POST.get('lname')
            password =  request.POST.get('password')
            email = request.POST.get('email')
            cpassword =  request.POST.get('cpassword')
            phone = request.POST.get('phone')
            program = request.POST.get('program')
            department = request.POST.get('department')
            batch = request.POST.get('batch')
            # dob = request.POST.get('dob')
            # linkedin_profile=request.POST.get('linkedin_profile')

        
            if User.objects.filter(email=email).exists():
                messages.error(request, f'{email} is already registered. Please log in.')
                return redirect('login')
                 
            else:
                new_user=User.objects.create_user(username=username,email=email,password=password,first_name=fname,last_name=lname)
                new_user.save()
                messages.success(request, f' {fname} {lname} is successfully registered !')
                student = Student(
                    student_id=username,
                    first_name=fname,
                    last_name=lname,
                    # date_of_birth=dob,
                    email=email,
                    phone_number=phone,
                    program=program,
                    department=department,
                    batch=batch,
                    # linkedin_profile=linkedin_profile
        )
                student.save()
                return redirect('Homepage')
    else:
            messages.error(request,"Please try again")
            return redirect('view_signup')

   
def view_signup(request):
    return render(request,'Home/signup.html')
def  view_login(request):
    return render(request,'Home/loginpage.html')
def handle_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password =  request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
  
            login(request, user)
            messages.success(request, 'Logged in')
            return redirect('Homepage')  
        else:
           
            messages.error(request, 'Invalid email or password. Please try again.')
            return redirect('login') 
    else:
        messages.error(request,"Please try again")
        return redirect('login')

  
def handle_logout(request):
        logout(request)
        messages.success(request,"Logged out successfully")
        return redirect('Homepage')
