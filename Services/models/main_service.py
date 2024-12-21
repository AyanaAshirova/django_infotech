from django.db import models


class MainService(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=False, unique=True)
    icon = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    status = models.BooleanField(default='True')

    def __str__(self):
        return self.name
