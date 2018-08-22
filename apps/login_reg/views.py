from django.shortcuts import render, redirect
from apps.login_reg.models import *
from django.contrib import messages

def index(request):

    
    if 'username' not in request.session:
        request.session['username'] = ''     
    if 'current_username' not in request.session:
        request.session['current_username'] = ''         
    return render(request,'login_reg/index.html')
def create_user(request):

    response = User.objects.basic_validator(request.POST)
    if 'errors' in response:
        for error in response['errors']:
            messages.error(request,error)
        print(messages.error)
        return redirect('login_reg:index')
        
    else:
        request.session['user_id'] = response['user_id']
        request.session['username'] = request.POST['username']      
        return redirect('home:index')     
def login_user(request):
    response = User.objects.login_validator(request.POST)
    if 'errors' in response:
        for error in response['errors']:
            messages.error(request,error)
        return redirect('login_reg:index')
    else:
        request.session['user_id'] = response['user_id']     
        request.session['username'] = request.POST['username']
        return redirect('home:index')  
def logout(request):
    del request.session['user_id']
    
    return redirect('login_reg:index')

