import datetime
from django import template
from project import settings

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag()
def my_stripe_key():
    return settings.STRIPE_PUBLISHABLE


