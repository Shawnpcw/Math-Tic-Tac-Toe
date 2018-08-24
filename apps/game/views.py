from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.home.models import *

def index(request,num):
    diff= int(num)
    return render(request,'game/index.html',{'difficulty':diff})

def computer(request,num):
    return render(request,'game/computer.html')
    
def multiplayer(request, num):
    b = openMatches.objects.get(id = num)
    board = b.board
    
    request.session['board'] = board
    request.session['gameId'] = num
    scoreboard = b.scoreboard
    return render(request,'game/multiplayer.html',{'board':board, 'scoreboard': scoreboard})

def player2(request,num):
    
    board = openMatches.objects.get(id = num).board
    b = openMatches.objects.get(id = num)
    b.attendee = User.objects.get(id = request.session['user_id'])
    
    scoreboard = b.scoreboard
    print(scoreboard)
    b.save()
    request.session['board'] = board
    request.session['gameId'] = num

    return render(request,'game/player2.html',{'board':board, 'scoreboard': scoreboard})

def update(request):

    updateBoard = openMatches.objects.get(id = request.session['gameId'])

    formatedBoard = request.GET['board']

    remove = formatedBoard.replace('"','')
    updateBoard.board = remove
    updateBoard.scoreboard = request.GET['scoreboard']
    print("GET REQUEST", request.GET['scoreboard'])
    updateBoard.save()
   
    return redirect('/gameplayer2/'+request.session['gameId'])

def update1(request):

    updateBoard = openMatches.objects.get(id = request.session['gameId'])

    formatedBoard = request.GET['board']

    remove = formatedBoard.replace('"','')
    updateBoard.board = remove
    updateBoard.scoreboard = request.GET['scoreboard']
    print("GET REQUEST", request.GET['scoreboard'])
    updateBoard.save()
    
    return redirect('/gameplayer1/'+request.session['gameId'])

