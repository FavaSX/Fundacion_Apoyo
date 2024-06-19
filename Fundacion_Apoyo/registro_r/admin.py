from django.contrib import admin
from .models import Residente

class ResidenteAdmin(admin.ModelAdmin):
    list_display = ["rut", "nombre", "edad", "familiar_cargo", "medicamentos", "situacion_salud", "cuidados_especiales"]
    search_fields = ["nombre"]
admin.site.register(Residente, ResidenteAdmin)
