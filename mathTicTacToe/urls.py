from django.conf.urls import url, include
from django.contrib import admin




urlpatterns = [

    url(r'^game', include('apps.game.urls', namespace='game')),
    url(r'^home', include('apps.home.urls', namespace='home')),
    url(r'^', include('apps.login_reg.urls', namespace='login_reg'))
]