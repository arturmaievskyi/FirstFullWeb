from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.projects, name='Projects'),
    path('<int:project_id>/', views.project_detail, name='Project Details and Testing'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)