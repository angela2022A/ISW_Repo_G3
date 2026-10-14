"""Configuración Django mínima para las pruebas web."""

SECRET_KEY = "test-only-secret-key"
DEBUG = True
USE_TZ = True
ALLOWED_HOSTS = ["testserver", "localhost"]
ROOT_URLCONF = "tests.urls"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "ecoharmony",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

LOGIN_URL = "/iniciar-sesion/"
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
DEFAULT_FROM_EMAIL = "entradas@ecoharmony.test"
PRECIO_ENTRADA_REGULAR = 1000
PRECIO_ENTRADA_VIP = 2000
MERCADO_PAGO_CHECKOUT_URL = "https://mercadopago.test/checkout"
