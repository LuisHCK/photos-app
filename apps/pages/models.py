from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Asset(models.Model):
    file = models.ImageField(upload_to='assets', verbose_name=_("File"))
    caption = models.CharField(max_length=255, verbose_name=_("Caption"))

    class Meta:
        verbose_name = _("Asset")
        verbose_name_plural = _("Assets")

    def __str__(self):
        return self.caption


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            verbose_name=_("Name"))

    def __str__(self):
        return self.name


class Page(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    slug = models.SlugField(max_length=255, unique=True,
                            verbose_name=_('Slug'))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_('Tags'))
    description = models.TextField(verbose_name=_('Description'))
    cover = models.ForeignKey(
        Asset, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Cover'))
    is_published = models.BooleanField(
        default=True, verbose_name=_('Published'))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created at'))
    data = models.JSONField(blank=True, null=True, verbose_name=_('Data'))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('Updated at'))
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   null=True, blank=True, verbose_name=_('Created by'))

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")

        indexes = [
            models.Index(fields=['slug'], name='slug_index'),
        ]

    def __str__(self):
        return self.title
