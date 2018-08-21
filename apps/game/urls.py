from django.conf.urls import url
from . import views    
app_name = 'game'     
urlpatterns = [
    url(r'^computer$', views.index, name='index'),
    url(r'^player1$', views.multiplayer, name='multiplayer'),
    url(r'^player2$', views.player2, name='player2')
]