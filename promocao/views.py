from django.shortcuts import render
from .models import Promocao
from mercado.models import Mercado
from django.urls import reverse


def promocoes(request):
    promocoes_todas = Promocao.objects
    lista_mercado = Mercado.objects.all()
  
    
    saida={"lista_promocao": promocoes_todas.all,"lista_mercado": lista_mercado}
    return render (request, 'promocao/index.html', saida)

    
