from django import forms
from django.forms import ModelForm
from .models import Patient


class PatientForm(ModelForm):
    class Meta:
        model=Patient
        fields="__all__"


class SearchForm(forms.ModelForm):
    Date=forms.DateField(required=False)
    discharge_date=forms.DateField(required=False)
    class Meta:
        model=Patient
        fields=['name', 'Date','discharge_date']