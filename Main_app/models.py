from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
import datetime
from tinymce.models import HTMLField

class Procedure(models.Model):
    procedure_type=models.CharField(max_length=20)
    Cost=models.IntegerField()

    def __str__(self):
        return self.procedure_type

        
class Operator(models.Model):
    name=models.CharField(max_length=30)
    designation=models.CharField(max_length=25)
    def __str__(self):
        return self.name
   

class PCI(models.Model):
    pci_desc=HTMLField(default="Right Radial access used to engage LAD with Guiding Catheter JL-4 6F. Injection given lesion identified in LAD. BMW wire 0.014x190 cm wire used to cross the lesion in LAD. Pre dilatation done with Compliant 2.0x10 mm Balloon at 10 atm. Firehawk 3.0x18mm (DES) stent deployed in Proximal LAD inflated at 14 atm. Successful PCI done to LAD. TIMI grade III flow obtained with no immediate complications.")
    result_pci=models.CharField(max_length=100, default=" Successful PCI done to")
    recommendation=models.CharField(max_length=200, default="Dual Antiplatelet therapy")
   

class Angio(models.Model):
    TECHNICIAN_CHOICE=(
        ('Shabir Ahmed', 'Shabir Ahmed'),
        ('Ibrar Ahmed', 'Ibrar Ahmed'),        
    )
    #Heamodinamic 
    blood_pressure=models.IntegerField()
    respiratory_rate=models.IntegerField()
    saturation=models.IntegerField()
    heart_rate=models.IntegerField()
    #radiation
    flouro_time=models.IntegerField()
    contrast_received=models.FloatField()
    radiation_dose=models.FloatField()
    #Angio
    technician=models.CharField(max_length=200, choices=TECHNICIAN_CHOICE)
    text=HTMLField(default=" Right Radial Artery entered with Seldinger technique using  6F sheath. Diagnostic Catheter TIG II 5F used for LCA & JR-4 5F used for RCA. Standard views recorded. Pressure homeostasis achieved.")
    lms=models.TextField(default="Normal")
    lad=models.TextField(default="Proximal: Normal </br> Mid: Normal </br> Distal:Normal")
    ramus=models.TextField(null=True, blank=True, default="Not Present")
    lcx=models.TextField(default="Proximal: Normal </br> Distal:Normal")
    rca=models.TextField(default="Proximal: Normal </br> Mid: Normal </br> Distal:Normal")
    result_angio=models.CharField(max_length=50)
    recommendation_angio=models.CharField(max_length=100)
    

class Patient(models.Model):
    GENDER_CHOICE=(
        ('Male', 'Male'),
        ('Female', 'Female'),        
    )
    p_id = models.AutoField(primary_key=True)
    name=models. CharField(max_length=30)
    age=models.IntegerField()
    sex=models.CharField(max_length=6, choices=GENDER_CHOICE)
    address=models.CharField(max_length=20)
    cnic=models.IntegerField()
    indication=models.CharField(max_length=100)
    visit_number=models.IntegerField()
    Date=models.DateField() 
    discharge_date=models.DateField()
    operator=models.ForeignKey(Operator, on_delete=models.CASCADE)
    procedure=models.ForeignKey(Procedure, null=True, blank=True,on_delete=models.DO_NOTHING)
    angio=models.ForeignKey(Angio, blank=True, null=True, on_delete=models.CASCADE)
    pci=models.ForeignKey(PCI, blank=True, null=True, on_delete=models.CASCADE)
    def __str__ (self):
        return self.name 