"""Configuracoes gerais do projeto Django mercadinho."""

import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key

# Pasta raiz usada para localizar o banco e outros arquivos do projeto.
BASE_DIR = Path(__file__).resolve().parent.parent


# Usa a variavel de ambiente ou cria uma chave temporaria para uso local.
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY") or get_random_secret_key()

# O modo debug mostra erros detalhados durante o desenvolvimento.
DEBUG = True

ALLOWED_HOSTS = []


# Apps padrao do Django e o app com as regras do mercadinho.

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ecommerce",
]

# Componentes executados em toda requisicao, inclusive sessao e protecao CSRF.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Arquivo principal de rotas que inclui os enderecos do ecommerce.
ROOT_URLCONF = "mercadinho.urls"

# Procura os arquivos HTML dentro das pastas templates dos apps.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mercadinho.wsgi.application"


# Banco SQLite local; o arquivo e criado quando as migracoes sao aplicadas.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Regras padrao para senhas dos usuarios do Django.

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Idioma, horario e formatos de data exibidos pelo Django.

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Prefixo das URLs dos arquivos estaticos, como o CSS.

STATIC_URL = "static/"
