from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear-turno/', views.crear_turno, name='crear_turno'),
]