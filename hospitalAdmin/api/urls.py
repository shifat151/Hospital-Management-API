from .views import (
CustomAuthToken,)
from django.urls import path



app_name='hospitalAdmin'
urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='api_admin_login'),
    # path('profile/', patientProfileView.as_view(), name='api_patient_profile'),
    # path('history/', patientHistoryView.as_view(), name='api_patient_history'),


]