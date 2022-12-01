from django.contrib import admin
from .models import Patient
from .models import Operator
from .models import Procedure 
from .models import PCI
from .models import Angio
#from daterange_filter.filter import DateRangeFilter

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display= ('name','Date','visit_number')
    list_filter=('operator','Date')

# Register your models here.
#admin.site.register(Patient)
#admin.site.register(Procedure)
admin.site.register(Operator)
admin.site.register(PCI)
admin.site.register(Angio)
admin.site.register(Procedure)