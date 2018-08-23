from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.home.models import *

def index(request):
    return render(request,'game/index.html')

def computer(request):
    return render(request,'game/computer.html')
    
def multiplayer(request, num):
    board = openMatches.objects.get(id = num).board
    request.session['board'] = board
    print(board)
    return render(request,'game/multiplayer.html',{'board':board})

def player2(request,num):
    board = openMatches.objects.get(id = num).board
    b = openMatches.objects.get(id = num)
    b.attendee = User.objects.get(id = request.session['user_id'])
    b.save()
    request.session['board'] = board
    return render(request,'game/player2.html',{'board':board})
