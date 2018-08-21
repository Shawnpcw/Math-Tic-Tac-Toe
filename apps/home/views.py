
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.login_reg.models import *
from .models import *

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

def matchRoom(request):
    opponentInfo = User.objects.all()
    gameInfo = Game.objects.all()
    
    myGames = openMatches.objects.all()
    openGames = openMatches.objects.exclude(creator = User.objects.get(id = request.session['user_id']))
    print(myGames)
    return render (request, 'home/matchRoom.html', {'myGames': myGames, 'openGames': openGames})

def createMatch(request):

    return render(request, 'home/create.html')

def add(request):

    openMatches.objects.create(diffiliculty = request.POST['Difficulty'], creator = User.objects.get(id= request.session['user_id']))
    
    return redirect('/homematchRoom')

