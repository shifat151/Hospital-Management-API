from .views import (
CustomAuthToken,
doctorAccountViewAdmin,
docregistrationViewAdmin,
appointmentmentViewAdmin,
approveDoctorViewAdmin, 
approveAppointmentViewAdmin, 
patientRegistrationViewAdmin,
patientAccountViewAdmin)
from django.urls import path



app_name='hospitalAdmin'
urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='api_admin_login'),
    path('doctors/', doctorAccountViewAdmin.as_view(), name='api_doctors_admin'),
    path('doctor/registration/', docregistrationViewAdmin.as_view(), name='api_doctors_registration_admin'),
    path('doctor/<uuid:pk>/', doctorAccountViewAdmin.as_view(), name='api_doctor_detail_admin'),
    path('approve/doctors/', approveDoctorViewAdmin.as_view(), name='api_doctors_approve_admin'),
    path('approve/doctor/<uuid:pk>', approveDoctorViewAdmin.as_view(), name='api_doctors_approve_admin'),
    path('appointments/', appointmentmentViewAdmin.as_view(), name='api_appointments_admin'),
    path('appointment/<int:pk>/', appointmentmentViewAdmin.as_view(), name='api_appointment_detail_admin'),
    path('approve/appointments/', approveAppointmentViewAdmin.as_view(), name='api_appointment_approve_admin'),
    path('approve/appointment/<int:pk>', approveAppointmentViewAdmin.as_view(), name='api_appointment_approve_detail_admin'),
    path('patients/', patientAccountViewAdmin.as_view(), name='api_patients_admin'),
    path('patient/registration/', patientRegistrationViewAdmin.as_view(), name='api_patient_registration_admin'),
    path('patient/<uuid:pk>/', patientAccountViewAdmin.as_view(), name='api_patient_detail_admin'),
]