from django.contrib import admin
from . models import patient, patient_history, Appointment, patient_cost

# Register your models here.

# admin.site.register(patient)
# admin.site.register(patient_history)
admin.site.register(Appointment)
admin.site.register(patient_cost)

class PatientCost(admin.TabularInline):
    model=patient_cost

class PatientAppointment(admin.TabularInline):
    model=Appointment

class PatientHistoryAdmin(admin.ModelAdmin):
    list_display=('patient', 'assigned_doctor','admit_date','department','release_date')
    inlines=[PatientAppointment, PatientCost]

admin.site.register(patient_history, PatientHistoryAdmin)

class PatientHistoryInline(admin.StackedInline):
    model=patient_history
    
    

class PatientAdmin(admin.ModelAdmin):
    list_display=('user','age','address','mobile')
    inlines=[PatientHistoryInline]

admin.site.register(patient, PatientAdmin)





