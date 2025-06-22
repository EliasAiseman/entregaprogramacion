from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Departamento

class DepartamentoView (TemplateView):
    template_name= 'departamento/departamento.html'

class ListarDepartamentos (ListView):
    template_name = 'departamentos/lista_departamentos.html'
    Model = Departamento
    queryset = Departamento.objects.all()
    context_object_name = 'lista_departamentos'