from webbrowser import get
from django.contrib import admin
from django.urls import path
from Main_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',list_venues ),
    path('show_angio/<sudo_id>', show_angio, name='show-angio'),
    path('home/',home, name='home'),
      
]
