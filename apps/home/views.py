
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.login_reg.models import *
from apps.home.models import *

from random import randint

def index(request):
    username = User.objects.get(id =request.session['user_id']).username
    print(username)
    if 'match_id' not in request.session:
        request.session['match_id'] = 0
    return render(request, 'home/home.html', {'username':username})
def stats(request):
    
    userinfo={
        'username' : User.objects.get(id =request.session['user_id']).username,
        'gamesWon' : User.objects.get(id =request.session['user_id']).gamesWon,
        'gamesPlayed' : User.objects.get(id =request.session['user_id']).gamesPlayed 
    }    
    return render(request, 'home/stats.html', {'userinfo':userinfo})

def matchRoom(request):

    otherUser = 0
    myGames = openMatches.objects.filter(creator = User.objects.get(id = request.session['user_id']))
    
    openGames = openMatches.objects.exclude(creator = User.objects.get(id = request.session['user_id']))
    if myGames:
        if myGames[0].attendee_id !=1:
            print('it changed!')
            otherUser = 1
    return render (request, 'home/matchRoom.html', {'myGames': myGames, 'openGames': openGames, 'otherUser':otherUser})

def createMatch(request):

    return render(request, 'home/create.html')

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
    count = 0
    for i in range(0, 3):
        stri +='<tr>'
        for j in range(0, 3):
            e = equation()
            stri += '<td class = '+str(e['answer'])+' id = '+str(count)+'>'+str(e['equation'])+'</td>'
            count +=1
        stri+='</tr>'
    

    if openMatches.objects.filter(creator = request.session['user_id']).exists():
        b=openMatches.objects.get(creator = request.session['user_id'])
        b.difficulty = request.POST['Difficulty']
        b.board = stri
        b.save()
    else:
        i = openMatches.objects.create(board = stri, difficulty = request.POST['Difficulty'], creator = User.objects.get(id= request.session['user_id']), attendee = User.objects.get(id=1))
        
    return redirect('home:matchRoom')

def addnum(request,num):
    
    def equation():
        signs = ['+','-','x','/']
        sign = randint(0,int(num)-1)
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
    count = 0
    for i in range(0, 3):
        stri +='<tr>'
        for j in range(0, 3):
            e = equation()
            stri += '<td class = '+str(e['answer'])+' id = '+str(count)+'>'+str(e['equation'])+'</td>'
            count +=1
        stri+='</tr>'
    

    if openMatches.objects.filter(creator = request.session['user_id']).exists():
        b=openMatches.objects.get(creator = request.session['user_id'])
        b.difficulty = num
        b.board = stri
        b.save()
    else:
        i = openMatches.objects.create(board = stri, difficulty = num, creator = User.objects.get(id= request.session['user_id']), attendee = User.objects.get(id=1))
        
    return redirect('home:matchRoom')

def logout(request):
    request.session.clear()

    return redirect('login_reg:index')
def delete(request, num):
    b = openMatches.objects.get(id = num)
    b.delete()
    return redirect('home:matchRoom')

