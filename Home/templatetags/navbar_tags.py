from django import template
from Services.models.service_category import ServiceCategory
from Services.models.main_service import MainService
from django.shortcuts import get_object_or_404

register = template.Library()

@register.simple_tag()
def get_sites():
    return MainService.objects.all()
    
@register.simple_tag()
def get_categories():
    return ServiceCategory.objects.all()
