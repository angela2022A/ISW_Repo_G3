from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils import timezone


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


def validar_compra(datos, hoy=None):
    errores = []
    hoy = hoy or timezone.localdate()

    try:
        fecha_visita = date.fromisoformat(datos.get("fecha_visita", ""))
    except (TypeError, ValueError):
        fecha_visita = None
        errores.append("La fecha de visita no es válida.")

    if fecha_visita is not None and fecha_visita < hoy:
        errores.append("La fecha de visita no puede ser pasada.")

    try:
        cantidad = int(datos.get("cantidad_entradas", ""))
    except (TypeError, ValueError):
        cantidad = 0
        errores.append("La cantidad de entradas debe estar entre 1 y 10.")

    if cantidad < 1 or cantidad > 10:
        if "La cantidad de entradas debe estar entre 1 y 10." not in errores:
            errores.append("La cantidad de entradas debe estar entre 1 y 10.")

    visitantes = []
    if 1 <= cantidad <= 10:
        for numero in range(1, cantidad + 1):
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
                errores.append(
                    f"El tipo de pase del visitante {numero} no es válido."
                )

            visitantes.append({"edad": edad, "tipo_pase": pase})

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
