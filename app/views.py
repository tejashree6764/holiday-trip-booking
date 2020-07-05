from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from .models import Contact,Post
from .models import Register
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    if not request.user.is_authenticated:
         message.warning(request,"please login and try again")
         return render(request,'login.html')

    return render(request,'home.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        from_email=settings.EMAIL_HOST_USER

        if len(email)<4:
            messages.error(request,'Email is Invalid')
            return render(request,'contact.html')

        if len(phone)>11:
            messages.error(request,'Phone No is Invalid') 
            return render(request,'contact.html')

        if len(desc)<5:
            messages.error(request,'Description is Invalid') 
            return render(request,'contact.html')

        connection=mail.get_connection()
        connection.open()
        email=mail.EmailMessage(name,desc,from_email,['tejashree.katamaiah1999@gmail.com'],connection=connection)
        connection.send_messages([email])
        connection.close()
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()

        messages.success(request,"your response has been recorded and sent")    
    return render(request,'contact.html')

def registration(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        gender=request.POST.get('gender','')
        address1=request.POST.get('address1','')
        address2=request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')

        if len(email)<4:
            messages.error(request,'Email is Invalid')
            return render(request,'registration.html')

        if len(phone)>11:
            messages.error(request,'Phone No is Invalid') 
            return render(request,'registration.html')

       
        register=Register(name=name,email=email,phone=phone,gender=gender,address1=address1,address2=address2,city=city,state=state)
        register.save()
        messages.success(request,"your registration is successfull")    
    return render(request,'registration.html')

def about(request):
    return render(request,'about.html') 

def handleBlog(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please loginand Try Again")
        return render(request,'login.html')
    else:
        allposts=Post.objects.all()
        context={'allposts':allposts}    
    return render(request,'handleBlog.html',context) 


def handleSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1 != pass2:
            messages.warning(request,'password is incorrect')
            return render(request,'index.html')

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Signup successfull")
        return redirect('/login')

    return render(request,'index.html')

def handleLogin(request):
    if request.method=='POST':
        loginusername=request.POST['name']
        loginpassword=request.POST['pass1']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.warning(request,'login Successsfull')
            return render(request,'home.html')
        else:
            messages.error(request,'Invalid credentials')
            return HttpResponse("Invalid credentials")

    return render(request,'login.html')

def handleLogout(request):
 logout(request)
 messages.warning(request,"successfully logged out")
 return redirect('/login')