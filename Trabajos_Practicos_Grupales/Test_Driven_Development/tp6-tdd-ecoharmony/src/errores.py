"""Excepciones de dominio: una por cada motivo de rechazo de la US."""


class InscripcionError(Exception):
    """Base de todos los rechazos de una inscripción."""


class ActividadInexistenteError(InscripcionError):
    """La actividad no pertenece al listado del parque."""


class HorarioNoDisponibleError(InscripcionError):
    """El parque está cerrado o la actividad no opera en ese horario."""


class CantidadPersonasInvalidaError(InscripcionError):
    """La cantidad es menor a 1 o no coincide con los visitantes cargados."""


class SinCupoError(InscripcionError):
    """No quedan cupos suficientes para el horario seleccionado."""


class DatosVisitanteIncompletosError(InscripcionError):
    """Falta nombre, DNI o edad de algún visitante."""


class TallaRequeridaError(InscripcionError):
    """La actividad exige talla de vestimenta y no se ingresó."""


class TerminosNoAceptadosError(InscripcionError):
    """No se aceptaron los términos y condiciones de la actividad."""
