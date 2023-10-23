from time import timezone
from django.shortcuts import render
from django.http import HttpResponse
from promocao.models import Promocao
from .models import Mercado  # Importe o modelo de Mercado ]
from django.utils import timezone

def detalhes_mercado(request, pk):
    mercado = Mercado.objects.get(pk=pk)
    return render(request, 'mercado/detalhes_mercado.html', {'mercado': mercado})

def mercado_detalhes(request, pk):
    # Recupere o mercado com base na chave primária (pk) 
    mercado = Mercado.objects.get(id=pk)
    return render(request, 'mercado/detalhes_mercado.html', {'mercado': mercado})

def lista_mercado(request):
    mercado = Mercado.objects.all()  # Corrija o nome da variável para 'mercados'
    return render(request, 'mercado/lista_mercado.html', {'mercado': mercado})

def detalhes_mercado(request, pk):
    now = timezone.now()
    mercado = Mercado.objects.get(pk=pk)
    
    # Consulte as promoções ativas (com data de término maior ou igual à data e hora atuais)
    promocoes_todas = Promocao.objects.filter(data_fim__gte=now).order_by('-id')  # Ordene por 'id' em ordem descendente
    
    # Recupere a lista de promoções relacionadas a este mercado
    promocoes = Promocao.objects.filter(mercado=mercado)
    
    # Crie um contexto com a lista de promoções
    contexto = {'mercado': mercado, 'lista_promocao': promocoes}
    
    return render(request, 'mercado/detalhes_mercado.html', contexto)


