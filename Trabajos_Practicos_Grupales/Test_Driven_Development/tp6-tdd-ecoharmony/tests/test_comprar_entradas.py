"""Pruebas web de la US «Comprar entradas», escritas para la etapa RED."""

from datetime import date, datetime, time, timedelta
from io import StringIO
import pytest
from django.core.management import call_command
from django.test import Client
from ecoharmony.services import fecha_maxima_compra

from ecoharmony.models import Compra

pytestmark = pytest.mark.django_db


@pytest.fixture
def cliente():
    return Client()


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
    while fecha.weekday() == 0 or (fecha.month, fecha.day) in {
        (12, 25),
        (1, 1),
    }:
        fecha += timedelta(days=1)
    return fecha


def test_inicio_web_muestra_acceso_a_compra_de_entradas(cliente):
    respuesta = cliente.get("/")

    assert respuesta.status_code == 200
    assert b"Comprar entradas" in respuesta.content


def test_encabezado_muestra_logo_del_parque(cliente):
    respuesta = cliente.get("/")

    assert respuesta.status_code == 200
    assert b'class="logo-icono"' in respuesta.content
    assert b"Logo de EcoHarmony Park" in respuesta.content


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


def test_compra_en_efectivo_muestra_confirmacion_de_mail_simulado(cliente):
    registrar_y_autenticar(cliente)
    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(),
        follow=True,
    )

    fecha_mostrada = fecha_habil_futura().strftime("%d/%m/%Y")
    assert respuesta.status_code == 200
    assert b"Compra confirmada" in respuesta.content
    assert b"Entradas: 2" in respuesta.content
    assert fecha_mostrada.encode() in respuesta.content
    assert b"Mail enviado (simulado) a ana@example.com" in respuesta.content


def test_compra_calcula_total_segun_pase_de_cada_visitante(cliente):
    registrar_y_autenticar(cliente)
    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(),
        follow=True,
    )
    assert respuesta.status_code == 200
    assert b"Total: $20000" in respuesta.content


def test_compra_con_tarjeta_muestra_checkout_simulado(cliente):
    registrar_y_autenticar(cliente)
    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(medio_pago="tarjeta"),
    )
    assert respuesta.status_code == 302
    assert "/pago-tarjeta-simulado/" in respuesta.headers["Location"]
    respuesta = cliente.get(respuesta.headers["Location"])
    assert respuesta.status_code == 200
    assert b"Mercado Pago Compra Exitosa" in respuesta.content
    assert b"no se realiz\xc3\xb3 ning\xc3\xban cobro" in respuesta.content
    assert b"Mail enviado (simulado) a ana@example.com" in respuesta.content


def test_compra_sin_medio_de_pago_muestra_error_y_no_crea_compra(cliente):
    registrar_y_autenticar(cliente)
    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(medio_pago=""),
    )

    assert respuesta.status_code == 200
    assert b"Seleccion" in respuesta.content
    assert Compra.objects.count() == 0


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


def test_compra_rechaza_los_lunes(cliente):
    registrar_y_autenticar(cliente)
    dias_hasta_lunes = (0 - date.today().weekday()) % 7 or 7
    lunes = date.today() + timedelta(days=dias_hasta_lunes)
    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(fecha_visita=lunes.isoformat()),
    )

    assert respuesta.status_code == 200
    assert b"cerrado los lunes" in respuesta.content
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


def test_compra_rechaza_mas_de_diez_entradas_acumuladas_por_fecha(cliente):
    registrar_y_autenticar(cliente)
    fecha = fecha_habil_futura().isoformat()

    for cantidad in (6, 5):
        datos = {
            "fecha_visita": fecha,
            "cantidad_entradas": str(cantidad),
            "medio_pago": "efectivo",
        }
        for numero in range(1, cantidad + 1):
            datos[f"edad_{numero}"] = "25"
            datos[f"tipo_pase_{numero}"] = "regular"
        respuesta = cliente.post("/comprar-entradas/", datos)

    assert respuesta.status_code == 200
    assert b"hasta 10 entradas para una misma fecha" in respuesta.content
    assert Compra.objects.filter(fecha_visita=fecha).count() == 1
    assert Compra.objects.get(fecha_visita=fecha).cantidad_entradas == 6


def test_compra_aplica_descuentos_por_edad(cliente):
    registrar_y_autenticar(cliente)
    datos = {
        "fecha_visita": fecha_habil_futura().isoformat(),
        "cantidad_entradas": "3",
        "medio_pago": "efectivo",
        "edad_1": "3",
        "tipo_pase_1": "regular",
        "edad_2": "15",
        "tipo_pase_2": "regular",
        "edad_3": "60",
        "tipo_pase_3": "vip",
    }

    respuesta = cliente.post("/comprar-entradas/", datos, follow=True)

    assert respuesta.status_code == 200
    assert b"Total: $15000" in respuesta.content


