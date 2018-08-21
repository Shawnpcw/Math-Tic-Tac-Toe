
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.login_reg.models import *


def index(request):
    username = User.objects.get(id =request.session['user_id']).username

    
    return render(request, 'home/home.html', {'username':username})
def stats(request):
    userinfo={
        'username' : User.objects.get(id =request.session['user_id']).username,
        'gamesWon' : User.objects.get(id =request.session['user_id']).gamesWon,
        'gamesPlayed' : User.objects.get(id =request.session['user_id']).gamesPlayed 
    }

    
    return render(request, 'home/stats.html', {'userinfo':userinfo})

