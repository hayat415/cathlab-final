from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .form import*
from .filter import PatientFilter
def show_angio(request, sudo_id):
    sudo=Patient.objects.get(pk=sudo_id),
    return render(request, 'show_angio.html',
        {'sudo': sudo})
      
def list_venues(request):
    venue_list=Patient.objects.all()
    return render(request, 'angio.html',
        {'venue_list': venue_list})

def add_patient(request):
    submitted=False
    if request.method=='POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dlist/?submitted=True')
    else:
        form=PatientForm
        if 'submitted'in request.GET:
            submitted=True
    return render(request, 'forms.html',{'form':form, 'submitted':submitted})

def search(request):
        p_list=Patient.objects.all()
        p_filter=PatientFilter(request.GET, queryset=p_list)
        return render(request, 'search.html', {'filter':p_filter})

    
