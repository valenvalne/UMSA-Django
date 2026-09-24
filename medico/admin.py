from django.contrib import admin
from .models import Turno


@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = (
        'id_turno',
        'nombre',
        'dni',
        'telefono',
        'especialidad',
        'profesional',
        'fecha',
        'hora',
        'registro',
    )
    search_fields = ('id_turno', 'nombre', 'dni', 'profesional')
    list_filter = ('especialidad', 'profesional', 'fecha')
    readonly_fields = ('registro',)
