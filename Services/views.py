from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.db.models import Count, Q, Model
from django.views.generic import CreateView, ListView, View, TemplateView, DetailView
from django import urls
from django.contrib import messages

from .forms import *
from .models import *
from App1C.views import SERVICE_1C_SLUG, SERVICE_1C_ID




class MainServiceView(TemplateView):
    template_name = 'Services/index.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if kwargs.get('slug') == SERVICE_1C_SLUG:
            return redirect(SERVICE_1C_SLUG)
        
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        main_service = get_object_or_404(MainService, slug=kwargs.get('slug'))

        context = super().get_context_data(**kwargs)
        context['main_service'] = main_service
        context['categories'] = ServiceCategory.objects.filter(main_service=main_service)
        context['services'] = Service.objects.filter(main_service=main_service)

        return context
        


class ServiceDetail(DetailView):
    model = Service
    slug_field='slug'
    template_name = 'Services/service_detail.html'
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if kwargs.get('main_service_slug') == SERVICE_1C_SLUG:
            return redirect('1c_service_detail', slug=kwargs.get('service_slug'))
        
        return super().get(request, *args, **kwargs)
    
    def get_object(self) -> Model:
        return get_object_or_404(Service, slug=self.kwargs.get('service_slug'))


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
            context = super().get_context_data(**kwargs)
            context['main_service'] = get_object_or_404(MainService, slug=self.kwargs.get('main_service_slug'))
            
            return context
    



def category_detail(request, slug):
    return render(request, 'Services/category_detail.html')



from django.views.decorators.csrf import csrf_exempt
import asyncio
from TeleBot.bot import send_message


class OrderCreate(View):
    model = Order

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        service = get_object_or_404(Service, id=kwargs.get('service_id'))
        main_service = get_object_or_404(MainService, id=kwargs.get('main_service_id'))
        if form.is_valid():
            order = form.save(commit=False)
            order.service = service
            order.main_service = main_service
            ms_body = str(f'{order.name}   {order.email}  тел: {order.phone} \n{order.details}\nid{service.id}: {service.name}')
            asyncio.run(send_message(ms_body))
            order.save()
            messages.success(request, 'Отправлено')



            return redirect('service_detail', main_service_slug=main_service.slug, service_slug=service.slug)
        
        messages.error(request, 'Возникла ошибка при отправке!')
        return redirect('service_detail', main_service_slug=main_service.slug, service_slug=service.slug)
        

    def get(self, request, *args, **kwargs):
        service = get_object_or_404(Service, id=kwargs.get('service_id'))
        main_service = get_object_or_404(MainService, id=kwargs.get('main_service_id'))
        return redirect('service_detail', main_service_slug=main_service.slug, service_slug=service.slug)


    # def form_valid(self, form: BaseModelForm) -> HttpResponse:
    #     form.instance.service = get_object_or_404(Service, id=self.request.POST.get('service_id'))
    #     form.instance.main_service = get_object_or_404(MainService, id=self.request.POST.get('main_service_id'))
    #     return super().form_valid(form)
    
    # def get_success_url(self) -> str:
    #     return super().get_success_url()
