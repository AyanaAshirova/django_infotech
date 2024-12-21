from django.urls import path
from. import views


urlpatterns = [
    path('', views.Index.as_view(), name='1c'),
    path('filter/', views.Filter.as_view(), name='filter'),
    path('task/<slug:slug>/', views.TaskDetail.as_view(), name='task_detail'),
    path('sector/<slug:slug>/', views.IdustryDetail.as_view(), name='sector_detail'),
    path('categories/<slug:slug>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('services/<slug:slug>/', views.ServiceDetail.as_view(), name='1c_service_detail'),
    path('services/', views.ServiceListView.as_view(), name='all_1c_services')
]