"""Pruebas web de la US «Comprar entradas», escritas para la etapa RED."""

from datetime import date, timedelta

import pytest
from django.core import mail
from django.test import Client, override_settings

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
        "fecha_visita": (date.today() + timedelta(days=1)).isoformat(),
        "cantidad_entradas": "2",
        "edad_1": "25",
        "tipo_pase_1": "regular",
        "edad_2": "12",
        "tipo_pase_2": "vip",
        "medio_pago": "efectivo",
    }
    datos.update(cambios)
    return datos


def test_inicio_web_muestra_acceso_a_compra_de_entradas(cliente):
    respuesta = cliente.get("/")

    assert respuesta.status_code == 200
    assert b"Comprar entradas" in respuesta.content


def test_visitante_sin_registro_no_puede_iniciar_una_compra(cliente):
    respuesta = cliente.get("/comprar-entradas/")

    assert respuesta.status_code == 302
    assert "/iniciar-sesion/" in respuesta.headers["Location"]


def test_compra_en_efectivo_confirma_fecha_cantidad_y_envia_email(cliente):
    registrar_y_autenticar(cliente)
    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(),
        follow=True,
    )

    assert respuesta.status_code == 200
    assert b"Compra confirmada" in respuesta.content
    assert b"Entradas: 2" in respuesta.content
    assert datos_compra()["fecha_visita"].encode() in respuesta.content
    assert len(mail.outbox) == 1
    assert mail.outbox[0].to == ["ana@example.com"]
    assert "2" in mail.outbox[0].body


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


def test_compra_rechaza_mas_de_diez_entradas(cliente):
    registrar_y_autenticar(cliente)
    datos = {
        "fecha_visita": (date.today() + timedelta(days=1)).isoformat(),
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
