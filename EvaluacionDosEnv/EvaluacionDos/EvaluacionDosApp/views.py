from django.shortcuts import render
from .models import Automovil
from django.utils import timezone
from django.core.paginator import Paginator
from django.views.generic import ListView
# Create your views here.

def index(request):
    automovil = Automovil.objects.order_by('FechaPublicacion').desc()
    return render(request, 'EvaluacionDosApp/index.html', {'automovil': automovil})

def listar(request):
    autos_lista = Automovil.objects.all()
    context = {'autos' : autos_lista}

    paginator = Paginator(autos_lista, 3)
    page = request.GET.get('page', 1)
    autos = paginator.get_page(page)
    
    return render(request, 'EvaluacionDosApp/index.html', context)

class AutoList(ListView):
    model = Automovil
    template_name = 'EvaluacionDosApp/index.html'
    paginate_by = 3

    