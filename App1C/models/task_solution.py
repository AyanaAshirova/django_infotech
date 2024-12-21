from django.db import models
from slugify import slugify


class TaskSolution(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super (TaskSolution, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    