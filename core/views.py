from django.shortcuts import render, redirect
from django.contrib import messages
from ..login.models import *

def index(request):
    context={
            'logged_in_user': User.objects.get(id= request.session['user_id']) 
        }
    return render(request, 'index.html', context)
