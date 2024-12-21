from django.db import models
from django.db import models
from Services.models import Service, MainService


# class PortfolioItem(models.Model):
#     name = models.CharField(max_length=252)
#     service = models.ForeignKey(Service, related_name='portfolio_items', on_delete=models.CASCADE)
#     main_service = models.ForeignKey(MainService, related_name='portfolio_items', on_delete=models.CASCADE)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     link = models.URLField(blank=True, null=True)


#     def __str__(self) -> str:
#         return self.name



# class PortfolioImage(models.Model):
#     portfolio_item = models.ForeignKey(PortfolioItem, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='portfolio_images/')


    # def __str__(self) -> str:
    #     return f'Image for - {self.portfolio_item.name}'



class Contacts(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    working_hours = models.CharField(max_length=100, verbose_name='Часы работы', blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)


