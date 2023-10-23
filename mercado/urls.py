from django.urls import path
from . import views

urlpatterns = [
    path('mercado/', views.lista_mercado, name='lista_mercado'),
    path('mercado/<int:pk>/', views.detalhes_mercado, name='detalhes_mercado'),
    
   
   
    ]
