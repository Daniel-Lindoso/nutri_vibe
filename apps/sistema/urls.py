from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar-nutricionista/', views.cadastrar_nutricionista, name='cadastrar_nutricionista'),
    path('cadastrar-paciente/', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('', views.home, name='home'),
]