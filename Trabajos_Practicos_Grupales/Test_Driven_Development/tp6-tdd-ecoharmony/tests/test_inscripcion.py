"""Pruebas de la US 'Inscribirme a actividad'.

Cada test sigue el formato de la cátedra:
    # PASOS DEL CASO DE PRUEBA  -> Arrange (datos que ingresa el visitante)
    # Llamado a la US           -> Act
    # Resultado esperado        -> Assert

Los tests están en el ORDEN de los ciclos Red-Green-Refactor
(ver docs/03_bitacora_ciclos.md). U = prueba de usuario de la US,
D = caso derivado de los criterios de aceptación (ver docs/02).
"""

import pytest

from conftest import QR_FALSO
from ecoharmony.errores import (
    ActividadInexistenteError,
    CantidadPersonasInvalidaError,
    DatosVisitanteIncompletosError,
    HorarioNoDisponibleError,
    SinCupoError,
    TallaRequeridaError,
    TerminosNoAceptadosError,
)


def crear_visitante(**cambios):
    visitante = {
        'nombre': 'Ana Pérez',
        'dni': '40123456',
        'edad': 25,
        'talla': 'M',
    }
    visitante.update(cambios)
    return visitante


# --- Ciclo 1 - U1 (parte 1): inscripción válida -------------------------

def test_inscripcion_valida_devuelve_los_datos_de_la_inscripcion(servicio):
    # PASOS DEL CASO DE PRUEBA
    visitantes = [
        crear_visitante(),
        crear_visitante(nombre='Juan Gómez', dni='38999111', talla='L'),
    ]

    # Llamado a la US
    inscripcion = servicio.inscribir_actividad(
        actividad='Tirolesa', horario='10:00', cantidad_personas=2,
        visitantes=visitantes, acepta_terminos=True)

    # Resultado esperado: pasa
    assert inscripcion.actividad == 'Tirolesa'
    assert inscripcion.horario == '10:00'
    assert len(inscripcion.visitantes) == 2


# --- Ciclo 2 - D1: actividad fuera del listado ---------------------------

@pytest.mark.parametrize('actividad', ['Buceo', '', None])
def test_inscripcion_a_actividad_fuera_del_listado_falla(servicio,
                                                         actividad):
    with pytest.raises(ActividadInexistenteError):
        servicio.inscribir_actividad(
            actividad=actividad, horario='10:00', cantidad_personas=1,
            visitantes=[crear_visitante()], acepta_terminos=True)


# --- Ciclo 3 - U5: sin aceptar términos y condiciones --------------------

def test_inscripcion_sin_aceptar_terminos_falla(servicio):
    with pytest.raises(TerminosNoAceptadosError):
        servicio.inscribir_actividad(
            actividad='Tirolesa', horario='10:00', cantidad_personas=1,
            visitantes=[crear_visitante()], acepta_terminos=False)


# --- Ciclo 4 - D4: cantidad de personas = 0 ------------------------------

def test_inscripcion_con_cero_personas_falla(servicio):
    with pytest.raises(CantidadPersonasInvalidaError):
        servicio.inscribir_actividad(
            actividad='Safari', horario='09:00', cantidad_personas=0,
            visitantes=[], acepta_terminos=True)


# --- Ciclo 5 - D5: la cantidad no coincide con los visitantes cargados ---

def test_inscripcion_con_cantidad_distinta_a_visitantes_falla(servicio):
    with pytest.raises(CantidadPersonasInvalidaError):
        servicio.inscribir_actividad(
            actividad='Safari', horario='09:00', cantidad_personas=3,
            visitantes=[crear_visitante(), crear_visitante()],
            acepta_terminos=True)


# --- Ciclo 6 - D6: visitante con datos incompletos -----------------------

@pytest.mark.parametrize('dato_faltante', ['nombre', 'dni', 'edad'])
def test_inscripcion_con_visitante_incompleto_falla(servicio,
                                                    dato_faltante):
    visitante = crear_visitante(**{dato_faltante: None})

    with pytest.raises(DatosVisitanteIncompletosError):
        servicio.inscribir_actividad(
            actividad='Safari', horario='09:00', cantidad_personas=1,
            visitantes=[visitante], acepta_terminos=True)


