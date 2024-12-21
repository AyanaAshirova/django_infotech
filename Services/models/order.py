from django.db import models
from .service import Service
from .main_service import MainService

class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    details = models.TextField(blank=True, null=True)

    service = models.ForeignKey(Service, related_name='orders', on_delete=models.PROTECT)
    main_service = models.ForeignKey(MainService, related_name='orders', on_delete=models.PROTECT)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Ожидает обработки'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершено'),
        ('canceled', 'Отменено'),
        ),
        default='pending'
    )
    