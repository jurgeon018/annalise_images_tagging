from django import apps


class ImagesConfig(apps.AppConfig):
    name = 'images'
    verbose_name = 'Annalise Images'
    verbose_name_plural = verbose_name

    def ready(self):
        from images import signals  # NOQA


default_app_config = 'images.ImagesConfig'
