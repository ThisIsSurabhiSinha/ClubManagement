from django.shortcuts import render,HttpResponse,redirect
from Home.models import MajorClub,RelatedClub,Student
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import Group
import re


# Create your views here.
def is_valid_name(name):
    # Check if the name is not empty
    return name.strip() != ""

def is_valid_username(username):
    # Check if the username follows the specified format
    return re.match(r'^\d{4}[A-Za-z]{3}\d{4}$', username) is not None

def is_valid_phone(phone):
    # Check if the phone number contains 10 digits
    return phone.isdigit() and len(phone) == 10

def is_valid_password(password, cpassword):
    # Check if the password and confirm password match
    return password == cpassword

def is_valid_email(email):
    # Check if the email ends with "@iiitkottayam.ac.in"
    return email.endswith("@iiitkottayam.ac.in")

def index(request):
   major_clubs=MajorClub.objects.all()
   return render(request,'Home/home.html',{'major_clubs':major_clubs})

def countdown(request):
    return render(request,'Home/countdown.html')
def kh(request):
    return render(request,'Home/kh.html')
def details(request):
    return render(request,'Home/detail.html')
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
            if not ((is_valid_name(fname) and is_valid_name(lname) )):
                messages.error(request,"First name and last name must be filled")
                return redirect('view_signup')
            if not is_valid_username(username):
                messages.error(request,"Invalid username.Use your college Roll number as username")
                return redirect('view_signup')
            if not is_valid_email(email):
                messages.error(request,"Invalid email.Please use your college email id")
                return redirect('view_signup')
            if not is_valid_phone(phone):
                messages.error(request,"Invalid phone number.")
                return redirect('view_signup')
            if not is_valid_password(cpassword,password):
                messages.error(request,"Passwords didn't match.")
                return redirect('view_signup')
            if User.objects.filter(email=email).exists():
                messages.error(request, f'{email} is already registered. Please log in.')
                return redirect('login')
                 
            else:
                new_user=User.objects.create_user(username=username,email=email,password=password,first_name=fname,last_name=lname)
                new_user.save()
                student_group = Group.objects.get(name='Student')
                student_group.user_set.add(new_user)
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
            # messages.error(request,"Please try again")
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
            messages.success(request, f'{user.username} Logged in')
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
def show_quiz(request):
    return render (request,"Home/quizpage.html")

def analyze(request):
    l=[0,0,0,0]
    for i in range(1,13):
        value1=request.GET.get('q{}'.format(i))
                
        if value1=='a1':
            l[0]=l[0]+1
        elif value1=='a2':
           l[1]=l[1]+1
        elif value1=='a3':
             l[2]=l[2]+1
        elif value1=='a4':
            l[3]=l[3]+1
    
    d={1 :'WILDBEATS' ,
       2 : 'TRENDLES' ,
       3 :'SPORTEC' ,
       4 :'BETALABS' ,
       }
    l2=[1,2,3,4]
    for i in range(0,3):
        for j in range(i+1,4):
            if l[j]>l[i]:
                l[j],l[i]=l[i],l[j]
                l2[j],l2[i]=l2[i],l2[j]
    l3=[d[l2[0]],d[l2[1]],d[l2[2]],d[l2[3]]]
    dictt={'mylist':l3}

    return render(request,"Home/quizresult.html",{ 'my_list' : dictt })
def show_full_result(request):
    mylist= request.GET.get('all', '').split(',')
    return render(request,"Home/quizresult2.html",{'mylist':mylist})
def custom_login_view(request):
    # Check if the user is authorized to access the admin page
    if not request.user.is_staff:
        return HttpResponse("<h1><center>You are not authorized to view this page</center></h1>", status=401)  # Replace this with your desired response

    # If authorized, redirect to the default admin login view
    
    return login(request)

def is_valid_name(name):
    # Check if the name is not empty
    return name.strip() != ""

def is_valid_username(username):
    # Check if the username follows the specified format
    return re.match(r'^\d{4}[A-Za-z]{3}\d{4}$', username) is not None

def is_valid_phone(phone):
    # Check if the phone number contains 10 digits
    return phone.isdigit() and len(phone) == 10

def is_valid_password(password, cpassword):
    # Check if the password and confirm password match
    return password == cpassword

def is_valid_email(email):
    # Check if the email ends with "@iiitkottayam.ac.in"
    return email.endswith("@iiitkottayam.ac.in")
