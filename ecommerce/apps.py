from django.apps import AppConfig


class EcommerceConfig(AppConfig):
    """Identifica o app ecommerce para o Django."""

    # Tipo de ID automatico para models sem chave primaria declarada.
    default_auto_field = "django.db.models.BigAutoField"
    name = "ecommerce"
