from django import forms
from django.forms import ModelForm
from .models import Docket, Stock, Proof, Ink
from .widgets import DatePickerInput
from django.urls import reverse_lazy
from django_addanother.widgets import AddAnotherWidgetWrapper
from .utils import OptionalChoiceField


# Create form for docket creation
class NewDocketForm(ModelForm): #model form for new docket
    machines = ((1, 'Xerox 1000'),
            (2, 'Xerox Nuvera'),
            (3, 'Xerox Versant'),
            (4, 'Roland'),
            (5, '9810'),
            (6, 'DI'),
            (7, 'Komori'),
            (8, 'Outsource'),
            (9, 'Design'),
            (10, 'Shipping'),
            (11, 'Mailing'),
            (12, 'Postage'),
            (13, 'PLS'),
            (14, 'Other'),
            (15, 'N/A'))
    flexibility = ((1, 'Flexible'),
                    (2, 'Firm'))

    stock_1 = forms.ModelChoiceField(queryset=Stock.objects.all(), widget=forms.Select(attrs = {'class': 'form-control'}))
    stock_2 = forms.ModelChoiceField(queryset=Stock.objects.all(), widget=forms.Select(attrs = {'class': 'form-control'}))
    stock_3 = forms.ModelChoiceField(queryset=Stock.objects.all(), widget=forms.Select(attrs = {'class': 'form-control'}))
    proof_1 = forms.ModelChoiceField(queryset=Proof.objects.all(), widget=forms.Select(attrs = {'class': 'form-control'}))
    proof_2 = forms.ModelChoiceField(queryset=Proof.objects.all(), widget=forms.Select(attrs = {'class': 'form-control'}))
    proof_3 = forms.ModelChoiceField(queryset=Proof.objects.all(), widget=forms.Select(attrs = {'class': 'form-control'}))
    inks_1 = OptionalChoiceField(choices=list(Ink.objects.all().values_list("name", "name")))
    inks_2 = forms.ModelChoiceField(queryset=Ink.objects.all(), widget=forms.Select(attrs = {'class': 'form-control'}))
    inks_3 = forms.ModelChoiceField(queryset=Ink.objects.all(), widget=forms.Select(attrs = {'class': 'form-control'}))
    machine_1 =forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices = machines)
    machine_2 =forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices = machines)
    machine_3 =forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs = {'class': 'list-inline'}),choices = machines)
    flexibility = forms.MultipleChoiceField(widget=forms.Select(attrs = {'class':'form-control'}), choices = flexibility)

    class Meta:
        model = Docket #the model it follows
        fields = ('customer_name', 'date', 'date_required', 'flexibility', 'contact',  #the fields that are part of the form
                    'account', 'terms', 'customer_PO',
                    'deposit', 'rep', 'csr', 'reception_notes',
                    'quantity_1', 'description_1', 'finished_size_1', 'stock_1', 'machine_1', 'run_quantity_1', 'sheet_size_1', 'run_size_1', 'proof_1', 'inks_1', 'instructions_1', 'bindery_1', 'file_1', 'price_comission_1', 'shipping_1',
                    'quantity_2', 'description_2', 'finished_size_2', 'stock_2', 'machine_2', 'run_quantity_2', 'sheet_size_2', 'run_size_2', 'proof_2', 'inks_2', 'instructions_2', 'bindery_2', 'file_2', 'price_comission_2', 'shipping_2',
                    'quantity_3', 'description_3', 'finished_size_3', 'stock_3', 'machine_3', 'run_quantity_3', 'sheet_size_3', 'run_size_3', 'proof_3', 'inks_3', 'instructions_3', 'bindery_3', 'file_3', 'price_comission_3', 'shipping_3', 'reception_notes'
                )

        widgets = { #allows utilization of bootstrap form controls and styling
            'customer_name': AddAnotherWidgetWrapper(forms.Select(attrs={'class':'form-control'}), reverse_lazy('client-create')),
            'date': DatePickerInput(attrs={'class': 'form-control'}), #using custom datepicker widget
            'date_required': DatePickerInput(attrs={'class': 'form-control'}),
            'contact': AddAnotherWidgetWrapper(forms.Select(attrs={'class':'form-control','id':'contact-select'}), reverse_lazy('contact-create')),
            'account': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quote Number'}),
            'terms': forms.Select(attrs={'class':'form-control'}),
            'customer_PO': forms.TextInput(attrs={'class':'form-control'}),
            'deposit': forms.Select(attrs={'class':'form-control'}),
            'rep': forms.Select(attrs={'class':'form-control'}),
            'csr': forms.Select(attrs={'class':'form-control'}),
            'quantity_1': forms.TextInput(attrs={'class':'form-control'}),
            'description_1': forms.TextInput(attrs={'class':'form-control'}),
            'finished_size_1': forms.TextInput(attrs={'class':'form-control'}),
            'run_quantity_1': forms.TextInput(attrs={'class':'form-control'}),
            'sheet_size_1': forms.TextInput(attrs={'class':'form-control'}),
            'run_size_1': forms.TextInput(attrs={'class':'form-control'}),
            'instructions_1': forms.TextInput(attrs={'class':'form-control'}),
            'bindery_1': forms.TextInput(attrs={'class':'form-control'}),
            'file_1': forms.TextInput(attrs={'class':'form-control'}),
            'price_comission_1': forms.TextInput(attrs={'class':'form-control'}),
            'shipping_1': forms.TextInput(attrs={'class':'form-control'}),
            'quantity_2': forms.TextInput(attrs={'class':'form-control'}),
            'description_2': forms.TextInput(attrs={'class':'form-control'}),
            'finished_size_2': forms.TextInput(attrs={'class':'form-control'}),
            'machine_2': forms.CheckboxSelectMultiple(attrs={'class':'form-check form-check-inline ml-4'}),
            'run_quantity_2': forms.TextInput(attrs={'class':'form-control'}),
            'sheet_size_2': forms.TextInput(attrs={'class':'form-control'}),
            'run_size_2': forms.TextInput(attrs={'class':'form-control'}),
            'instructions_2': forms.TextInput(attrs={'class':'form-control'}),
            'bindery_2': forms.TextInput(attrs={'class':'form-control'}),
            'file_2': forms.TextInput(attrs={'class':'form-control'}),
            'price_comission_2': forms.TextInput(attrs={'class':'form-control'}),
            'shipping_2': forms.TextInput(attrs={'class':'form-control'}),
            'quantity_3': forms.TextInput(attrs={'class':'form-control'}),
            'description_3': forms.TextInput(attrs={'class':'form-control'}),
            'finished_size_3': forms.TextInput(attrs={'class':'form-control'}),
            'machine_3': forms.CheckboxSelectMultiple(attrs={'class':'form-check form-check-inline ml-4'}),
            'run_quantity_3': forms.TextInput(attrs={'class':'form-control'}),
            'sheet_size_3': forms.TextInput(attrs={'class':'form-control'}),
            'run_size_3': forms.TextInput(attrs={'class':'form-control'}),
            'instructions_3': forms.TextInput(attrs={'class':'form-control'}),
            'bindery_3': forms.TextInput(attrs={'class':'form-control'}),
            'file_3': forms.TextInput(attrs={'class':'form-control'}),
            'price_comission_3': forms.TextInput(attrs={'class':'form-control'}),
            'shipping_3': forms.TextInput(attrs={'class':'form-control'}),
            'reception_notes': forms.TextInput(attrs={'class':'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super(NewDocketForm, self).__init__(*args, **kwargs)
            self.fields['quantity_2', 'description_2', 'finished_size_2', 'stock_2', 'machine_2', 'run_quantity_2', 'sheet_size_2', 'run_size_2', 'proof_2', 'inks_2', 'instructions_2', 'bindery_2', 'file_2', 'price_comission_2', 'shipping_2',
                    'quantity_3', 'description_3', 'finished_size_3', 'stock_3', 'machine_3', 'run_quantity_3', 'sheet_size_3', 'run_size_3', 'proof_3', 'inks_3', 'instructions_3', 'bindery_3', 'file_3', 'price_comission_3', 'shipping_3'].required = False
            self.field['inks_1'].widget.attrs['class'] = 'form-control'
