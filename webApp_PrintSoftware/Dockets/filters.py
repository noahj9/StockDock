import django_filters
from .models import *
from django_filters import DateFilter, CharFilter

class DocketFilter(django_filters.FilterSet): #filter for searchable docket table
    date = DateFilter(field_name="date", lookup_expr="contains")
    description = CharFilter(field_name="description_1", lookup_expr='contains')
    class Meta:
        model = Docket
        fields = ('customer_name', 'rep')
