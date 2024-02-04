from django import template

from config.constants import SITE_SECTIONS

register = template.Library()


@register.simple_tag()
def get_site_sections():
    return SITE_SECTIONS
