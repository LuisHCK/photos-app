from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def sitename():
    return settings.SITE_NAME or 'My Site Name'


@register.simple_tag
def sitedescription():
    return 'My Site Description'


@register.simple_tag
def sitekeywords():
    return 'My Site Keywords'


@register.simple_tag
def siteauthor():
    return 'My Site Author'


@register.simple_tag
def sitephone():
    return settings.SITE_PHONE


@register.simple_tag
def sitephoneurlsafe():
    return settings.SITE_PHONE.replace('+', '').replace('(', '').replace(')', '').replace(' ', '')


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
