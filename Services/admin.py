from django.contrib import admin
from .models import *

admin.site.register(MainService)
admin.site.register(Service)
admin.site.register(ServiceCategory)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'service', 'main_service', 'status']
    list_filter = ['main_service','status', 'created_at']
    search_fields = ['name', 'service__name']


class ServiceListAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    filter_horizontal = ['services']

admin.site.register(ServiceList, ServiceListAdmin)