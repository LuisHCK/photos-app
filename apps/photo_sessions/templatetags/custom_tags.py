from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def sitename():
    return settings.SITE_NAME or 'My Site Name'


@register.filter
def get_status_class_name(status):
    if (status == 'active'):
        return 'is-success'
    elif (status == 'expired'):
        return 'is-warning'
    elif (status == 'deleted'):
        return 'is-danger'
    else:
        return 'is-primary'
