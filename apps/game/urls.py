from django.conf.urls import url
from . import views    
app_name = 'game'     

urlpatterns = [
    url(r'^computer/(?P<num>\d+)$', views.index, name='index'), 
    url(r'^/reloadDiv$', views.reload, name='reloadDiv'), 
    url(r'^/incermentTurn$', views.incermentTurn, name='incermentTurn'), 
    url(r'^player1/(?P<num>\d+)$', views.multiplayer, name='multiplayer'),
    url(r'^player2/(?P<num>\d+)$', views.player2, name='player2'),
    url(r'^update$', views.update, name='update'),
    url(r'^update1$', views.update1, name='update1')
]