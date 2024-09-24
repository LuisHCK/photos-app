from django.contrib import admin
from .models import Session, Photo
from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget

admin.site.register(Session)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ImageField: {'widget': ImageUploaderWidget},
    }
