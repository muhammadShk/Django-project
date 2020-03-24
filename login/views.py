from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'gate.html')

def logout(request):
    request.session.clear()
    return redirect('/')    

def register(request):
    for key in request.POST:
        print(request.POST[key])
    errors=User.objects.registration_validator(request.POST)
    for key in errors:
        print(key)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        hashed_pw= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print(hashed_pw)
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password= hashed_pw
        )
        fresh_user=User.objects.last()
        request.session['user_id']= fresh_user.id
        return redirect('/wall')

def login(request):
    errors=User.objects.login_validator(request.POST)
    for key in errors:
        print(key)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        print("email ok")
        potential_user= User.objects.filter(email=request.POST['login_email'])[0]
        if bcrypt.checkpw(request.POST['login_password'].encode(), potential_user.password.encode()):
            print("password ok")
            request.session['user_id']=potential_user.id
            return redirect('/wall')
        else:
            messages.error(request, "Invalid Login", extra_tags='Login_password')
            return redirect('/')

##################################################################################################################

def dashboard(request):
    if 'user_id' in request.session:
        context={
            'logged_in_user': User.objects.get(id= request.session['user_id']) 
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect("/")
