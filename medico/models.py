from django.db import models


class Turno(models.Model):
    registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha y Hora de Registro"
    )
    id_turno = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="ID Turno"
    )
    nombre = models.CharField(
        max_length=150,
        verbose_name="Nombre y Apellido"
    )
    dni = models.CharField(
        max_length=20,
        verbose_name="DNI"
    )
    telefono = models.CharField(
        max_length=50,
        verbose_name="Telefono"
    )
    especialidad = models.CharField(
        max_length=100,
        verbose_name="Especialidad"
    )
    profesional = models.CharField(
        max_length=100,
        verbose_name="Profesional"
    )
    fecha = models.DateField(
        verbose_name="Fecha del Turno"
    )
    hora = models.TimeField(
        verbose_name="Hora del Turno"
    )

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"
        ordering = ["-registro"]

    def __str__(self):
        return f"{self.id_turno} - {self.nombre} ({self.fecha} {self.hora})"
