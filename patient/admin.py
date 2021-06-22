from django.contrib import admin
from . models import patient, patient_history, Appointment, patient_discharge

# Register your models here.

admin.site.register(patient)
admin.site.register(patient_history)
admin.site.register(Appointment)
admin.site.register(patient_discharge)
