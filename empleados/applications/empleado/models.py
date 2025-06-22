from django.db import models
from applications.departamento.models import Departamento
from django_ckeditor_5.fields import CKEditor5Field
from django.db.models import Q


class Habilidades(models.Model):
    habilidad = models.CharField('habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades del empleado'
        ordering = ['habilidad']
        unique_together = ('habilidad',)

    def __str__(self):
        return self.habilidad 
    
class Rol(models.Model):
    nombreRol = models.CharField('Rol', max_length = 20, blank=True)
    habilidadesRol = models.ManyToManyField(Habilidades)
    
    class Meta:
        verbose_name = 'Rol/Trabajo'
        verbose_name_plural = 'Roles/Trabajos'
        ordering = ['nombreRol']
    
    def __str__(self):
        return f'{self.nombreRol}'
class Pais (models.Model):
    nombre = models.CharField('Pais', max_length=50, unique=True)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Empleado (models.Model):


    JOB_CHOICES =(
        ('0', 'Contador'),
        ('1', 'Administrativo'),
        ('2', 'Desarrollador'),
        ('3', 'Analista Funcional'),
        ('4', 'Otro'),
    )

    nombre = models.CharField('Nombre', max_length=60)
    apellido = models.CharField('Apellido', max_length=60)
    rol = models.ForeignKey('Rol', on_delete=models.SET_NULL, null=True, blank=True)
    email = models.CharField('Email', blank=True)
    fecha_nac = models.DateField('Fecha de Nacimiento', auto_now=False, auto_now_add=False)
    trabajo = models.CharField('Puesto', max_length=1, choices= JOB_CHOICES)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    observaciones = CKEditor5Field(config_name='default', blank = True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['apellido', 'nombre']
        unique_together = ('nombre', 'apellido')

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.rol}'