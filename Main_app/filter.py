from .models import Patient
import django_filters

class PatientFilter(django_filters.FilterSet):
    class Meta:
        model=Patient
        fields=['name', 'Date',] 