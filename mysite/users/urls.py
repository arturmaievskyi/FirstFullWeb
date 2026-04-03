from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('settings/', views.profile_settings, name='profile_settings'),
    path('friends/', views.friends, name='friends'),
    path('projects/', views.userProjects, name='user_projects'),
    # path('textes/', views.textes, name='user_textes'),
    path('change_password/', views.change_password, name='change_password')
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)