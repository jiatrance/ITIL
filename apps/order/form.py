from django import forms
from .models import WorkOrder


class NewOrderForm(forms.Form):
    phone=forms.IntegerField(required=True)
    title=forms.CharField(required=True)
    description=forms.CharField(required=True)