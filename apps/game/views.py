from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index(request):
        
    return HttpResponse("hello")