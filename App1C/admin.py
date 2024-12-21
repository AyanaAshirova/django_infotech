from django.contrib import admin
from .models.company_type import CompanyType
from .models.industry_solution import IndustrySolution
from .models.task_solution import TaskSolution
from .models.service_extension_for_1c import ServiceExtensionFor1C


admin.site.register(ServiceExtensionFor1C)
admin.site.register(CompanyType)
admin.site.register(TaskSolution)
admin.site.register(IndustrySolution)