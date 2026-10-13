import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Compra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_visita", models.DateField()),
                ("cantidad_entradas", models.PositiveSmallIntegerField()),
                ("visitantes", models.JSONField()),
                (
                    "medio_pago",
                    models.CharField(
                        choices=[
                            ("efectivo", "Efectivo en boletería"),
                            ("tarjeta", "Tarjeta"),
                        ],
                        max_length=20,
                    ),
                ),
                ("total", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("pendiente_pago", "Pendiente de pago"),
                            ("confirmada", "Confirmada"),
                        ],
                        default="pendiente_pago",
                        max_length=20,
                    ),
                ),
                ("creada_en", models.DateTimeField(auto_now_add=True)),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="compras_entradas",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
