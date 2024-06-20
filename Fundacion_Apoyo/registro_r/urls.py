from django.urls import path
from .views import home, registror, agregar_residente, modificar_residente, eliminar_residente
urlpatterns = [
    path('', home, name="home"),
    path('registror/', registror, name='registror'),
    path('agregar-residente/', agregar_residente, name="agregar_residente"),
    path('modificar-residente/<rut>/', modificar_residente, name="modificar_residente"),
    path('eliminar-residente/<rut>/', eliminar_residente, name="eliminar_residente")
]
