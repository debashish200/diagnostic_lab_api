from django.contrib import admin
from .models import Patient, LabReport


admin.site.register(Patient)
admin.site.register(LabReport)