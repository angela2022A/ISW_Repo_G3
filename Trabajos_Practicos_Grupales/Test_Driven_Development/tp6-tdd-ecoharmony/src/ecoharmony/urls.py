from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("registro/", views.registro, name="registro"),
    path("iniciar-sesion/", views.iniciar_sesion, name="iniciar_sesion"),
    path("cerrar-sesion/", views.cerrar_sesion, name="cerrar_sesion"),
    path("comprar-entradas/", views.comprar_entradas, name="comprar_entradas"),
    path(
        "pago-tarjeta-simulado/<int:compra_id>/",
        views.pago_tarjeta_simulado,
        name="pago_tarjeta_simulado",
    ),
]
