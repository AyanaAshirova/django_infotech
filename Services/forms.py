from .models.order import Order
from django import forms
from captcha.fields import CaptchaField


class OrderForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Order
        fields = ['name', 'phone', 'email', 'details']



    
