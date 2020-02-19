from django.apps import AppConfig


class ServicesAppConfig(AppConfig):
    name = 'services'
    label = 'services'
    verbose_name = 'Services'

    def ready(self):
        import services.signals

default_app_config = 'services.ServicesAppConfig'
