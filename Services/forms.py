from .models.order import Order
from django.forms import BaseModelForm
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = ['name', 'phone', 'email', 'details']




    
