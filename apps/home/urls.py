from django.conf.urls import url
from . import views    
app_name = 'home'     
urlpatterns = [

    url(r'^$', views.index, name='index')  ,
<<<<<<< HEAD
    url(r'^stats$', views.stats, name='stats')  ,
    url(r'^start_game$', views.start_game, name='start_game')  ,
=======
    url(r'^stats$', views.stats, name='stats'),
    url(r'^matchRoom$', views.matchRoom, name='matchRoom'),
    url(r'^createMatch$', views.createMatch, name='createMatch'),
    url(r'^add$', views.add, name='add')
>>>>>>> origin/Cbranch


] 

