from .views import (
CustomAuthToken,
doctorAccountViewAdmin,
docregistrationViewAdmin,
approveDoctorViewAdmin, 
appointmentViewAdmin,
patientRegistrationViewAdmin,
patientAccountViewAdmin,
patientHistoryViewAdmin,
approvePatientViewAdmin,
approveAppointmentViewAdmin,
)

from django.urls import path



app_name='hospitalAdmin'
urlpatterns = [
    #Admin login
    path('login/', CustomAuthToken.as_view(), name='api_admin_login'),

 
    #Approve Doctor
    path('approve/doctors/', approveDoctorViewAdmin.as_view(), name='api_doctors_approve_admin'),
    path('approve/doctor/<uuid:pk>/', approveDoctorViewAdmin.as_view(), name='api_doctor_detail_approve_admin'),

    #Approve Patient
    path('approve/patients/', approvePatientViewAdmin.as_view(), name='api_patients_approve_admin'),
    path('approve/patient/<uuid:pk>/', approvePatientViewAdmin.as_view(), name='api_patient_detail_approve_admin'),

    # Approve Appointment
    path('approve/appointments/', approveAppointmentViewAdmin.as_view(), name='api_appointment_approve_admin'),
    path('approve/appointment/<int:pk>', approveAppointmentViewAdmin.as_view(), name='api_appointment_approve_detail_admin'),

    #Doctor management
    path('doctor/registration/', docregistrationViewAdmin.as_view(), name='api_doctors_registration_admin'),
    path('doctors/', doctorAccountViewAdmin.as_view(), name='api_doctors_admin'),
    path('doctor/<uuid:pk>/', doctorAccountViewAdmin.as_view(), name='api_doctor_detail_admin'),
    
    #patient Management
    path('patient/registration/', patientRegistrationViewAdmin.as_view(), name='api_patient_registration_admin'),
    path('patients/', patientAccountViewAdmin.as_view(), name='api_patients_admin'),
    path('patient/<uuid:pk>/', patientAccountViewAdmin.as_view(), name='api_patient_detail_admin'),
    path('patient/<uuid:pk>/history/', patientHistoryViewAdmin.as_view(), name='api_patient_history_admin'),
    path('patient/<uuid:pk>/history/<int:hid>/', patientHistoryViewAdmin.as_view(), name='api_patient_history_admin'),

    #Appointment Management
    path('appointments/', appointmentViewAdmin.as_view(), name='api_appointments_admin'),
    path('appointment/<int:pk>/', appointmentViewAdmin.as_view(), name='api_appointment_detail_admin'),

]