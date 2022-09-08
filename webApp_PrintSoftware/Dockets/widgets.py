from django import forms
from django.forms import ModelForm

class DatePickerInput(forms.DateInput): #custom widget that produces a calendar to pick date
    input_type = 'date'
