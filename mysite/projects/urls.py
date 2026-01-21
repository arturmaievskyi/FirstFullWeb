from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.projects, name='Projects'),
    path('<int:project_id>/', views.project_detail, name='Project Details and Testing'),
    
]