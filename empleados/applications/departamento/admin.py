from django.contrib import admin
from atexit import register
from .models import Departamento
# Register your models here.

admin.site.register(Departamento)