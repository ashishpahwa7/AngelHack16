from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.user_login, name='user_login'),
    url(r'^home/$', views.home_page, name='home_page'),

]