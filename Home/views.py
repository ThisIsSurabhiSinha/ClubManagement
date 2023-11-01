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
def show_quiz(request):
    return render (request,"Home/quizpage.html")

def analyze(request):
    l=[0,0,0,0]
    for i in range(1,13):
        value1=request.GET.get('q{}'.format(i))
        #return HttpResponse(value1)
        
        if value1=='a1':
            l[0]=l[0]+1
        elif value1=='a2':
           l[1]=l[1]+1
        elif value1=='a3':
             l[2]=l[2]+1
        elif value1=='a4':
            l[3]=l[3]+1
        print(l[0],l[1],l[2],l[3])
    '''if l[0]>l[1] and l[0]>l[2]:
            return HttpResponse("Your interests match with Wildbeats")
    elif l[1]>l[0] and l[1]>l[2]:
            return HttpResponse("Your interests match with Trendles")
    else:
            return HttpResponse("Your interests match with Sports club")'''
    d={1 :'WILDBEATS' ,
       2 : 'Trendles' ,
       3 :'Sports' ,
       4 :'Technical' ,
       }
    l2=[1,2,3,4]
    for i in range(0,3):
        for j in range(i+1,4):
            if l[j]>l[i]:
                l[j],l[i]=l[i],l[j]
                l2[j],l2[i]=l2[i],l2[j]
    l3=[d[l2[0]],d[l2[1]],d[l2[2]],d[l2[3]]]

    return render(request,"Home/quizresult.html",{ 'my_list' : l3 })
def show_full_result(request):
    return render(request,"Home/quizresult2.html")