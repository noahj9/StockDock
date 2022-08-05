from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dockets-home'),
    path('new/', views.newDocket, name='dockets-new'),
]
