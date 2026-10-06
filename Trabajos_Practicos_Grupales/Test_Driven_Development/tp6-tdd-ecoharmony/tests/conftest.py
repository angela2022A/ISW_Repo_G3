"""Fixtures compartidas: datos de prueba y dobles de prueba.

Los horarios y cupos son SUPUESTOS del grupo (ver docs/01_concepto.md).
El parque abre de 09:00 a 18:00: ninguna actividad tiene horarios fuera
de esa franja.
"""

import copy
from unittest.mock import Mock

import pytest

from ecoharmony.inscripcion import ServicioInscripcion
from ecoharmony.parque import Parque

ACTIVIDADES = {
    'Tirolesa': {
        'requiere_talla': True,
        'horarios': {'10:00': 10, '14:00': 0},   # 14:00 agotado (U2)
    },
    'Palestra': {
        'requiere_talla': True,
        'horarios': {'11:00': 8, '15:00': 3},    # 15:00 límite (D2/D3)
    },
    'Safari': {
        'requiere_talla': False,
        'horarios': {'09:00': 20, '13:00': 20},
    },
    'Jardinería': {
        'requiere_talla': False,
        'horarios': {'10:00': 12, '16:00': 12},
    },
}

QR_FALSO = 'QR-FAKE-123'


@pytest.fixture
def parque():
    # Copia profunda: cada test arranca con los cupos originales
    # (patrón Isolated Test).
    return Parque(copy.deepcopy(ACTIVIDADES))


@pytest.fixture
def notificador():
    # Mock: verifica si se envió el email y con qué datos.
    return Mock()


@pytest.fixture
def generador_qr():
    # Stub: devuelve siempre el mismo QR, sin generar uno real.
    stub = Mock()
    stub.generar.return_value = QR_FALSO
    return stub


@pytest.fixture
def servicio(parque, notificador, generador_qr):
    return ServicioInscripcion(parque, notificador, generador_qr)
