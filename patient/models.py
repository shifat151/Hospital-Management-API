from django.db import models
from account.models import User
from doctor.models import doctor

# Create your models here.

class patient(models.Model):

    age= models.PositiveIntegerField()
    address= models.TextField()
    mobile=models.CharField(max_length=20)
    status=models.BooleanField(default=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.username

class patient_history(models.Model):
    Cardiologist='CL'
    Dermatologists='DL'
    Emergency_Medicine_Specialists='EMC'
    Immunologists='IL'
    Anesthesiologists='AL'
    Colon_and_Rectal_Surgeons='CRS'

    #The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name. 
    department_choices=[(Cardiologist,'Cardiologist'),
        (Dermatologists,'Dermatologists'),
        (Emergency_Medicine_Specialists,'Emergency Medicine Specialists'),
        (Immunologists,'Immunologists'),
        (Anesthesiologists,'Anesthesiologists'),
        (Colon_and_Rectal_Surgeons,'Colon and Rectal Surgeons')
    ]
    admit_date=models.DateField(verbose_name="Admit Date",auto_now=False, auto_now_add=True)
    symptomps=models.TextField()
    department=models.CharField(max_length=3, choices=department_choices, default=Cardiologist)
    release_date=models.DateField(verbose_name="Release Date",auto_now=False, auto_now_add=False, blank=True)
    patient=models.ForeignKey(patient, on_delete=models.CASCADE)
    assigned_doctor=models.OneToOneField(doctor, on_delete=models.CASCADE)
    

class Appointment(models.Model):
    appontment_date=models.DateField(verbose_name="Appointment date",auto_now=False, auto_now_add=False)
    appointment_time=models.TimeField(verbose_name="Appointement time", auto_now=False, auto_now_add=False)
    status=models.BooleanField(default=False)
    patient=models.ForeignKey(patient_history, on_delete=models.CASCADE)
    doctor=models.OneToOneField(doctor, on_delete=models.CASCADE)



class patient_discharge(models.Model):
    room_charge=models.PositiveIntegerField(verbose_name="Room charge", null=False)
    medicine_cost=models.PositiveIntegerField(verbose_name="Medicine cost", null=False)
    doctor_fee=models.PositiveIntegerField(verbose_name="Doctor Fee", null=False)
    Other_charge=models.PositiveIntegerField(verbose_name="Other charges", null=False)
    patient_details=models.OneToOneField(patient_history, on_delete=models.CASCADE)









    

    