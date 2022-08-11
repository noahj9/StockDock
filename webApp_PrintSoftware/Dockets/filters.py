import django_filters
from .models import *
from django_filters import DateFilter

class DocketFilter(django_filters.FilterSet): #filter for searchable docket table
    date = DateFilter(field_name="date", lookup_expr="contains")
    class Meta:
        model = Docket
        fields = ('customer_name', 'rep')
