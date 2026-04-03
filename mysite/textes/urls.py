from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    # path('', views.textes, name='textes'),
    # path('<int:texte_id>/', views.texte_detail, name='texte_detail'),
    # path('create/', views.create_texte, name='create_texte'),
    # path('<int:texte_id>/edit/', views.edit_texte, name='edit_texte'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)