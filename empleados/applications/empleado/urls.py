from django.urls import path
from .views import IndexView
from applications.empleado.views import ModeloPruebaListView
from .views import ListarEmpleadosBusqueda



urlpatterns = [
    path('buscar/', ListarEmpleadosBusqueda.as_view(), name='buscar_empleados'),
    path('', IndexView.as_view(), name='home_empleado'),  # Página principal de la aplicación Empleado
    path('prueba/', ModeloPruebaListView.as_view(), name='prueba'),

]