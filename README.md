# Hospital-Management-API

This is a hospital management API based on Django REST Framework. This API features three types of users - Doctor, Patient and Admin .
For authenticating user, Django REST Framework custom token authentication is used. Installation guide, API endpoints and sample request/response are given below.

## Please follow the below steps to install this application-
1. Install python 3.8 and pipenv.
2. Clone this repository- https://github.com/shifat151/Hospital-Management-API.git
3. Then go to the Hospital-Management-API-master directory: cd Hospital-Management-API-master
4. Install dependencies: pipenv install (This will create a virtual environment and install all depedencies).
5. Activate the virtual environment: pipenv shell
6. Run the app: python manage.py runserver
7. Then create a superuser: python manage.py createsuperuser
8. Then go to Django admin- http://localhost:8000/admin/ and create some patients,doctors, admins and appointments to test the API.


## Endpoints
### 1. Doctor:
- api/doctor/registration/
- api/doctor/login/
- api/doctor/profile/
- api/doctor/appointments/

### 2. Patient:
- api/patient/registration/
- api/patient/login/
- api/patient/profile/
- /api/patient/history/

### 2. Admin:
- api/admin/login/
- api/admin/approve/doctors/
- api/admin/approve/doctor/:uuid/
- api/admin/approve/patients/
- api/admin/patient/:uuid/
- api/admin/doctor/registration/
- api/admin/doctors/
- api/admin/doctor/:uuid/
- api/admin/patient/registration/
- api/admin/patients/
- api/admin/patient/:uuid/
- api/admin/patient/:uuid/history/
- api/admin/patient/:uuid/history/:id/
- api/admin/appointments/
- api/admin/appointment/:id/





