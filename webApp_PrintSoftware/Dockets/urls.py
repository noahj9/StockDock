from django.urls import path
from . import views
from .views import ContactCreate, CreateDocket

urlpatterns = [
    path('', views.home, name='dockets-home'),
    path('newDocket/', CreateDocket.as_view(), name='dockets-new'),
    path('updateDocket/<str:pk>/', views.updateDocket, name='dockets-update'),
    path('deleteDocket/<str:pk>/', views.deleteDocket, name='dockets-delete'),
    path('printDocket/<str:pk>/', views.printDocket, name='dockets-print'),
    # path('contact-create', ContactCreate.as_view(), name='contact-create')
    # path('cloneDocket/<str:pk>/', views.cloneDocket, name='dockets-clone'),
]

