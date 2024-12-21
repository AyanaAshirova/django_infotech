from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import ListView, DetailView, TemplateView


from Services.forms import OrderForm
from Services.models import MainService, ServiceCategory, Service
from .models import *
from .utils import *

# in edit
class Index(DataMixin, CompanyTaskIndustry, TemplateView):
    template_name = 'App1C/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['categories'] = ServiceCategory.objects.filter(main_service__id=SERVICE_1C_ID)
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



class IdustryDetail(DataMixin, CompanyTaskIndustry, ListView):
    template_name = 'App1C/sector_detail.html'
    model = Service

    def get_queryset(self) -> QuerySet[Any]:
        slug=self.kwargs.get('slug')
        return Service.objects\
            .filter(main_service=SERVICE_1C_ID)\
            .select_related('extension')\
            .filter(extension__industry_solutions__slug=slug)
 

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['sector'] = get_object_or_404(IndustrySolution, slug=slug)
        context['other_sectors_name'] = 'Все отрасли'

        return context
    

class TaskDetail(DataMixin, CompanyTaskIndustry, ListView):
    template_name = 'App1C/sector_detail.html'
    model = Service

    def get_queryset(self) -> QuerySet[Any]:
        slug=self.kwargs.get('slug')
        return Service.objects\
            .filter(main_service=SERVICE_1C_ID)\
            .select_related('extension')\
            .filter(extension__task_solutions__slug=slug)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['sector'] = get_object_or_404(TaskSolution, slug=slug)
        context['other_sectors_name'] = 'Все задачи'

        return context


class CategoryDetail(DataMixin, CompanyTaskIndustry, ListView):
    template_name = 'App1C/category_detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['category'] = ServiceCategory.objects.get(slug=self.kwargs.get('slug'))
        context['categories'] = ServiceCategory.objects.filter(main_service__id=SERVICE_1C_ID)
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        return Service.objects.filter(category__slug=self.kwargs.get('slug'))



class ServiceListView(DataMixin, ListView):
    model = Service
    template_name = 'App1C/filter.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['sector_name'] = 'Все сервисы по автомотизации 1С'
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        return Service.objects.filter(main_service__id=SERVICE_1C_ID)



class Filter(DataMixin, ListView):
    template_name = 'App1C/filter.html'
    model = Service

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['sector_name'] = 'Фильтр'
        return context


    def get_queryset(self) -> QuerySet[Any]:
        query_set = Service.objects\
            .filter(main_service__id=SERVICE_1C_ID)\
            .select_related('extension')
        filters = {}

        company_type = self.request.GET.get('company_type')
        industry_sln = self.request.GET.getlist('industry_sln')
        task_sln = self.request.GET.getlist('task_sln')

        if company_type:
            filters['extension__company_type'] = company_type

        if task_sln:
            filters['extension__task_solutions__slug__in'] = task_sln

        if industry_sln:
            filters['extension__industry_solutions__slug__in'] = industry_sln

        return query_set.filter(**filters).distinct()
    


class ServiceDetail(DataMixin, DetailView):
    model = Service
    template_name = 'App1C/service_detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['sector'] = {'name': 'Сервис'}
        context['form'] = OrderForm()
        return context

    def get_queryset(self) -> QuerySet[Any]:
        return Service.objects\
            .select_related('extension')\
            .all()\
            .prefetch_related('extension__company_type')\
            .prefetch_related('extension__industry_solutions')\
            .prefetch_related('extension__task_solutions')\
            .filter(slug=self.kwargs.get('slug'))

