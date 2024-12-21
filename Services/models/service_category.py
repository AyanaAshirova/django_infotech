from django.db import models
from slugify import slugify
from.main_service import MainService


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    main_service = models.ForeignKey(MainService, on_delete=models.DO_NOTHING)
    icon = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super (ServiceCategory, self).save(*args, **kwargs)

