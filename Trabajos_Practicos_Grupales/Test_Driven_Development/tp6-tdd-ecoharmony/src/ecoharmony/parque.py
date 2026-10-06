"""Catálogo de actividades del parque con sus horarios y cupos."""


class Parque:

    def __init__(self, actividades):
        # actividades: {nombre: {'requiere_talla': bool,
        #                        'horarios': {'HH:MM': cupo}}}
        self.actividades = actividades

    def cupo_restante(self, actividad, horario):
        raise NotImplementedError('Pendiente: surge de los ciclos TDD')
