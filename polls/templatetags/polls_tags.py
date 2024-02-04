from django import template

from polls.models import Poll

register = template.Library()


@register.simple_tag()
def get_polls_list():
    return Poll.objects.all()
