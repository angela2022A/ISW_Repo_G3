"""Pruebas web de la US «Comprar entradas», escritas para la etapa RED."""

from datetime import date, timedelta
from io import StringIO
import pytest
from django.core import mail
from django.core.management import call_command
from django.test import Client, override_settings

from ecoharmony.models import Compra

pytestmark = pytest.mark.django_db


@pytest.fixture
def cliente():
    return Client()


@pytest.fixture(autouse=True)
def limpiar_emails():
    mail.get_connection()
    mail.outbox.clear()


def registrar_y_autenticar(cliente):
    respuesta = cliente.post(
        "/registro/",
        {
            "email": "ana@example.com",
            "password": "ClaveSegura123!",
            "confirmar_password": "ClaveSegura123!",
        },
    )
    assert respuesta.status_code == 302

    respuesta = cliente.post(
        "/iniciar-sesion/",
        {"username": "ana@example.com", "password": "ClaveSegura123!"},
    )
    assert respuesta.status_code == 302


def datos_compra(**cambios):
    datos = {
        "fecha_visita": fecha_habil_futura().isoformat(),
        "cantidad_entradas": "2",
        "edad_1": "25",
        "tipo_pase_1": "regular",
        "edad_2": "12",
        "tipo_pase_2": "vip",
        "medio_pago": "efectivo",
    }
    datos.update(cambios)
    return datos


def fecha_habil_futura():
    fecha = date.today() + timedelta(days=1)
    while fecha.weekday() >= 5:
        fecha += timedelta(days=1)
    return fecha


def test_inicio_web_muestra_acceso_a_compra_de_entradas(cliente):
    respuesta = cliente.get("/")

    assert respuesta.status_code == 200
    assert b"Comprar entradas" in respuesta.content


def test_visitante_sin_registro_no_puede_iniciar_una_compra(cliente):
    respuesta = cliente.get("/comprar-entradas/")

    assert respuesta.status_code == 302
    assert "/iniciar-sesion/" in respuesta.headers["Location"]


def test_cuenta_compartida_permite_iniciar_sesion_y_cerrar_sesion(
    cliente,
    monkeypatch,
):
    password = "ClaveCompartida2026!"
    monkeypatch.setenv("ECOHARMONY_SHARED_USER_PASSWORD", password)
    salida = StringIO()

    call_command("crear_usuario_compartido", stdout=salida)

    assert "ecoharmony.g3.pruebas@yopmail.com" in salida.getvalue()
    assert password not in salida.getvalue()
    respuesta = cliente.post(
        "/iniciar-sesion/",
        {
            "username": "ecoharmony.g3.pruebas@yopmail.com",
            "password": password,
        },
    )

    assert respuesta.status_code == 302
    assert cliente.get("/comprar-entradas/").wsgi_request.user.is_authenticated
    respuesta = cliente.post("/cerrar-sesion/")

    assert respuesta.status_code == 302
    assert not cliente.get("/comprar-entradas/").wsgi_request.user.is_authenticated


def test_formulario_separa_forma_de_pago_de_datos_de_visitantes(cliente):
    registrar_y_autenticar(cliente)
    respuesta = cliente.get("/comprar-entradas/")

    contenido = respuesta.content
    assert b'<fieldset class="payment-section">' in contenido
    assert b"<legend>Forma de pago</legend>" in contenido
    assert contenido.index(b'<fieldset class="payment-section">') > contenido.rindex(
        b"</section>"
    )


def test_compra_en_efectivo_confirma_sin_enviar_email_real(cliente):
    registrar_y_autenticar(cliente)
    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(),
        follow=True,
    )

    fecha_mostrada = fecha_habil_futura().strftime("%d/%m/%Y")
    assert respuesta.status_code == 200
    assert len(mail.outbox) == 1
    mensaje = mail.outbox[0]
    assert mensaje.to == ["ana@example.com"]
    assert "Entradas: 2" in mensaje.body
    assert fecha_mostrada in mensaje.body
    assert b"Compra confirmada" in respuesta.content
    assert b"Entradas: 2" in respuesta.content
    assert fecha_mostrada.encode() in respuesta.content
    assert "Te enviamos la confirmación a ana@example.com".encode() in (
        respuesta.content
    )





