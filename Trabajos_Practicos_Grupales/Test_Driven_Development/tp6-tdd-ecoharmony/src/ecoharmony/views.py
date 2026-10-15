from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import IntegrityError, transaction
from django.db.models import Sum
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .models import Compra
from .services import (
    ErrorValidacionCompra,
    fecha_maxima_compra,
    validar_compra,
)


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
        "precio_regular": getattr(settings, "PRECIO_ENTRADA_REGULAR", "10000"),
        "precio_vip": getattr(settings, "PRECIO_ENTRADA_VIP", "20000"),
        "fecha_maxima": fecha_maxima_compra().isoformat(),
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


@require_POST
def cerrar_sesion(request):
    logout(request)
    return redirect("inicio")


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
        with transaction.atomic():
            get_user_model().objects.select_for_update().get(
                pk=request.user.pk
            )
            entradas_existentes = (
                Compra.objects.filter(
                    usuario=request.user,
                    fecha_visita=compra_validada.fecha_visita,
                ).aggregate(total=Sum("cantidad_entradas"))["total"]
                or 0
            )
            if entradas_existentes + len(compra_validada.visitantes) > 10:
                raise ErrorValidacionCompra(
                    [
                        "Solo podés comprar hasta 10 entradas para una "
                        "misma fecha."
                    ]
                )
            compra = Compra.objects.create(
                usuario=request.user,
                fecha_visita=compra_validada.fecha_visita,
                cantidad_entradas=len(compra_validada.visitantes),
                visitantes=compra_validada.visitantes,
                medio_pago=compra_validada.medio_pago,
                total=compra_validada.total,
                estado=Compra.Estado.CONFIRMADA,
            )
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

    if compra.medio_pago == Compra.MedioPago.TARJETA:
        return redirect("pago_tarjeta_simulado", compra_id=compra.pk)

    total_mostrado = f"{compra.total:.2f}".rstrip("0").rstrip(".")
    return render(
        request,
        "ecoharmony/compra_confirmada.html",
        {
            "compra": compra,
            "total_mostrado": total_mostrado,
        },
    )


@login_required
def pago_tarjeta_simulado(request, compra_id):
    compra = get_object_or_404(
        Compra,
        pk=compra_id,
        usuario=request.user,
        medio_pago=Compra.MedioPago.TARJETA,
    )
    total_mostrado = f"{compra.total:.2f}".rstrip("0").rstrip(".")
    return render(
        request,
        "ecoharmony/pago_tarjeta_simulado.html",
        {
            "compra": compra,
            "total_mostrado": total_mostrado,
        },
    )
