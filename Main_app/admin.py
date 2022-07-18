from django.contrib import admin
from .models import Patient
from .models import Operator
from .models import Procedure 
from .models import PCI
from .models import Angio

class PCIAdmin(admin.ModelAdmin):
    list_display= ('PCI_desc')


# Register your models here.
admin.site.register(Patient)
admin.site.register(Procedure)
admin.site.register(Operator)
admin.site.register(PCI)
admin.site.register(Angio)