@override_settings(
    PRECIO_ENTRADA_REGULAR=1000,
    PRECIO_ENTRADA_VIP=2000,
)
def test_compra_calcula_total_segun_pase_de_cada_visitante(cliente):
    registrar_y_autenticar(cliente)
    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(),
        follow=True,
    )

    assert respuesta.status_code == 200
    assert b"Total: $3000" in respuesta.content


def test_compra_con_tarjeta_redirige_a_mercado_pago(cliente):
    registrar_y_autenticar(cliente)
    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(medio_pago="tarjeta"),
    )

    assert respuesta.status_code == 302
    assert respuesta.headers["Location"].startswith(
        "https://mercadopago.test/"
    )


def test_compra_sin_medio_de_pago_muestra_error_y_no_envia_email(cliente):
    registrar_y_autenticar(cliente)
    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(medio_pago=""),
    )

    assert respuesta.status_code == 200
    assert b"Seleccion" in respuesta.content
    assert len(mail.outbox) == 0


def test_compra_rechaza_fecha_anterior_a_hoy(cliente):
    registrar_y_autenticar(cliente)
    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(
            fecha_visita=(date.today() - timedelta(days=1)).isoformat()
        ),
    )

    assert respuesta.status_code == 200
    assert b"fecha" in respuesta.content.lower()


@pytest.mark.parametrize("dia_semana", (5, 6))
def test_compra_rechaza_fines_de_semana(cliente, dia_semana):
    registrar_y_autenticar(cliente)
    dias_hasta_fecha = (dia_semana - date.today().weekday()) % 7 or 7
    fecha_fin_semana = date.today() + timedelta(days=dias_hasta_fecha)
    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(fecha_visita=fecha_fin_semana.isoformat()),
    )

    assert respuesta.status_code == 200
    assert b"lunes a viernes" in respuesta.content
    assert Compra.objects.count() == 0


def test_compra_rechaza_mas_de_diez_entradas(cliente):
    registrar_y_autenticar(cliente)
    datos = {
        "fecha_visita": fecha_habil_futura().isoformat(),
        "cantidad_entradas": "11",
        "medio_pago": "efectivo",
    }
    for numero in range(1, 12):
        datos[f"edad_{numero}"] = "25"
        datos[f"tipo_pase_{numero}"] = "regular"

    respuesta = cliente.post(
        "/comprar-entradas/",
        datos,
    )

    assert respuesta.status_code == 200
    assert b"10" in respuesta.content


def test_compra_rechaza_edad_o_tipo_de_pase_faltante(cliente):
    registrar_y_autenticar(cliente)
    datos = datos_compra()
    datos.pop("edad_2")
    datos.pop("tipo_pase_2")

    respuesta = cliente.post(
        "/comprar-entradas/",
        datos,
    )

    assert respuesta.status_code == 200
    assert b"edad" in respuesta.content.lower()
    assert b"pase" in respuesta.content.lower()


@pytest.mark.parametrize(
    ("campo", "valor"),
    (("cantidad_entradas", "2a"), ("edad_1", "veinticinco")),
)
def test_compra_rechaza_letras_en_campos_numericos(cliente, campo, valor):
    registrar_y_autenticar(cliente)
    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(**{campo: valor}),
    )

    assert respuesta.status_code == 200
    assert Compra.objects.count() == 0
    assert b"debe" in respuesta.content.lower()


def test_formulario_muestra_fecha_dia_mes_anio_y_campos_solo_numericos(
    cliente,
):
    registrar_y_autenticar(cliente)
    respuesta = cliente.get("/comprar-entradas/")

    assert respuesta.status_code == 200
    assert b'<html lang="es-AR">' in respuesta.content
    assert b'name="fecha_visita" type="date"' in respuesta.content
    assert b"Formato d\xc3\xada/mes/a\xc3\xb1o." in respuesta.content
    assert b'inputmode="numeric"' in respuesta.content
    assert b'pattern="[0-9]+"' in respuesta.content
