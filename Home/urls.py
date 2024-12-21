from django.urls import path, include
from. import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('1c/', include('App1C.urls')),
    path('services/', include('Services.urls')),
    path('', views.Index.as_view(), name='home'),
]
