from django import forms
from .models import Session, Photo


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True
    template_name = "_file-uploader.html"


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class SessionForm(forms.ModelForm):
    photos = MultipleFileField()

    class Meta:
        model = Session
        fields = ['customer', 'valid_days', 'photos', 'status']


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['session', 'image']
