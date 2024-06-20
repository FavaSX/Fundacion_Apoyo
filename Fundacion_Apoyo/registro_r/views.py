from django.shortcuts import render, redirect, get_object_or_404
from .models import Residente
from .forms import ResidenteForm


def home(request):
    return render(request, 'registro_r/home.html')
def registror(request):
    residentes = Residente.objects.all()
    data = {
        'residentes': residentes
    }
    return render(request, 'registro_r/residente/registror.html', data)

def agregar_residente(request):
    data  = {
        'form': ResidenteForm()
    }
    
    if request.method== 'POST':
        formulario = ResidenteForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'registro_r/residente/agregar.html', data)


def modificar_residente(request, rut):
    residente = get_object_or_404(Residente, rut=rut)
    data = {
        'form': ResidenteForm(instance=residente)
    }
    if request.method == 'POST':
        formulario = ResidenteForm(data=request.POST, instance=residente,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="registror")
        data["form"] = formulario
    return render(request, 'registro_r/residente/modificar.html', data)


def eliminar_residente(request, rut):
    residente = get_object_or_404(Residente, rut=rut)
    residente.delete()
    return redirect(to="registror")