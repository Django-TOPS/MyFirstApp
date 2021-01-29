from django.shortcuts import render,HttpResponse,redirect
from .models import Student,signup,mypost
from .forms import StudentForm,SignupForm,MyPostForm
from django.core.mail import send_mail
from MyWebSite import settings
import random
from twilio.rest import Client
from django.contrib.auth import logout


# Create your views here.
def index(request):
    if request.method=='POST':
        if request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            stid=signup.objects.get(username=unm)

            user=signup.objects.filter(username=unm,password=pas)
            if user:
                request.session['userid']=unm
                request.session['stid']=stid.id
                print('Login Successfully!')
                return redirect('profile')
            else:
                print('Error...Invalid User!')
        elif request.POST.get('signup')=='signup':
            signupfrm=SignupForm(request.POST)
            if signupfrm.is_valid():
                signupfrm.save()
                print("Signup Successfully!")
                return redirect('profile')
            else:
                print(signupfrm.errors)
    else:
        signupfrm=SignupForm()
        print("Error...Somthing went wrong..")
    return render(request,'index.html',{'signupfrm':signupfrm})
   


def profile(request):
    uid=request.session.get('userid')
    if request.method=='POST':
        mypostfrm=MyPostForm(request.POST,request.FILES)
        if mypostfrm.is_valid():
            mypostfrm.save()
            print("Your Post has been uploaded!")
            return redirect('/')
        else:
            print(mypostfrm.errors)
    else:
        mypostfrm=MyPostForm()
    return render(request,'profile.html',{'mypostfrm':mypostfrm,'userid':uid})

def updatestudent(request,id):
    if request.method=='POST':
        myfrm=StudentForm(request.POST)
        id=Student.objects.get(id=id)
        if myfrm.is_valid():
            myfrm=StudentForm(request.POST,instance=id)
            myfrm.save()
            return redirect('profile')
        else:
            print(myfrm.errors)
    else:
        myfrm=StudentForm()
    return render(request,'updatestudent.html',{'myfrm':myfrm,'stdata':Student.objects.get(id=id)})

def deleteprofile(request,id):
    st=Student.objects.get(id=id)
    st.delete()
    return redirect('profile')

def student(request):
    if request.method=='POST':
        myfrm=StudentForm(request.POST)
        if myfrm.is_valid():
            myfrm.save()
            return redirect('profile')
            print('Record Inserted Successfully!')
        else:
            print(myfrm.errors)
    else:
        myfrm=StudentForm()
    return render(request,'student.html')

def studentdata(request):
    uid=request.session.get('userid')
    return render(request,'studentdata.html',{'stdata':Student.objects.all,'uid':uid})

def updateprofile(request):
    uid=request.session.get('userid')
    stid=request.session.get('stid')
    if request.method=='POST':
        myfrm=SignupForm(request.POST)
        id=signup.objects.get(id=stid)
        if myfrm.is_valid():
            myfrm=SignupForm(request.POST,instance=id)
            myfrm.save()
            print("Your profile has been updated!")
            return redirect('profile')
        else:
            print(myfrm.errors)
    else:
        myfrm=SignupForm()
    return render(request,'updateprofile.html',{'uid':uid,'stid':signup.objects.get(id=stid)})


def user_logout(request):
    logout(request)
    return redirect('/')