from django import template

register = template.Library()


@register.filter
def placeholder(input_field, value):
    input_field.field.widget.attrs['placeholder'] = value
    return input_field