@pytest.mark.parametrize(
    ("edad", "total"),
    (
        (0, 0),
        (3, 0),
        (4, 5000),
        (15, 5000),
        (16, 10000),
        (59, 10000),
        (60, 5000),
    ),
)
def test_compra_aplica_limites_de_descuento(cliente, edad, total):
    registrar_y_autenticar(cliente)
    datos = datos_compra(
        cantidad_entradas="1",
        edad_1=str(edad),
        tipo_pase_1="regular",
    )

    respuesta = cliente.post("/comprar-entradas/", datos, follow=True)

    assert respuesta.status_code == 200
    assert f"Total: ${total}".encode() in respuesta.content


def test_compra_rechaza_fecha_con_mas_de_un_mes_de_anticipacion(cliente):
    registrar_y_autenticar(cliente)
    fecha = date.today() + timedelta(days=60)
    while fecha.weekday() == 0 or (fecha.month, fecha.day) in {
        (12, 25),
        (1, 1),
    }:
        fecha += timedelta(days=1)
    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(fecha_visita=fecha.isoformat()),
    )

    assert respuesta.status_code == 200
    assert b"un mes de anticipaci\xc3\xb3n" in respuesta.content


def test_compra_mismo_dia_se_rechaza_despues_de_las_1730(
    cliente,
    monkeypatch,
):
    registrar_y_autenticar(cliente)
    hoy = date.today()
    if hoy.weekday() == 0 or (hoy.month, hoy.day) in {(12, 25), (1, 1)}:
        pytest.skip("La fecha actual es un día de cierre del parque.")
    monkeypatch.setattr(
        "ecoharmony.services.timezone.localtime",
        lambda value=None, timezone=None: datetime.combine(hoy, time(17, 31)),
    )
    monkeypatch.setattr(
        "ecoharmony.services.timezone.localdate",
        lambda: hoy,
    )

    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(fecha_visita=hoy.isoformat()),
    )

    assert respuesta.status_code == 200
    assert b"hasta las 17:30" in respuesta.content
    assert Compra.objects.count() == 0


def test_compra_mismo_dia_se_permite_hasta_las_1730(cliente, monkeypatch):
    registrar_y_autenticar(cliente)
    hoy = date.today()
    if hoy.weekday() == 0 or (hoy.month, hoy.day) in {(12, 25), (1, 1)}:
        pytest.skip("La fecha actual es un día de cierre del parque.")
    monkeypatch.setattr(
        "ecoharmony.services.timezone.localtime",
        lambda value=None, timezone=None: datetime.combine(hoy, time(17, 30)),
    )
    monkeypatch.setattr(
        "ecoharmony.services.timezone.localdate",
        lambda: hoy,
    )

    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(fecha_visita=hoy.isoformat()),
    )

    assert respuesta.status_code == 200
    assert b"Compra confirmada" in respuesta.content
    assert Compra.objects.count() == 1


@pytest.mark.parametrize(
    ("fecha", "hoy"),
    ((date(2026, 12, 25), date(2026, 12, 1)),
     (date(2027, 1, 1), date(2026, 12, 1))),
)
def test_compra_rechaza_fechas_festivas(cliente, monkeypatch, fecha, hoy):
    registrar_y_autenticar(cliente)
    monkeypatch.setattr(
        "ecoharmony.services.timezone.localtime",
        lambda value=None, timezone=None: datetime.combine(hoy, time(12)),
    )
    monkeypatch.setattr(
        "ecoharmony.services.timezone.localdate",
        lambda: hoy,
    )

    respuesta = cliente.post(
        "/comprar-entradas/",
        datos_compra(fecha_visita=fecha.isoformat()),
    )

    assert respuesta.status_code == 200
    assert b"cerrado los d\xc3\xadas festivos" in respuesta.content
    assert Compra.objects.count() == 0


def test_calendario_limita_fecha_maxima_y_muestra_reglas(cliente):
    registrar_y_autenticar(cliente)
    respuesta = cliente.get("/comprar-entradas/")

    assert respuesta.status_code == 200
    assert (
        f'max="{fecha_maxima_compra().isoformat()}"'.encode()
        in respuesta.content
    )
    assert b"25 de diciembre" in respuesta.content
    assert b"1 de enero" in respuesta.content


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
