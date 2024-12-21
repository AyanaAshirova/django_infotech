from Services.models.service import Service
from Services.models.service_category import ServiceCategory
from App1C.models.company_type import CompanyType
from App1C.models.industry_solution import IndustrySolution
from App1C.models.task_solution import TaskSolution
from django import template
from App1C.views import SERVICE_1C_ID
from django.db.models import Count

register = template.Library()

@register.inclusion_tag('App1C/tags/sidebar_1c.html', takes_context=True)
def get_sidebar_data(context):
    category = context.get('category')
    company_types = CompanyType.objects.all()
    industry_sln =IndustrySolution.objects.all()
    task_sln = TaskSolution.objects.all()
    categories = ServiceCategory.objects\
        .filter(main_service=SERVICE_1C_ID)\
        # .aaggregate(services_count=Count('services'))

    

    return {
        'companies': company_types,
        'industry_sln': industry_sln,
        'categories': categories,
        'category': category,
        'task_sln': task_sln,
        }
