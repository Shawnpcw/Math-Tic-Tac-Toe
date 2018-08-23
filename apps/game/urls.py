from django.conf.urls import url
from . import views    
app_name = 'game'     

urlpatterns = [
    url(r'^computer$', views.index, name='index'),
    url(r'^player1/(?P<num>\d+)$', views.multiplayer, name='multiplayer'),
    url(r'^player2/(?P<num>\d+)$', views.player2, name='player2'),
    url(r'^update$', views.update, name='update')
]