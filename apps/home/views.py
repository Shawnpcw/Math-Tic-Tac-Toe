
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.login_reg.models import *
from .models import *
from random import randint

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
    return render (request, 'home/matchRoom.html', {'myGames': myGames, 'openGames': openGames})

def startgame(request):

    return render(request, 'home/startgame.html')

def add(request):
    def equation():
        signs = ['+','-','x','/']
        sign = randint(0,int(request.POST['Difficulty'])-1)
        num1 = randint(1,10)
        num2 = randint(1,10)
        if(num2>num1):
            temp = num1
            num1 = num2
            num2 = num1
        if (sign ==3):
            if(num2 ==0):
                num2 =1
            num1 = num2 * randint(1,10)
        
        

        eq = str(num1) +' '+str(signs[sign])+' '+ str(num2)
        if (sign ==1):
            ans = num1 - num2
        elif (sign == 0):
            ans = num1 +num2
        elif (sign == 2):
            ans = num1 * num2
        elif (sign == 3):
            ans = int(num1/num2)
        square = {
                    'equation': eq,
                    'answer' : ans,
                }
        return square
    stri = ""
    for i in range(0, 3):
        stri +='<tr>'
        for j in range(0, 3):
            e = equation()
            stri += '<td class = '+str(e['answer'])+' id = '+str(i)+''+str(j)+'>'+str(e['equation'])+'</td>'
        stri+='</tr>'
    

    
    openMatches.objects.create(board = stri, diffiliculty = request.POST['Difficulty'], creator = User.objects.get(id= request.session['user_id']))
    
    return redirect('/homematchRoom')

