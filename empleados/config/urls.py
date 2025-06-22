from django.urls import path, include
from django.contrib import admin
from applications.inicio.views import HomeView
from applications.empleado.views import IndexView, ModeloPruebaListView, Listar_todos_los_empleados_por_departamento
from django.views.generic import RedirectView
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/inicio/')),
    path('inicio/', include('applications.inicio.urls')),  # Redirige a la app Inicio
    path('empleados/', include('applications.empleado.urls')),  # Redirige a la app Empleado
    path('departamento/', include('applications.departamento.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)