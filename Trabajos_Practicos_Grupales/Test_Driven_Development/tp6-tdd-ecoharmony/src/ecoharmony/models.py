from django.conf import settings
from django.db import models


class Compra(models.Model):
    class MedioPago(models.TextChoices):
        EFECTIVO = "efectivo", "Efectivo en boletería"
        TARJETA = "tarjeta", "Tarjeta"

    class Estado(models.TextChoices):
        PENDIENTE_PAGO = "pendiente_pago", "Pendiente de pago"
        CONFIRMADA = "confirmada", "Confirmada"

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="compras_entradas",
    )
    fecha_visita = models.DateField()
    cantidad_entradas = models.PositiveSmallIntegerField()
    visitantes = models.JSONField()
    medio_pago = models.CharField(max_length=20, choices=MedioPago.choices)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.PENDIENTE_PAGO,
    )
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Compra {self.pk} - {self.cantidad_entradas} entradas"
