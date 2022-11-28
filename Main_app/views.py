from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *

def show_angio(request, sudo_id):
    sudo=Patient.objects.get(pk=sudo_id),
    return render(request, 'show_angio.html',
        {'sudo': sudo})
      
def list_venues(request):
    venue_list=Patient.objects.all()
    return render(request, 'angio.html',
        {'venue_list': venue_list})

def home(request):
    return render(request, 'home.html')
         

    
