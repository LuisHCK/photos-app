from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Package, Tier


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'description', 'display_on_homepage']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class TierForm(forms.ModelForm):
    class Meta:
        model = Tier
        fields = ['name', 'description', 'price', 'features']
        widgets = {
            'features': forms.Textarea(attrs={'rows': 3, 'placeholder': _('Features separated by new lines')}),
            'description': forms.Textarea(attrs={'rows': 2}),
        }
