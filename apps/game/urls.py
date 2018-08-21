from django.conf.urls import url
from . import views    
app_name = 'game'     
urlpatterns = [
    url(r'^game$', views.index, name='index')
]