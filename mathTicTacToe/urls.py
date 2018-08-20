from django.conf.urls import url, include
urlpatterns = [
    url(r'', include('apps.login_reg.urls')),
    url(r'/home', include('apps.game.urls'))  
]