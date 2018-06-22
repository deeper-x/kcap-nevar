from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^home_page/$', views.home_page, name='home_page'),
     ]