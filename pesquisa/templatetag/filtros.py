#modulo responsável pela criação de templates
from atexit import register
from django import template

register = template.Library()

@register.filter
def diferenca_data(valor1, valor2):
    return (valor1 - valor2).days