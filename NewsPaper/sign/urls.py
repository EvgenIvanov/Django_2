from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, upgarde_me, UserProfile, subscribe

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='signup.html'), name='signup'),
    path('upgrade/', upgarde_me, name='upgrade'),
    path('subscribe/', subscribe, name='subscribe'),
    path('profile/', UserProfile.as_view(template_name='user_profile.html'), name='user_profile'),
]