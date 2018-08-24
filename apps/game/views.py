from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.home.models import *

def index(request,num):
    diff= int(num)
    return render(request,'game/index.html',{'difficulty':diff})

def computer(request,num):
    return render(request,'game/computer.html')
    
def multiplayer(request, num):
    request.session['match_id'] = num

    b = openMatches.objects.get(id = num)
    board = b.board
    
    request.session['board'] = board
    request.session['gameId'] = num
    scoreboard = b.scoreboard
    playersTurn = b.playersTurn
    return render(request,'game/multiplayer.html',{'board':board, 'scoreboard': scoreboard,'playersTurn':playersTurn})

def player2(request,num):
    request.session['match_id'] = num
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

def reload(request):
    if 'turn' not in request.session:
        request.session['turn']= 0
    counter = 0
    currentTurn = openMatches.objects.get(id = request.session['match_id']).playersTurn
    print('current turn =',currentTurn)
    print('request.session["turn"] =',request.session['turn'])            
    print(currentTurn)
    return render(request, 'game/reload.html',{'currentTurn':currentTurn})

def incermentTurn(request):
    b =openMatches.objects.get(id = request.session['match_id'])
    print('i wnet hereere')
    if b.playersTurn == 1:
        b.playersTurn = 2
        print('8'*60, b.playersTurn)
    elif b.playersTurn ==2:
        b.playersTurn =1
        print('8'*60, b.playersTurn)
    b.save()
    print(b.playersTurn)
    return render(request, 'game/reload.html',{'currentTurn':b.playersTurn})