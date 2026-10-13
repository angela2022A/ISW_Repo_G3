"""URLs web incluidas en la configuración de pruebas."""

from django.urls import include, path

urlpatterns = [
    path("", include("ecoharmony.urls")),
]
