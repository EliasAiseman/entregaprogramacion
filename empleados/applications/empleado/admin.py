from django.contrib import admin
from .models import Empleado, Habilidades, Pais, Rol
from django.db import models
from django import forms
from datetime import date
from django_ckeditor_5.widgets import CKEditor5Widget
import csv
from django.http import HttpResponse
from reportlab.pdfgen import canvas

admin.site.register(Habilidades)
admin.site.register(Pais)


class RolAdmin(admin.ModelAdmin):
    list_filter = (
        'habilidadesRol',
    )


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'observaciones': CKEditor5Widget(config_name='default')
        }


def exportar_empleados_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="empleados.csv"'

    writer = csv.writer(response)
    writer.writerow(['\ufeffNombre', 'Apellido', 'Rol', 'Departamento', 'Fecha de Nacimiento'])


    for empleado in queryset:
        writer.writerow([
             empleado.nombre,
             empleado.apellido,
             empleado.rol.nombreRol if empleado.rol else '',
             empleado.departamento.nombre,
             empleado.fecha_nac
    ])


    return response


exportar_empleados_csv.short_description = "Exportar empleados seleccionados a CSV"


def exportar_empleados_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="empleados.pdf"'

    p = canvas.Canvas(response)
    y = 800
    p.setFont("Helvetica", 12)
    p.drawString(100, y, "Lista de Empleados")

    y -= 30
    for empleado in queryset:
        p.drawString(100, y, f'{empleado.nombreEmp} {empleado.apellidoEmp} - {empleado.rolEmp}')
        y -= 20
        if y < 50:
            p.showPage()
            y = 800

    p.showPage()
    p.save()
    return response


exportar_empleados_pdf.short_description = "Exportar empleados seleccionados a PDF"


class EmpleadoAdmin(admin.ModelAdmin):
    form = EmpleadoForm
    list_display = (
        'nombre',
        'apellido',
        'email',
        'fecha_nac',
        'calcularEdad',
        'pais',
        'trabajo',
        'departamento',
    )

    def calcularEdad(self, obj):
        today = date.today()
        age = today.year - obj.fecha_nac.year - ((today.month, today.day) < (obj.fecha_nac.month, obj.fecha_nac.day))
        return age

    calcularEdad.short_description = 'Edad'

    search_fields = (
        'apellido',
        'nombre',
    )

    list_filter = (
        'departamento',
        'trabajo',
        'pais',
        'habilidades',
    )

    filter_horizontal = (
        'habilidades',
    )

    actions = [exportar_empleados_csv, exportar_empleados_pdf]


admin.site.register(Rol, RolAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
