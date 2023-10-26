from django.shortcuts import render
from . import validate
from .models import Otp
from .models import Client
from home.views import home
import random
from django.shortcuts import redirect

def index(request):
    if validate.alreadyLoggedIN(request):
        return redirect("/home")
    #print(request.POST['exampleInputEmail1'])
    return render(request, 'home/landingpage.html', {})


def sendOTP(request):
    print("IN sendOtp",request.POST)
    try:
        k = request.POST
        email = k['email']
        res = validate.validateEmail(email) 
        request.session['email'] = email
        if res:
            otp = random.randint(10000,99999)
            request.session['otp'] = otp
            validate.sendOTP(otp,email)
            return render(request, 'home/otp.html', {'email':request.session['email']})
        return render(request, 'home/landingpage.html', {'message':'email already exists'})
    except:
        return render(request, 'home/landingpage.html', {})


def verifyemail(request):
    otp = request.POST['otp'] 
    print(otp,request.session['otp'])
    if int(otp)==int(request.session['otp']):
        print("correct otp")
        return render(request, 'home/signup.html')
    else:
        print("wrong otp")
    return render(request, 'home/otp.html', {'alert':'sorry wrong otp','email':request.session['email']})
    #print('otp',k)


def signupwithemail(request):
    return render(request,'home/email.html')


def signup(request):
    try:
        obj = Client(email=request.session['email'],password=request.POST['password'],username=request.POST['username'])
        obj.save()
        print(obj)
        return redirect('/home')
    except:
        return render(request, 'home/landingpage.html')

def login(request):
    print(request.POST)
    try:
        if not validate.validateLogIn(request.session['username'],request.session['password']):
            raise Exception("INvalid login")
        print("already has session")
        return redirect('/home')
    except:
        print("no session")
    print(request.POST)
    try:
        obj = Client.objects.all().filter(username=request.POST['username'])
        print(obj)
        if len(obj)==0:
            print("incorrect email")
            return render(request, 'home/landingpage.html',{'message':'INcorrect password'})
        else:
            print("crct email")
            if obj[0].password==request.POST['password']:
                print("succesful login")
                request.session['username'] = request.POST['username']
                request.session['password'] = request.POST['password']
                return redirect("/home")
            else:
                print("incorrect password")
                return render(request, 'home/landingpage.html',{'message':'INcorrect password'})
        print(obj)
        return redirect("/home")
    except:
        print("email")
        return redirect("/")
        
def logout(request):
    request.session.clear()
    print('cleared')
    return redirect('/login/')

def tmp(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/')
    return home(request)

    #print('otp',k)

# Create your views here.
