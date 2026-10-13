from smtplib import SMTPException

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import OperationalError

from ecoharmony.models import Compra
from ecoharmony.services import enviar_confirmacion_compra


class Command(BaseCommand):
    help = "Reenvía por SMTP la confirmación de una compra en efectivo."

    def add_arguments(self, parser):
        parser.add_argument(
            "compra_id",
            nargs="?",
            type=int,
            help="ID de compra; si se omite, reenvía la última confirmada.",
        )

    def handle(self, *args, **options):
        if settings.EMAIL_BACKEND != "django.core.mail.backends.smtp.EmailBackend":
            raise CommandError(
                "SMTP no está configurado. No se envió el correo. "
                "Configurá Mailtrap Email Sending (no My Sandbox) y "
                "reiniciá Django."
            )

        compras = Compra.objects.filter(
            estado=Compra.Estado.CONFIRMADA,
            medio_pago=Compra.MedioPago.EFECTIVO,
        )
        compra_id = options["compra_id"]
        if compra_id is not None:
            compras = compras.filter(pk=compra_id)

        try:
            compra = compras.order_by("-creada_en").first()
        except OperationalError as error:
            raise CommandError(
                "No se pudo consultar la base de datos local."
            ) from error

        if compra is None:
            if compra_id is None:
                raise CommandError(
                    "No hay compras en efectivo confirmadas para reenviar."
                )
            raise CommandError(
                f"La compra {compra_id} no existe o no está confirmada "
                "en efectivo."
            )

        try:
            mensajes_enviados = enviar_confirmacion_compra(compra)
        except (OSError, SMTPException) as error:
            raise CommandError(
                "El servidor SMTP rechazó o no pudo aceptar el mensaje. "
                "Revisá las credenciales, el remitente verificado y los "
                "registros de Email Sending."
            ) from error

        if mensajes_enviados != 1:
            raise CommandError(
                "El servidor SMTP no confirmó la aceptación del mensaje."
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Confirmación de compra {compra.pk} enviada al servidor "
                f"SMTP para {settings.EMAIL_CONFIRMATION_RECIPIENT}. "
                "Revisá también los registros de entrega del proveedor."
            )
        )
