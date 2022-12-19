from webbrowser import get
from django.contrib import admin
from django.urls import path
from Main_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_panel'),
    path('',list_venues, name='a_list'),
    path('show_angio/<sudo_id>', show_angio, name='show-angio'),
    path('add_venue/',add_patient, name='add_patient'),
    path('dlist/', search, name='dlist'),
    path('proc/',proc, name='proc')
      
]
