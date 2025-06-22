from django.urls import path
from .views import DepartamentoView

urlpatterns = [
    path('', DepartamentoView.as_view(), name='home_departamento')
]

