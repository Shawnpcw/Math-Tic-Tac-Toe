from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index(request):
    return render(request,'game/index.html')

def multiplayer(request, num):
    return render(request,'game/multiplayer.html')

def player2(request,num):
    return render(request,'game/player2.html')
