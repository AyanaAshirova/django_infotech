from django.db import models
from . import Service

class ServiceList(models.Model):
    services = models.ManyToManyField(Service, related_name='service_list')
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title