from django.db import models
from django.utils.translation import gettext_lazy as _

class Customer(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Phone"))
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Email"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name