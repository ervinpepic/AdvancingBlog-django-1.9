from urllib import quote_plus #python 2


from django import template

register = template.Library()
@register.filter
def urlify(value):
    return quote_plus(value)