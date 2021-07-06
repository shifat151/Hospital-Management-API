from .views import (
CustomAuthToken,
doctorAccountViewAdmin,
docregistrationViewAdmin,
appointmentmentViewAdmin,
approveDoctorViewAdmin, approveAppointmentViewAdmin)
from django.urls import path



app_name='hospitalAdmin'
urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='api_admin_login'),
    path('doctors/', doctorAccountViewAdmin.as_view(), name='api_doctors_admin'),
    path('doctors/<uuid:pk>/', doctorAccountViewAdmin.as_view(), name='api_doctor_detail_admin'),
    path('doctor/registration/', docregistrationViewAdmin.as_view(), name='api_doctors_admin'),
    path('approve/doctors/', approveDoctorViewAdmin.as_view(), name='api_doctors_approve_admin'),
    path('approve/doctors/<uuid:pk>', approveDoctorViewAdmin.as_view(), name='api_doctors_approve_admin'),
    path('appointments/', appointmentmentViewAdmin.as_view(), name='api_appointments_admin'),
    path('appointments/<int:pk>/', appointmentmentViewAdmin.as_view(), name='api_appointment_detail_admin'),
    path('approve/appointments/', approveAppointmentViewAdmin.as_view(), name='api_appointment_approve_admin'),
    path('approve/appointments/<int:pk>', approveAppointmentViewAdmin.as_view(), name='api_appointment_approve_detail_admin'),
]