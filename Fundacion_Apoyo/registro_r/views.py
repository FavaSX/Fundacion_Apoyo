from django.shortcuts import render

def home(request):
    return render(request, 'registro_r/home.html')
def registror(request):
    return render(request, 'registro_r/registror.html')