from django import template
from Services.models.service_category import ServiceCategory
from Services.models.main_service import MainService
from django.shortcuts import get_object_or_404
from Home.models import Contacts

register = template.Library()


@register.simple_tag()
def get_footer_data():
    return Contacts.objects.get(id=1)