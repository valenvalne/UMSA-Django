from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Turno
from datetime import datetime
import uuid


def inicio(request):
    return render(request, 'medico/index.html')


def crear_turno(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        dni = request.POST.get('dni', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        especialidad = request.POST.get('especialidad', '').strip()
        profesional = request.POST.get('profesional', '').strip()
        fecha = request.POST.get('fecha', '').strip()
        hora = request.POST.get('hora', '').strip()

        turno = Turno.objects.create(
            id_turno=f"UMSA-{uuid.uuid4().hex[:8].upper()}",
            nombre=nombre,
            dni=dni,
            telefono=telefono,
            especialidad=especialidad,
            profesional=profesional,
            fecha=datetime.strptime(fecha, '%Y-%m-%d').date(),
            hora=datetime.strptime(hora, '%H:%M').time(),
        )

        return JsonResponse({
            'ok': True,
            'id_turno': turno.id_turno,
        })

    return JsonResponse({
        'ok': False,
        'error': 'Método no permitido.'
    }, status=405)