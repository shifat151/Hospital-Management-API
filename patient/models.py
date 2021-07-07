from django.db import models
from account.models import User
from doctor.models import doctor


# Create your models here.

class patient(models.Model):

    age= models.DecimalField(max_digits=4,decimal_places=1)
    address= models.TextField()
    mobile=models.CharField(max_length=20)
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
    release_date=models.DateField(verbose_name="Release Date",auto_now=False, auto_now_add=False, null=True, blank=True)
    patient=models.ForeignKey(patient, on_delete=models.CASCADE)
    assigned_doctor=models.ForeignKey(doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.get_name
    

class Appointment(models.Model):
    appointment_date=models.DateField(verbose_name="Appointment date",auto_now=False, auto_now_add=False)
    appointment_time=models.TimeField(verbose_name="Appointement time", auto_now=False, auto_now_add=False)
    status=models.BooleanField(default=False)
    #related_name fix reverse relationship field name with patient_history model
    patient_history=models.ForeignKey(patient_history,related_name='patient_appointments', on_delete=models.CASCADE)
    doctor=models.ForeignKey(doctor,related_name='doctor_appointments',null=True, on_delete=models.SET_NULL)

    @property
    def patient_name(self):
        self.patient_history.patient.get_name
    
    def __str__(self):
        return self.patient_history.patient.get_name+'-'+self.doctor.get_name



class patient_cost(models.Model):
    room_charge=models.PositiveIntegerField(verbose_name="Room charge", null=False)
    medicine_cost=models.PositiveIntegerField(verbose_name="Medicine cost", null=False)
    doctor_fee=models.PositiveIntegerField(verbose_name="Doctor Fee", null=False)
    other_charge=models.PositiveIntegerField(verbose_name="Other charges", null=False)
    patient_details=models.OneToOneField(patient_history, related_name='costs', on_delete=models.CASCADE)

    @property
    def total_cost(self):
        return "{} tk" .format(self.room_charge+self.medicine_cost+self.doctor_fee+self.other_charge)
    

    def __str__(self):
        return self.patient_details.patient.get_name+'-'+str(self.patient_details.admit_date)
    










    

    