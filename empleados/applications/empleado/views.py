from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Empleado

class ListarEmpleadosBusqueda(ListView):
    template_name = 'empleado/listar_empleados_busqueda.html'
    model = Empleado
    context_object_name = 'empleados'
    paginate_by = 10  # Opcional: paginación

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Empleado.objects.filter(
                Q(nombre__icontains=query) |
                Q(apellido__icontains=query) |
                Q(email__icontains=query) |
                Q(rol__nombreRol__icontains=query) |
                Q(pais__nombre__icontains=query)
            ).distinct()
        return Empleado.objects.all().select_related('rol', 'pais', 'departamento')

class IndexView (TemplateView):
    template_name= 'empleado/empleado.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empleados=Empleado.objects.all()
        print(empleados)
        context['empleados'] = empleados
        return context


class ModeloPruebaListView(ListView):
    model = Empleado
    template_name = 'empleado/lista-prueba.html'
    context_object_name = 'lista_prueba'

class Listar_todos_los_empleaods(ListView):
    template_name = 'empleados/listar_todos_los_empleados.html'
    model = Empleado

class Listar_todos_los_empleados_por_departamento(ListView):
    template_name = 'empleado/listar_todos_los_empleados_por_departamento.html'
    model = Empleado

    def get_queryset(self):
        departamento = self.kwargs['nombre']
        lista = Empleado.objects.filter(departamento__nombre=departamento)
        return lista