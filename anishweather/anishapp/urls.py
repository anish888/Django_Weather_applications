from django.urls import path
from . import views
  
urlpatterns = [

    path('',views.index),
    path('index', views.index,name='index'),
    path('home',views.home,name='home'),
    path('detail',views.detail,name='detail'),
    path('contact',views.contact,name='contact')
]