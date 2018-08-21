from django.shortcuts import render

def index(request):
    return render(request,'game/index.html')

def player1(request):
    return render(request,'game/player1.html')

def player2(request):
    return render(request,'game/player2.html')