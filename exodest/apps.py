from django.apps import AppConfig


class ExodestConfig(AppConfig):
    name = "exodest"

    def ready(self):
        from exodest import modules
