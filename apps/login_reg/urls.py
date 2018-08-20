from django.conf.urls import url
from . import views    
app_name = 'login_reg'     
urlpatterns = [
    url(r'^$', views.index, name='index')  ,
    url(r'create_user$', views.create_user, name='create_user')  , 
    url(r'login_user$', views.login_user, name='login_user')  ,


]