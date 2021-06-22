from .views import registrationView
from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token

app_name='doctor'
urlpatterns = [
    path('registration/', registrationView.as_view(), name='api_doctor_registration'),
    # path('doctor-login/', obtain_auth_token, name='login'),
]