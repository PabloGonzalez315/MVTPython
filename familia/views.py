from django.shortcuts import render
from .models import Integrante


# Create your views here.
def home (request):
    integrantes = Integrante.objects.all()
    return render(request, 'integrante.html',{'integrante': integrantes})