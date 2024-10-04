from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Package


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'description', 'display_on_homepage']
