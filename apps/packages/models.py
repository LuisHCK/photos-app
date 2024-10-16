from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _
from utils.images import compress
import os

class Package(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(
        upload_to='package_thumbnails', verbose_name=_('Image'))

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('Updated at'))
    published = models.BooleanField(default=False, verbose_name=_('Published'))
    display_on_homepage = models.BooleanField(
        default=False, verbose_name=_('Display on homepage'))
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('Created by'))

    def __str__(self):
        return self.name

    def tiers(self):
        return Tier.objects.filter(package=self)

    def photo_examples(self):
        return PhotoExample.objects.filter(package=self)


class Tier(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    features = ArrayField(models.CharField(max_length=255), blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PhotoExample(models.Model):
    file = models.ImageField(
        upload_to='photo_examples', verbose_name=_("File"))
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """
        Compress image on creation
        """
        if not self.pk and self.file:
            self.file = compress(self.file, max_height=300)

        super(PhotoExample, self).save(*args, **kwargs)

@receiver(models.signals.post_delete, sender=PhotoExample)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Photo` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
