from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.db.models import indexes
from django.dispatch import receiver
from django.core.files import File
from PIL import Image
from io import BytesIO
from apps.customers.models import Customer
from datetime import datetime, timedelta
from django.utils.translation import gettext_lazy as _
import os
from utils.text import kebab


# Allow compressing large images
Image.MAX_IMAGE_PIXELS = 1000000000

PHOTOSHOOT_STATUS = (
    ('active', _('Active')),
    ('expired', _('Expired')),
    ('deleted', _('Deleted')),
)


class Session(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT,
                                 verbose_name=_('Customer'))
    user = models.ForeignKey(User, verbose_name=_("User"),
                             on_delete=models.CASCADE)

    access_slug = models.CharField(max_length=255, null=True, blank=True,
                                   unique=True, verbose_name=_("Access slug"))
    valid_days = models.IntegerField(default=15, verbose_name=_("Valid days"))
    download_count = models.IntegerField(default=0,
                                         verbose_name=_('Download count'))
    status = models.CharField(max_length=32,
                              choices=PHOTOSHOOT_STATUS,
                              default='active', verbose_name=_("Status"))

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        verbose_name = _("Session")
        verbose_name_plural = _("Sessions")
        indexes = [
            models.Index(fields=['access_slug'], name='access_slug_index'),
        ]

    def __str__(self):
        return "Session for customer %s" % self.customer_id

    def expires_at(self):
        return self.created_at + timedelta(days=self.valid_days)

    def count_photos(self):
        return self.photo_set.count()


class Photo(models.Model):
    session = models.ForeignKey(
        Session, on_delete=models.CASCADE, verbose_name=_("Session"))
    image = models.ImageField(
        upload_to='hires', null=True, blank=True, verbose_name=_("Image"))
    thumbnail = models.ImageField(
        upload_to='thumbs', null=True, blank=True, verbose_name=_("Thumbnail"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")

    def __str__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        if self.image:
            self.thumbnail = compress(self.image)
        super(Photo, self).save(*args, **kwargs)

    def clean_photos(self):
        """
        Deletes file from filesystem to free up space
        """
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)

        if self.thumbnail:
            if os.path.isfile(self.thumbnail.path):
                os.remove(self.thumbnail.path)


def compress(image: File) -> File:
    """
    Compress and optimize image
    """
    temp_img = Image.open(image)
    temp_io = BytesIO()
    max_width = 10000
    max_height = 850

    ratio = min(
        max_width / float(temp_img.size[0]), max_height / float(temp_img.size[1]))

    target_size = (int(temp_img.size[0] * ratio),
                   int(temp_img.size[1] * ratio))

    # Reescale image preserving aspect ratio
    # Convert to RGB then resize image and save
    temp_img = temp_img\
        .convert('RGB')\
        .resize(target_size, Image.LANCZOS)\
        .save(temp_io, 'JPEG', quality=80, optimize=True)

    new_image = File(temp_io, name=image.name)
    return new_image


@receiver(models.signals.post_delete, sender=Photo)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Photo` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

    if instance.thumbnail:
        if os.path.isfile(instance.thumbnail.path):
            os.remove(instance.thumbnail.path)


@receiver(models.signals.post_save, sender=Session)
def create_access_slug(sender, instance, created, **kwargs):
    if created:
        instance.access_slug = kebab("{} {} {}".format(
            instance.id,
            instance.customer.name,
            instance.created_at.strftime("%Y-%m-%d")))
        instance.save()
