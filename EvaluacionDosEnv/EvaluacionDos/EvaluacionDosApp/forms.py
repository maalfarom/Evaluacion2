from django import forms
from .models import Automovil

class AutoModelForm(forms.ModelForm):
    class Meta:
        model = Automovil
        fields = ["Marca","Modelo","Anio","Color","NumeroPuertas","Descripcion","Precio"]
