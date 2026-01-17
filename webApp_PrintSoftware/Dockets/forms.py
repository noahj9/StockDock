from django import forms
from django.forms import ModelForm
from .models import Docket, Stock, Proof, Ink, Machine, Contact
from .widgets import DatePickerInput
from django.urls import reverse_lazy
from django_addanother.widgets import AddAnotherWidgetWrapper
from .utils import OptionalChoiceField


# Create form for docket creation
class NewDocketForm(ModelForm):
    flexibility = (('Flexible', 'Flexible'),('Firm','Firm'),('N/A','N/A'))

    stock_1 = forms.ModelChoiceField(queryset=Stock.objects.all(), widget=forms.Select(attrs = {'class': 'form-control'}))
    stock_2 = forms.ModelChoiceField(queryset=Stock.objects.all(), required = False, widget=forms.Select(attrs = {'class': 'form-control'}))
    stock_3 = forms.ModelChoiceField(queryset=Stock.objects.all(), required = False, widget=forms.Select(attrs = {'class': 'form-control'}))
    proof_1 = forms.ModelChoiceField(queryset=Proof.objects.all(), widget=forms.Select(attrs = {'class': 'form-control'}))
    proof_2 = forms.ModelChoiceField(queryset=Proof.objects.all(), required = False, widget=forms.Select(attrs = {'class': 'form-control'}))
    proof_3 = forms.ModelChoiceField(queryset=Proof.objects.all(), required = False, widget=forms.Select(attrs = {'class': 'form-control'}))
    Inks_1 = OptionalChoiceField(choices=list(Ink.objects.all().values_list("name", "name")))
    Inks_2 = OptionalChoiceField(choices=list(Ink.objects.all().values_list("name", "name")))
    Inks_3 = OptionalChoiceField(choices=list(Ink.objects.all().values_list("name", "name")))
    machine_1 =forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required = False, choices = list(Machine.objects.all().values_list("name", "name")))
    machine_2 =forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required = False, choices = list(Machine.objects.all().values_list("name", "name")))
    machine_3 =forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required = False, choices = list(Machine.objects.all().values_list("name", "name")))
    flexibility = forms.ChoiceField(widget=forms.Select(attrs = {'class':'form-control'}), choices = flexibility, required= False)

    class Meta:
        model = Docket
        fields = "__all__"

        widgets = { #allows utilization of bootstrap form controls and styling
            'customer_name': AddAnotherWidgetWrapper(forms.Select(attrs={'class':'form-control'}), reverse_lazy('client-create')),
            'date': DatePickerInput(attrs={'class': 'form-control'}), #using custom datepicker widget
            'date_required': DatePickerInput(attrs={'class': 'form-control'}),
            'contact': AddAnotherWidgetWrapper(forms.Select(attrs={'class':'form-control','id':'contact-select'}), reverse_lazy('contact-create')),
            'quote': forms.TextInput(attrs={'class':'form-control'}),
            'terms': forms.Select(attrs={'class':'form-control'}),
            'customer_PO': forms.TextInput(attrs={'class':'form-control'}),
            'deposit': forms.Select(attrs={'class':'form-control'}),
            'deposit_amount': forms.TextInput(attrs={'class':'form-control'}),
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
        self.fields['contact'].queryset = Contact.objects.all()
