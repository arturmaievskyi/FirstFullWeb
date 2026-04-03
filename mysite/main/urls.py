from django.urls import path, include
from .views import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('settings/', views.settings, name='settings'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('projects/', include('projects.urls')),
    path('textes/', include('textes.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)