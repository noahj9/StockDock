from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dockets-home'),
    path('newDocket/', views.newDocket, name='dockets-new'),
    path('updateDocket/<str:pk>/', views.updateDocket, name='dockets-update'),
    path('deleteDocket/<str:pk>/', views.deleteDocket, name='dockets-delete'),
]
