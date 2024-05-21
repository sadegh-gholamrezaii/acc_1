from django.apps import AppConfig


app_name = 'customer'
class CustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer'
    verbose_name = 'مشتری'
