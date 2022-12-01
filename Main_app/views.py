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
            return HttpResponseRedirect('/list?submitted=True')
    else:
        form=PatientForm
        if 'submitted'in request.GET:
            submitted=True
    return render(request, 'forms.html',{'form':form, 'submitted':submitted})

def search(request):
        list=Patient.objects.all()
        p_filter=PatientFilter(request.GET, queryset=list)
        return render(request, 'search.html', {'filter':p_filter})

    
#def SearchDate (request):
    #queryset =Patient.objects.all()
    #form=SearchForm(request.POST or None)
    #context={
    #    "queryset":queryset,
     #   "form":form,
    #}
    #if request.method =='POST':
     #   category =form['name'].value()
      #  queryset=Patient.objects.filter(
       #     last_updated_range=[
        #        form['Date'].value(),
         #       form['discharge_date'].value()
          #  ]
        #)
    #else:
     #   "NO"
    #return render(request, 'search.html')