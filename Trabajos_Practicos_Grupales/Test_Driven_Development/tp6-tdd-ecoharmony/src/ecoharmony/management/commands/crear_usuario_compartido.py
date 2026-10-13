import os
import secrets

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError, transaction


EMAIL_COMPARTIDO = "ecoharmony.g3.pruebas@yopmail.com"


class Command(BaseCommand):
    help = "Crea la cuenta local compartida de EcoHarmony para pruebas."

    def handle(self, *args, **options):
        User = get_user_model()
        usuario = User.objects.filter(username=EMAIL_COMPARTIDO).first()
        if usuario is not None:
            self.stdout.write(
                self.style.WARNING(
                    f"La cuenta {EMAIL_COMPARTIDO} ya existe en esta base local."
                )
            )
            return

        if User.objects.filter(email__iexact=EMAIL_COMPARTIDO).exists():
            raise CommandError(
                f"El email {EMAIL_COMPARTIDO} ya está asociado a otra cuenta."
            )

        password = os.environ.get("ECOHARMONY_SHARED_USER_PASSWORD")
        password_generated = password is None
        if password_generated:
            password = secrets.token_urlsafe(24)
        elif len(password) < 12:
            raise CommandError(
                "ECOHARMONY_SHARED_USER_PASSWORD debe tener al menos "
                "12 caracteres."
            )

        try:
            with transaction.atomic():
                User.objects.create_user(
                    username=EMAIL_COMPARTIDO,
                    email=EMAIL_COMPARTIDO,
                    password=password,
                )
        except IntegrityError as error:
            raise CommandError(
                f"No se pudo crear la cuenta {EMAIL_COMPARTIDO}."
            ) from error

        self.stdout.write(
            self.style.SUCCESS(f"Cuenta creada: {EMAIL_COMPARTIDO}")
        )
        if password_generated:
            self.stdout.write(
                self.style.WARNING(
                    "Contraseña generada para desarrollo; guardala y "
                    "compartila con el grupo fuera del repositorio:"
                )
            )
            self.stdout.write(password)
        else:
            self.stdout.write(
                "Se usó ECOHARMONY_SHARED_USER_PASSWORD del entorno."
            )
