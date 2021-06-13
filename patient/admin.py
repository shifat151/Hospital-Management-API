from django.contrib import admin
from . models import patient, patient_history

# Register your models here.

admin.site.register(patient)
admin.site.register(patient_history)
