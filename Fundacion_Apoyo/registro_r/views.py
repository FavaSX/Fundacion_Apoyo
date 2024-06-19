from django.shortcuts import render
from .models import Residente



def home(request):
    return render(request, 'registro_r/home.html')
def registror(request):
    residentes = Residente.objects.all()
    data = {
        'residentes': residentes
    }
    return render(request, 'registro_r/registror.html', data)