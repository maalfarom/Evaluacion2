from django.contrib import admin
from .models import Automovil
from .forms import AutoModelForm

# Register your models here.

class AdminAuto(admin.ModelAdmin):
    form = AutoModelForm
    list_display = ["Marca","Modelo", "Anio", "Color", "NumeroPuertas", "Descripcion", "FechaPublicacion", "Precio"]

admin.site.register(Automovil, AdminAuto)