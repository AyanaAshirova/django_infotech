from typing import Any

from .models import *
from Services.models import *

SERVICE_1C_ID=1
SERVICE_1C_SLUG='1c'

class DataMixin:
    paginate_by = 7  

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['main_service'] = MainService.objects.get(id=SERVICE_1C_ID)
        return context
    



class CompanyTaskIndustry:
    def get_company_types(self):
        return CompanyType.objects.all()
    
    def get_task_slns(self):
        return TaskSolution.objects.all()
    
    def get_industry_slns(self):
        return IndustrySolution.objects.all()
    
    def get_categories(self):
        return ServiceCategory.objects.filter(main_service__id=SERVICE_1C_ID)

