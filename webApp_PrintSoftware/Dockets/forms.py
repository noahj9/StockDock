from django import forms
from django.forms import ModelForm
from .models import Docket
from .widgets import DatePickerInput
from django.urls import reverse_lazy
from django_addanother.widgets import AddAnotherWidgetWrapper


# Create form for docket creation
class NewDocketForm(ModelForm): #model form for new docket
    class Meta:
        model = Docket #the model it follows
        fields = ('customer_name', 'date', 'date_required', 'contact',  #the fields that are part of the form
                    'account', 'phone', 'email', 'terms', 'customer_PO',
                    'deposit', 'rep', 'csr',
                    'quantity_1', 'description_1', 'finished_size_1', 'stock_1', 'machine_1', 'run_quantity_1', 'sheet_size_1', 'run_size_1', 'proof_1', 'inks_1', 'instructions_1', 'bindery_1', 'file_1', 'price_comission_1', 'shipping_1'
                )
        widgets = { #allows utilization of bootstrap form controls and styling
            'customer_name': forms.Select(attrs={'class':'form-control'}),
            'date': DatePickerInput(attrs={'class': 'form-control'}), #using custom datepicker widget
            'date_required': DatePickerInput(attrs={'class': 'form-control'}),
            'contact': AddAnotherWidgetWrapper(forms.Select(attrs={'class':'form-control'}), reverse_lazy('contact-create')),
            'account': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Account'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'(xxx)-xxx-xxxx'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'user@company.com'}),
            'terms': forms.TextInput(attrs={'class':'form-control'}),
            'customer_PO': forms.TextInput(attrs={'class':'form-control'}),
            'deposit': forms.TextInput(attrs={'class':'form-control'}),
            'rep': forms.Select(attrs={'class':'form-control'}),
            'csr': forms.Select(attrs={'class':'form-control'}),
            'quantity_1': forms.TextInput(attrs={'class':'form-control'}),
            'description_1': forms.TextInput(attrs={'class':'form-control'}),
            'finished_size_1': forms.TextInput(attrs={'class':'form-control'}),
            'stock_1': forms.TextInput(attrs={'class':'form-control'}),
            'machine_1': forms.CheckboxSelectMultiple(attrs={'class':'form-check form-check-inline ml-4'}),
            'run_quantity_1': forms.TextInput(attrs={'class':'form-control'}),
            'sheet_size_1': forms.TextInput(attrs={'class':'form-control'}),
            'run_size_1': forms.TextInput(attrs={'class':'form-control'}),
            'proof_1': forms.TextInput(attrs={'class':'form-control'}),
            'inks_1': forms.TextInput(attrs={'class':'form-control'}),
            'instructions_1': forms.TextInput(attrs={'class':'form-control'}),
            'bindery_1': forms.TextInput(attrs={'class':'form-control'}),
            'file_1': forms.TextInput(attrs={'class':'form-control'}),
            'price_comission_1': forms.TextInput(attrs={'class':'form-control'}),
            'shipping_1': forms.TextInput(attrs={'class':'form-control'}),
        }
