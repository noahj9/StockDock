from django.urls import path, re_path
from . import views
from .views import ContactCreate, CreateDocket

urlpatterns = [
    path('', views.home, name='dockets-home'),
    path('newDocket/', CreateDocket.as_view(), name='dockets-new'),
    path('updateDocket/<str:pk>/', views.updateDocket, name='dockets-update'),
    path('deleteDocket/<str:pk>/', views.deleteDocket, name='dockets-delete'),
    path('printDocket/<str:pk>/', views.printDocket, name='dockets-print'),
    re_path(r'^create-contact/$', ContactCreate.as_view(), name='contact-create'),
    path('cloneDocket/<str:pk>/', views.cloneDocket, name='dockets-clone'),
    path('addJob/<str:pk>/', views.addJob, name='dockets-addJob'),
    path('ajax/update_subCat/', views.updateSubCats, name='get_contactInfo_ajax'),
]

