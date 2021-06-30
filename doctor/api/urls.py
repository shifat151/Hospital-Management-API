from .views import registrationView, CustomAuthToken, doctorProfileView, doctorAppointmentView
from django.urls import path


app_name='doctor'
urlpatterns = [
    path('registration/', registrationView.as_view(), name='api_doctor_registration'),
    path('login/', CustomAuthToken.as_view(), name='api_doctor_login'),
    path('profile/', doctorProfileView.as_view(), name='api_doctor_profile'),
    path('appointments/', doctorAppointmentView.as_view(), name='api_doctor_profile'),


]