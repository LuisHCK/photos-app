from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _


class Package(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='package_thumbnails', verbose_name=_('Image'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    published = models.BooleanField(default=False, verbose_name=_('Published'))
    display_on_homepage = models.BooleanField(default=False, verbose_name=_('Display on homepage'))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Created by'))

    def __str__(self):
        return self.name


class Tier(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    features = ArrayField(models.CharField(max_length=255), blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
