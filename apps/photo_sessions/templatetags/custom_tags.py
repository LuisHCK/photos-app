from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def sitename():
    return settings.SITE_NAME or 'My Site Name'
