from django import template
from obuchenie.models import *

register = template.Library()

@register.simple_tag()
def get_group():
    return NG_course.objects.all()

@register.inclusion_tag('obuchenie/list_group.html')
def show_group(sort=None, group_select=0):
    if not sort:
        groups = NG_course.objects.all()
    else:
        groups = NG_course.objects.order_by(sort)
    return {"groups": groups, "group_select": group_select}