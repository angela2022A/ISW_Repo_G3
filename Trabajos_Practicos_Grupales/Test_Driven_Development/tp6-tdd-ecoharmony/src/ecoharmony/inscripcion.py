"""US 'Inscribirme a actividad'.

COMO visitante QUIERO inscribirme a una actividad
PARA reservar mi lugar en la misma.
"""

from dataclasses import dataclass


@dataclass
class Inscripcion:
    actividad: str
    horario: str
    visitantes: list
    qr: str


class ServicioInscripcion:

    def __init__(self, parque, notificador, generador_qr):
        self.parque = parque
        self.notificador = notificador
        self.generador_qr = generador_qr

    def inscribir_actividad(self, actividad, horario, cantidad_personas,
                            visitantes, acepta_terminos):
        raise NotImplementedError('Pendiente: surge de los ciclos TDD')
