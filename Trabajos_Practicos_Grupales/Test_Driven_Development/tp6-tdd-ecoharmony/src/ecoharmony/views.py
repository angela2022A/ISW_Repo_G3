from urllib.parse import urlencode

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ImproperlyConfigured
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.mail import send_mail
from django.db import IntegrityError, transaction
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme

from .models import Compra
from .services import ErrorValidacionCompra, validar_compra


def _contexto_formulario_compra(datos=None):
    datos = datos or {}
    visitantes = [
        {
            "numero": numero,
            "edad": datos.get(f"edad_{numero}", ""),
            "tipo_pase": datos.get(f"tipo_pase_{numero}", "regular"),
        }
        for numero in range(1, 11)
    ]
    return {
        "visitantes_formulario": visitantes,
        "precio_regular": getattr(settings, "PRECIO_ENTRADA_REGULAR", "1000"),
        "precio_vip": getattr(settings, "PRECIO_ENTRADA_VIP", "2000"),
        "medio_pago": datos.get("medio_pago", ""),
    }


def inicio(request):
    return render(request, "ecoharmony/inicio.html")


def registro(request):
    if request.user.is_authenticated:
        return redirect("comprar_entradas")

    errores = []
    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")
        confirmar_password = request.POST.get("confirmar_password", "")

        try:
            validate_email(email)
        except ValidationError:
            errores.append("Ingresá un email válido.")
        if len(password) < 8:
            errores.append("La contraseña debe tener al menos 8 caracteres.")
        if password != confirmar_password:
            errores.append("Las contraseñas no coinciden.")

        User = get_user_model()
        if email and User.objects.filter(email__iexact=email).exists():
            errores.append("Ya existe una cuenta registrada con ese email.")

        if not errores:
            try:
                with transaction.atomic():
                    User.objects.create_user(
                        username=email,
                        email=email,
                        password=password,
                    )
            except IntegrityError:
                errores.append("No se pudo crear la cuenta con ese email.")
            else:
                messages.success(
                    request,
                    "Cuenta creada. Iniciá sesión para comprar tus entradas.",
                )
                return redirect("iniciar_sesion")

    return render(
        request,
        "ecoharmony/registro.html",
        {"errores": errores},
        status=200,
    )


def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect("comprar_entradas")

    error = ""
    if request.method == "POST":
        email = request.POST.get("username", "").strip().lower()
        password = request.POST.get("password", "")
        usuario = authenticate(request, username=email, password=password)
        if usuario is not None:
            login(request, usuario)
            destino = request.GET.get("next", "")
            if destino and url_has_allowed_host_and_scheme(
                destino,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
            ):
                return redirect(destino)
            return redirect("comprar_entradas")
        error = "Email o contraseña incorrectos."

    return render(
        request,
        "ecoharmony/iniciar_sesion.html",
        {"error": error},
        status=200,
    )


@login_required
def comprar_entradas(request):
    if request.method == "GET":
        contexto = _contexto_formulario_compra()
        contexto["cantidad_inicial"] = 1
        return render(
            request,
            "ecoharmony/comprar_entradas.html",
            contexto,
        )

    if request.method != "POST":
        return HttpResponseBadRequest("Método no permitido.")

    try:
        compra_validada = validar_compra(request.POST)
    except ErrorValidacionCompra as error:
        for mensaje in error.errores:
            messages.error(request, mensaje)
        contexto = _contexto_formulario_compra(request.POST)
        contexto.update(
            {
                "cantidad_inicial": request.POST.get(
                    "cantidad_entradas", "1"
                ),
                "datos": request.POST,
            }
        )
        return render(
            request,
            "ecoharmony/comprar_entradas.html",
            contexto,
            status=200,
        )

    estado = (
        Compra.Estado.CONFIRMADA
        if compra_validada.medio_pago == Compra.MedioPago.EFECTIVO
        else Compra.Estado.PENDIENTE_PAGO
    )
    base_url = ""
    if compra_validada.medio_pago == Compra.MedioPago.TARJETA:
        base_url = getattr(settings, "MERCADO_PAGO_CHECKOUT_URL", "")
        if not base_url:
            raise ImproperlyConfigured(
                "Falta configurar MERCADO_PAGO_CHECKOUT_URL."
            )

    compra = Compra.objects.create(
        usuario=request.user,
        fecha_visita=compra_validada.fecha_visita,
        cantidad_entradas=len(compra_validada.visitantes),
        visitantes=compra_validada.visitantes,
        medio_pago=compra_validada.medio_pago,
        total=compra_validada.total,
        estado=estado,
    )

    if compra.medio_pago == Compra.MedioPago.TARJETA:
        separador = "&" if "?" in base_url else "?"
        return redirect(
            f"{base_url}{separador}"
            f"{urlencode({'external_reference': compra.pk})}"
        )

    send_mail(
        subject="Confirmación de compra - EcoHarmony Park",
        message=(
            f"Compra confirmada. Entradas: {compra.cantidad_entradas}. "
            f"Fecha de visita: {compra.fecha_visita.isoformat()}. "
            f"Total: ${compra.total}."
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[request.user.email],
    )
    total_mostrado = f"{compra.total:.2f}".rstrip("0").rstrip(".")
    return render(
        request,
        "ecoharmony/compra_confirmada.html",
        {
            "compra": compra,
            "total_mostrado": total_mostrado,
        },
    )
