from django.shortcuts import render
from .models import Cafe

def home(request):
    # Pega todos os cafés que estão com status APROVADO
    cafes = Cafe.objects.filter(status='APROVADO')
    
    return render(request, 'core/index.html', {'cafes': cafes})