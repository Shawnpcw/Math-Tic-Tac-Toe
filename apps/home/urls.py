from django.conf.urls import url
from . import views    
app_name = 'home'     
urlpatterns = [
    url(r'^$', views.index, name='index')  ,
    url(r'^stats$', views.stats, name='stats')  ,
    url(r'^start_game$', views.start_game, name='start_game')  ,



] 