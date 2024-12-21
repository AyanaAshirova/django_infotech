from django.urls import path
from. import views


urlpatterns = [
    path('<slug>/', views.MainServiceView.as_view(), name='main_service'),
    path('order_create/<service_id>/<main_service_id>/', views.OrderCreate.as_view(), name='order_create'),
    path('<main_service_slug>/<service_slug>/', views.ServiceDetail.as_view(), name='service_detail'),
]