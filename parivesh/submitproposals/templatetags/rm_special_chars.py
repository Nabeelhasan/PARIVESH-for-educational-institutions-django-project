from django import template

register = template.Library()

@register.filter(name='remove_special_characters')
def remove_chars(value, arg):
    for character in arg:
        value = value.replace(character, "")
    return value