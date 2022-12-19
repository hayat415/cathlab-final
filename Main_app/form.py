from django import forms
from django.forms import ModelForm
from .models import Patient, Angio


class PatientForm(ModelForm):
    class Meta:
        model=Patient
        fields=('name', 'age', 'sex', 'address', 'cnic','indication', 'visit_number', 'Date', 'discharge_date', 'operator', 'procedure')
        labels={
            'name':'Enter Patient Name',
            'age': 'Enter Patient Age',
        }
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Patient Name'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'cnic':forms.TextInput(attrs={'class':'form-control'}),
            'indication':forms.TextInput(attrs={'class':'form-control'}),
            'visit_number':forms.TextInput(attrs={'class':'form-control'}),
            'Date':forms.DateInput(attrs={'type':'date',}),
            'discharge_date':forms.DateInput(attrs={'type': 'date',}),
            
            
        }
        #fields="__all__"


class SearchForm(forms.ModelForm):
    Date=forms.DateField(required=False)
    discharge_date=forms.DateField(required=False)
    class Meta:
        model=Patient
        fields=['name', 'Date','discharge_date']


class AngioForm (ModelForm):
    class Meta:
        model=Angio
        fields=['lms']