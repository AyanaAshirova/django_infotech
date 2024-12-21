from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from typing import Any

from django.views.generic import CreateView, ListView, View, TemplateView, DetailView
from Services.models import *
from App1C.models.company_type import CompanyType
from App1C.views import CompanyTaskIndustry
from App1C.utils import SERVICE_1C_ID
from .models import *


class Index(CompanyTaskIndustry, TemplateView):
    template_name = 'Home/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['categories'] = ServiceCategory.objects.filter(main_service__id=SERVICE_1C_ID)
        # context['services_list'] = Service.objects.filter(main_service__id=SERVICE_1C_ID)\
        #     .select_related('extension')\
        #     .prefetch_related('extension__company_type')\
        
        service_home_list = ServiceList.objects.get(id=1)
        context['service_list'] = service_home_list.services.all()
        
        print(service_home_list.services.all())

        context['companies'] = CompanyType.objects.all()

        company_type_list = ['Услуги Среднему и малому бизнесу','Коммерческим фирмам']
        context['com_services_1с'] = Service.objects\
            .filter(category__name='Продукты 1С:Предприятие')\
            .select_related('extension')\
            .filter(extension__company_type__name__in=company_type_list)
        context['gov_services_1c'] = Service.objects\
            .filter(category__name='Продукты 1С:Предприятие')\
            .select_related('extension')\
            .filter(extension__company_type__name='Государственным предприятиям',)

        return context

def about(request):
    return render(request, 'about.html', )