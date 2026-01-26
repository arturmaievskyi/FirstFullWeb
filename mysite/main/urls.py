from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    # path('projects/', include('projects.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)