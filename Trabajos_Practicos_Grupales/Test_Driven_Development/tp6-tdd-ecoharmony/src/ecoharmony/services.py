from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import send_mail
from django.utils import timezone

from .models import Compra


class ErrorValidacionCompra(ValueError):
    def __init__(self, errores):
        self.errores = errores
        super().__init__("; ".join(errores))


@dataclass(frozen=True)
class CompraValidada:
    fecha_visita: date
    visitantes: list[dict[str, int | str]]
    medio_pago: str
    total: Decimal


def enviar_confirmacion_compra(compra):
    return send_mail(
        subject="Confirmación de compra - EcoHarmony Park",
        message=(
            f"Compra confirmada. Entradas: {compra.cantidad_entradas}. "
            f"Fecha de visita: {compra.fecha_visita.isoformat()}. "
            f"Total: ${compra.total}."
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.EMAIL_CONFIRMATION_RECIPIENT],
        fail_silently=False,
    )


def _precio_configurado(nombre):
    valor = getattr(settings, nombre, None)
    if valor is None:
        raise ImproperlyConfigured(f"Falta configurar {nombre}.")
    try:
        precio = Decimal(str(valor))
    except (InvalidOperation, ValueError) as error:
        raise ImproperlyConfigured(
            f"El valor de {nombre} no es un importe válido."
        ) from error
    if not precio.is_finite() or precio < 0:
        raise ImproperlyConfigured(
            f"El valor de {nombre} debe ser un importe no negativo."
        )
    return precio


def _validar_fecha_visita(datos, hoy, errores):
    try:
        fecha_visita = date.fromisoformat(datos.get("fecha_visita", ""))
    except (TypeError, ValueError):
        fecha_visita = None
        errores.append("La fecha de visita no es válida.")

    if fecha_visita is not None and fecha_visita < hoy:
        errores.append("La fecha de visita no puede ser pasada.")
    elif fecha_visita is not None and fecha_visita.weekday() >= 5:
        errores.append("El parque abre de lunes a viernes.")

    return fecha_visita


def _validar_cantidad_entradas(datos, errores):
    try:
        cantidad = int(datos.get("cantidad_entradas", ""))
    except (TypeError, ValueError):
        errores.append("La cantidad de entradas debe estar entre 1 y 10.")
        return 0

    if cantidad < 1 or cantidad > 10:
        errores.append("La cantidad de entradas debe estar entre 1 y 10.")

    return cantidad


def _validar_visitante(datos, numero, errores):
    edad_texto = datos.get(f"edad_{numero}", "")
    pase = datos.get(f"tipo_pase_{numero}", "")

    try:
        edad = int(edad_texto)
        if edad < 0:
            raise ValueError
    except (TypeError, ValueError):
        errores.append(
            f"La edad del visitante {numero} debe ser un entero "
            "no negativo."
        )
        edad = None

    if pase not in ("regular", "vip"):
        errores.append(f"El tipo de pase del visitante {numero} no es válido.")

    return {"edad": edad, "tipo_pase": pase}


def validar_compra(datos, hoy=None):
    errores = []
    hoy = hoy or timezone.localdate()

    fecha_visita = _validar_fecha_visita(datos, hoy, errores)
    cantidad = _validar_cantidad_entradas(datos, errores)

    visitantes = []
    if 1 <= cantidad <= 10:
        for numero in range(1, cantidad + 1):
            visitantes.append(_validar_visitante(datos, numero, errores))

    medio_pago = datos.get("medio_pago", "")
    if medio_pago not in ("efectivo", "tarjeta"):
        errores.append("Seleccioná una forma de pago válida.")

    if errores:
        raise ErrorValidacionCompra(errores)

    precios = {
        "regular": _precio_configurado("PRECIO_ENTRADA_REGULAR"),
        "vip": _precio_configurado("PRECIO_ENTRADA_VIP"),
    }
    total = sum(
        (precios[visitante["tipo_pase"]] for visitante in visitantes),
        start=Decimal("0"),
    )

    return CompraValidada(
        fecha_visita=fecha_visita,
        visitantes=visitantes,
        medio_pago=medio_pago,
        total=total,
    )