# --- Ciclo 7 - U6: sin talla en actividad que la requiere ----------------

def test_inscripcion_sin_talla_requerida_por_la_actividad_falla(servicio):
    with pytest.raises(TallaRequeridaError):
        servicio.inscribir_actividad(
            actividad='Tirolesa', horario='10:00', cantidad_personas=1,
            visitantes=[crear_visitante(talla=None)],
            acepta_terminos=True)


# --- Ciclo 8 - U3: sin talla en actividad que no la requiere -------------

def test_inscripcion_sin_talla_en_actividad_que_no_la_requiere_pasa(
        servicio):
    inscripcion = servicio.inscribir_actividad(
        actividad='Safari', horario='09:00', cantidad_personas=1,
        visitantes=[crear_visitante(talla=None)], acepta_terminos=True)

    assert inscripcion.actividad == 'Safari'


# --- Ciclo 9 - U4: parque cerrado o actividad no disponible --------------

@pytest.mark.parametrize('horario', [
    '20:00',   # parque cerrado
    '12:00',   # parque abierto, pero la Tirolesa no opera a esa hora
])
def test_inscripcion_en_horario_no_disponible_falla(servicio, horario):
    with pytest.raises(HorarioNoDisponibleError):
        servicio.inscribir_actividad(
            actividad='Tirolesa', horario=horario, cantidad_personas=1,
            visitantes=[crear_visitante()], acepta_terminos=True)


# --- Ciclo 10 - U2: actividad sin cupo en el horario ---------------------

def test_inscripcion_a_horario_sin_cupo_falla(servicio):
    with pytest.raises(SinCupoError):
        servicio.inscribir_actividad(
            actividad='Tirolesa', horario='14:00', cantidad_personas=1,
            visitantes=[crear_visitante()], acepta_terminos=True)


# --- Ciclo 11 - D2 / D3: valores límite del cupo (cupo restante = 3) -----

def test_inscripcion_que_ocupa_exactamente_el_cupo_restante_pasa(servicio):
    visitantes = [crear_visitante(dni=str(n)) for n in range(3)]

    inscripcion = servicio.inscribir_actividad(
        actividad='Palestra', horario='15:00', cantidad_personas=3,
        visitantes=visitantes, acepta_terminos=True)

    assert len(inscripcion.visitantes) == 3


def test_inscripcion_que_supera_en_uno_el_cupo_restante_falla(servicio):
    visitantes = [crear_visitante(dni=str(n)) for n in range(4)]

    with pytest.raises(SinCupoError):
        servicio.inscribir_actividad(
            actividad='Palestra', horario='15:00', cantidad_personas=4,
            visitantes=visitantes, acepta_terminos=True)


# --- Ciclo 12 - D7: la inscripción descuenta cupos -----------------------

def test_inscripcion_exitosa_descuenta_los_cupos(servicio, parque):
    servicio.inscribir_actividad(
        actividad='Tirolesa', horario='10:00', cantidad_personas=2,
        visitantes=[crear_visitante(), crear_visitante(dni='38999111')],
        acepta_terminos=True)

    assert parque.cupo_restante('Tirolesa', '10:00') == 8


# --- Ciclo 13 - U1 (parte 2): email de confirmación con QR ---------------

def test_inscripcion_exitosa_envia_email_con_qr(servicio, notificador):
    inscripcion = servicio.inscribir_actividad(
        actividad='Tirolesa', horario='10:00', cantidad_personas=1,
        visitantes=[crear_visitante()], acepta_terminos=True)

    assert inscripcion.qr == QR_FALSO
    notificador.enviar.assert_called_once_with(inscripcion)


# --- Ciclo 14 - D8: si la inscripción falla, no se envía email -----------

def test_inscripcion_rechazada_no_envia_email(servicio, notificador):
    with pytest.raises(TerminosNoAceptadosError):
        servicio.inscribir_actividad(
            actividad='Tirolesa', horario='10:00', cantidad_personas=1,
            visitantes=[crear_visitante()], acepta_terminos=False)

    notificador.enviar.assert_not_called()
