from django.conf.urls import url
from . import views    
app_name = 'home'     
urlpatterns = [

    url(r'^$', views.index, name='index')  ,
    url(r'^/stats$', views.stats, name='stats'),
    url(r'^/matchRoom$', views.matchRoom, name='matchRoom'),
    url(r'^/createMatch$', views.createMatch, name='createMatch'),
    url(r'^/createMatch/(?P<num>\d+)$', views.addnum, name='addnum'),
    url(r'^/add$', views.add, name='add'),
    url(r'^/delete/(?P<num>\d+)$', views.delete, name='delete'),
    url(r'^/logout$', views.logout, name='logout'),


] 

