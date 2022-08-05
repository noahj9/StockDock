from django import forms
from django.forms import ModelForm
from .models import Docket

# Create form for docket creation
class NewDocketForm(ModelForm):
    class Meta:
        model = Docket
        fields = 'customer_name', 'date'
