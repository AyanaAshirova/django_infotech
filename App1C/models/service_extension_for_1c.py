from django.db import models
from Services.models.service import Service
from .company_type import CompanyType
from .industry_solution import IndustrySolution
from .task_solution import TaskSolution


class ServiceExtensionFor1CQuerySet(models.QuerySet):
    def filter_by_category(self, id):
        return ServiceExtensionFor1C.objects.filter(category__id=id)
    
    def filter_by_category_list(self, category_list):
        return ServiceExtensionFor1C.objects.filter(category__id=id)


class ServiceExtensionFor1C(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name='extension')
    brand = models.CharField(max_length=20, default='1С:Предприятие')
    delivery_method = models.CharField(max_length=50, default="Электронная поставка")
    
    company_type = models.ManyToManyField(CompanyType, related_name='service_1C', blank=True)
    industry_solutions = models.ManyToManyField(IndustrySolution, related_name='service_1C', blank=True)
    task_solutions = models.ManyToManyField(TaskSolution, related_name='service_1C', blank=True)

    def __str__(self):
        return f"Расширение - {self.service.name}"

