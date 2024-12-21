from django.db import models
from slugify import slugify

from Services.models.main_service import MainService
from .service_category import ServiceCategory


class Service(models.Model):
    name = models.CharField(max_length=200)
    main_service = models.ForeignKey(MainService, on_delete=models.DO_NOTHING)
    slug = models.SlugField(unique=True, blank=True, max_length=200)
    category = models.ForeignKey(ServiceCategory, related_name='services', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unit = models.CharField(max_length=20, default='за час', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super (Service, self).save(*args, **kwargs)
