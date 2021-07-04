from .views import (
CustomAuthToken,doctorAccountViewAdmin)
from django.urls import path



app_name='hospitalAdmin'
urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='api_admin_login'),
    path('doctors/', doctorAccountViewAdmin.as_view(), name='api_doctors_admin'),
    path('doctors/<int:pk>', doctorAccountViewAdmin.as_view(), name='api_doctor_detail_admin')
    # path('profile/', patientProfileView.as_view(), name='api_patient_profile'),
    # path('history/', patientHistoryView.as_view(), name='api_patient_history'),


]