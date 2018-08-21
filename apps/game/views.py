from django.shortcuts import render

def index(request):
    return render(request,'game/index.html')

def multiplayer(request):
    return render(request,'game/multiplayer.html')

def player2(request):
    return render(request,'game/player2.html')