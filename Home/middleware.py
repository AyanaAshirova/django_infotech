from django.contrib.sites.models import Site
from django.db import models

# class SiteMiddleware(models.Model):
#     def __inir__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         domain = request.get_host()
#         try:
#             site = Site.objects.get(domain=domain)
#             request.site = site
#         except Site.DoesNotExist:
#             request.site = Site.objects.get(id=1)

#         return self.get_response(request)