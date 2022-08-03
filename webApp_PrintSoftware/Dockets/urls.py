from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dockets-home'),
    path('new/', views.new, name='dockets-new'),
]
