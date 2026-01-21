from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('projects/', include('projects.urls')),
]