from django.db import models
from django.utils.translation import gettext_lazy as _


class AppSettings(models.Model):
    key = models.CharField(max_length=255, unique=True, verbose_name=_("Key"))
    value = models.CharField(max_length=255, verbose_name=_("Value"))
    description = models.CharField(
        max_length=255, verbose_name=_("Description"))
    config_type = models.CharField(
        max_length=255, verbose_name=_("Config type"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = _("App settings")
        indexes = [
            models.Index(fields=['key'], name='key_index'),
        ]

    def __str__(self):
        return self.key
