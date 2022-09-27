"""webApp_PrintSoftware URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'), #admin page
    path('dockets/', include('Dockets.urls')), #dockets application
    path('register/', user_views.register, name='register'), #register path
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), #login path
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), #logout path
    path('profile/', user_views.profile, name='profile'), #profile path
    path('resetpassword/', auth_views.PasswordResetView.as_view(), name='reset_password'), #password reset
    path('resetpassword_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), #password reset
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'), #password reset
    path('resetpassword_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), #password reset
]
