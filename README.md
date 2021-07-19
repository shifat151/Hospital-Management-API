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
- api/patient/history/
- api/patient/appointment/

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
- api/admin/approve/appointments/
- api/admin/approve/appointments/:id/


## Sample API Request and Response

**POST api/doctor/registration/**

Details: API endpoint for creating new doctor account.

request body:
```json
{
    "user_data": {
        "username": "doctor5",
        "first_name": "Dr. Deal",
        "last_name": "Walker",
        "password":"doctoraccess1234",
        "password2":"doctoraccess1234"
    },
    "profile_data": {
        "department": "CL",
        "address": "Dortmund",
        "mobile": "12312343424"
    }
}
```
response body:
```json
{
    "user_data": {
        "username": "doctor5",
        "first_name": "Dr. Deal",
        "last_name": "Walker"
    },
    "profile_data": {
        "department": "CL",
        "address": "Dortmund",
        "mobile": "12312343424"
    }
}
```



**POST api/doctor/login/**

Details: API endpoint for doctor login. Admin needs to approve account otherwise login will not be successful.

request body:
```json
{
    "username": "doctor7",
    "password": "doctoraccess1234"
}
```
response body:
```json
{
    "token": "e617d20f74709f1d2098076696e026f602cef5b9"
}
```
**GET api/doctor/profile/**

Details: API endpoint for getting doctor profile details. Token authentication required

response body:

```json
{
    "user_data": {
        "username": "doctor7",
        "first_name": "doctor7",
        "last_name": "seven"
    },
    "profile_data": {
        "department": "CL",
        "address": "Rajshahi",
        "mobile": "9999"
    }
}
```

**PUT api/doctor/profile/**

Details: API endpoint for updating doctor profile . Token authentication required

request:
```json
{
    "profile_data": {
        "department": "CL",
        "address": "Dhaka",
        "mobile": "9999"
    }
}
```
response:
```json
{
    "profile_data": {
        "department": "CL",
        "address": "Dhaka",
        "mobile": "9999"
    }
}
```

**GET api/doctor/appointments/**

Details: API endpoint for getting details of all appointments .Appointment need to be approved by admin. Token authentication required

response:
```json
[
    {
        "patient_name": "patient one",
        "patient_age": 25.5,
        "appointment_date": "2021-07-07",
        "appointment_time": "09:33:38",
        "patient_history": {
            "admit_date": "2021-07-06",
            "symptomps": "Pain",
            "department": "CL",
            "release_date": null,
            "assigned_doctor": "doctor7 (CL)"
        }
    }
]
```

------------


**POST api/patient/registration/**

Details: API endpoint for creating new patient account.

request:
```json
{
    "user_data": {
        "username": "patient2",
        "first_name": "patien2",
        "last_name": "two",
        "password":"patientaccess1234",
        "password2":"patientaccess1234"
    },
    "profile_data": {
        "age": "29",
        "address": "Dhaka",
        "mobile": "12312343424"
    }
}
```
response:
```json
{
    "user_data": {
        "username": "patient2",
        "first_name": "patien2",
        "last_name": "two"
    },
    "profile_data": {
        "age": "29.0",
        "address": "Dhaka",
        "mobile": "12312343424"
    }
}
```

**POST api/patient/login/**

Details: API endpoint for patient login. Account needs be approved by admin first.

request:
```json
{
    "username": "patient2",
    "password": "patientaccess1234"
}
```

```json
{
    "token": "eba9f0c858e84c11a5468545e1f0256d0ef4cf0c"
}
```

**GET api/patient/profile/**

Details: API endpoint for getting details of patient profile.Token authentication required.

response:
```json
{
    "user_data": {
        "username": "patient2",
        "first_name": "patien2",
        "last_name": "two"
    },
    "profile_data": {
        "age": "29.0",
        "address": "Dhaka",
        "mobile": "12312343424"
    }
}
```
**PUT api/patient/profile/**

Details: API endpoint for updating details of a patient profile.Token authentication required.

request:
```json
{
    "profile_data": {
        "age": "29.0",
        "address": "Dhaka",
        "mobile": "12312343"
    }
}
```

response:
```json
{
    "profile_data": {
        "age": "29.0",
        "address": "Dhaka",
        "mobile": "12312343"
    }
}
```

**GET api/patient/history/**

Details: API endpoint for all history of a patient .Token authentication required.

response:
```json
[
    {
        "admit_date": "2021-07-07",
        "symptomps": "Pain.cough",
        "department": "CL",
        "release_date": null,
        "assigned_doctor": "doctor3 (CL)",
        "patient_appointments": [],
        "costs": {
            "room_charge": 3000,
            "medicine_cost": 250,
            "doctor_fee": 1250,
            "other_charge": 60,
            "total_cost": "4560 tk"
        }
    }
]
```
**GET api/patient/appointment/**

Details: API endpoint for getting all latest approved appointments. Token authentication required.

response:
```json
[
    {
        "id": 14,
        "appointment_date": "2021-07-18",
        "appointment_time": "16:33:27",
        "status": true,
        "doctor": 5
    },
    {
        "id": 16,
        "appointment_date": "2021-07-18",
        "appointment_time": "16:33:27",
        "status": true,
        "doctor": 5
    }
]
```

**POST api/patient/appointment/**

Details: API endpoint for creating an appointment request. Token authentication required.

request:
```json
{
        "appointment_date": "2021-07-18",
        "appointment_time": "16:33:27",
        "doctor": 5
}
```

response:
```json
{
    "id": 18,
    "appointment_date": "2021-07-18",
    "appointment_time": "16:33:27",
    "status": false,
    "doctor": 5
}
```

------------


**POST api/admin/login/**

Details: API endpoint for  Admin login.

request:
```json
{
    "username": "admin1",
    "password": "access1234"
    
}
```
response:
```json
{
    "token": "f83f8c6ecf406aa1b5cec105355a6638661f5879"
}
```

**GET api/admin/approve/doctors/**

Details: API endpoint for  Getting approval requests of new doctors.Token authentication required.

Response:
```json
{
    "doctors": [
        {
            "id": "d6e19da5-92f8-45e3-ad26-63fa39f8e90f",
            "username": "doctor3",
            "first_name": "doctor3",
            "last_name": "three",
            "status": false,
            "doctor": {
                "id": 4,
                "department": "CL",
                "address": "Rajshahi",
                "mobile": "12312343424"
            }
        },
        {
            "id": "2ad1ebd7-b1fe-49b9-ad5a-b4eb583ececa",
            "username": "doctor4",
            "first_name": "doctor4",
            "last_name": "four",
            "status": false,
            "doctor": {
                "id": 5,
                "department": "CL",
                "address": "Kusthia",
                "mobile": "12312343424"
            }
        },
        {
            "id": "10745a74-bc69-4eea-b975-228f6ca6297a",
            "username": "doctor1",
            "first_name": "doctor1",
            "last_name": "one",
            "status": false,
            "doctor": {
                "id": 7,
                "department": "CL",
                "address": "Rangpur",
                "mobile": "12312343424"
            }
        }
    ]
}
```

**GET api/admin/approve/doctor/:uuid/**

Details: API endpoint for  Getting detail approval requests of a new doctor.Token authentication required.

response:
```json
{
    "doctors": {
        "id": "d6e19da5-92f8-45e3-ad26-63fa39f8e90f",
        "username": "doctor3",
        "first_name": "doctor3",
        "last_name": "three",
        "status": false,
        "doctor": {
            "id": 4,
            "department": "CL",
            "address": "Rajshahi",
            "mobile": "12312343424"
        }
    }
}
```

**PUT api/admin/approve/doctor/:uuid/**

Details: API endpoint for  updating approval requests of a new doctor.Token authentication required.

request:
```json
{
    "doctors": {
        "id": "d6e19da5-92f8-45e3-ad26-63fa39f8e90f",
        "username": "doctor3",
        "first_name": "doctor3",
        "last_name": "three",
        "status": true,
        "doctor": {
            "id": 4,
            "department": "CL",
            "address": "Rajshahi",
            "mobile": "12312343424"
        }
    }
}
```

response:
```json
{
    "doctors": {
        "id": "d6e19da5-92f8-45e3-ad26-63fa39f8e90f",
        "username": "doctor3",
        "first_name": "doctor3",
        "last_name": "three",
        "status": true,
        "doctor": {
            "id": 4,
            "department": "CL",
            "address": "Rajshahi",
            "mobile": "12312343424"
        }
    }
}
```
**DELETE api/admin/approve/doctor/:uuid/**

Details: API endpoint for  deleting approval requests of doctor.Token authentication required.

response:
```json
{
    "message": "Doctor approval request with id `d6e19da5-92f8-45e3-ad26-63fa39f8e90f` has been deleted."
}
```

**GET api/admin/approve/patients/**

Details: API endpoint for getting all patient approval request.Token authentication required.

response:
```json
{
    "patients": [
        {
            "id": "5b6926d3-fd27-4e25-a989-6e5043788567",
            "username": "patient10",
            "first_name": "Patient new",
            "last_name": "",
            "status": false,
            "patient": {
                "age": "45.0",
                "address": "New iskaton",
                "mobile": "342423423"
            }
        }
    ]
}
```

**GET api/admin/patient/:uuid/**

Details: API endpoint for getting detail of a patient approval request.Token authentication required.

response:
```json
{
    "patients": {
        "id": "5b6926d3-fd27-4e25-a989-6e5043788567",
        "username": "patient10",
        "first_name": "Patient new",
        "last_name": "",
        "status": false,
        "patient": {
            "age": "45.0",
            "address": "New iskaton",
            "mobile": "342423423"
        }
    }
}
```

**PUT api/admin/patient/:uuid/**

Details: API endpoint for updating detail of a patient approval request.Token authentication required.

request:
```json
{
    "patients": {
        "id": "5b6926d3-fd27-4e25-a989-6e5043788567",
        "username": "patient10",
        "first_name": "Patient new",
        "status": true,
        "patient": {
            "age": "45.0",
            "address": "New iskaton",
            "mobile": "342423423"
        }
    }
}
```

response:
```json
{
    "patients": {
        "id": "5b6926d3-fd27-4e25-a989-6e5043788567",
        "username": "patient10",
        "first_name": "Patient new",
        "last_name": "",
        "status": true,
        "patient": {
            "age": "45.0",
            "address": "New iskaton",
            "mobile": "342423423"
        }
    }
}
```


**DELETE api/admin/patient/:uuid/**

Details: API endpoint for deleting a patient approval request.Token authentication required.

response:
```json
{
    "message": "User with id `5b6926d3-fd27-4e25-a989-6e5043788567` has been deleted."
}
```


**POST api/admin/doctor/registration/**

Details: API endpoint for creating a new doctor account.Token authentication required.

request:
```json
{
    "user_data": {
        "username": "doctor2",
        "first_name": "doctor2",
        "last_name": "two",
        "password":"doctoraccess1234",
        "password2":"doctoraccess1234"
    },
    "profile_data": {
        "department": "CL",
        "address": "Rangpur",
        "mobile": "12312343424"
    }
}
```

response:
```json
{
    "user_data": {
        "username": "doctor2",
        "first_name": "doctor2",
        "last_name": "two"
    },
    "profile_data": {
        "department": "CL",
        "address": "Rangpur",
        "mobile": "12312343424"
    }
}
```

**GET api/admin/doctors/**

Details: API endpoint for getting all doctors with details.Only approved list will be displayed. Token authentication required.

response:

```json
{
    "doctors": [
        {
            "id": "11523302-4827-4d11-888c-10d0d0d4936e",
            "username": "doctor7",
            "first_name": "doctor7",
            "last_name": "seven",
            "status": true,
            "doctor": {
                "id": 6,
                "department": "CL",
                "address": "Dhaka",
                "mobile": "9999"
            }
        },
        {
            "id": "fbbc8225-e7e9-4039-9ec6-5cf1726088f0",
            "username": "doctor5",
            "first_name": "Dr. Deal",
            "last_name": "Walker",
            "status": true,
            "doctor": {
                "id": 8,
                "department": "CL",
                "address": "Dortmund",
                "mobile": "12312343424"
            }
        },
        {
            "id": "e942f267-ed39-46a7-a010-5db53813e664",
            "username": "doctor2",
            "first_name": "doctor2",
            "last_name": "two",
            "status": true,
            "doctor": {
                "id": 9,
                "department": "CL",
                "address": "Rangpur",
                "mobile": "12312343424"
            }
        }
    ]
}
```



**GET api/admin/doctor/:uuid/**

Details: API endpoint for getting specific doctor's profile detail.Only approved doctor will be available. Token authentication required.

response:
```json
{
    "doctors": {
        "id": "e942f267-ed39-46a7-a010-5db53813e664",
        "username": "doctor2",
        "first_name": "doctor2",
        "last_name": "two",
        "status": true,
        "doctor": {
            "id": 9,
            "department": "CL",
            "address": "Rangpur",
            "mobile": "12312343424"
        }
    }
}
```

**GET api/admin/doctor/:uuid/**

Details: API endpoint for updating specific doctor's profile. Token authentication required.

request:
```json
{
    "doctors": {
        "username": "doctor1",
        "first_name": "doctor1",
        "last_name": "one",
        "status": true,
        "doctor": {
            "department": "CL",
            "address": "Rangpur",
            "mobile": "12312343424"
        }
    }
}
```

response:

```json
{
    "doctors": {
        "id": "10745a74-bc69-4eea-b975-228f6ca6297a",
        "username": "doctor1",
        "first_name": "doctor1",
        "last_name": "one",
        "status": true,
        "doctor": {
            "id": 7,
            "department": "CL",
            "address": "Rangpur",
            "mobile": "12312343424"
        }
    }
}
```


**DELETE api/admin/doctor/:uuid/**

Details: API endpoint for deleting a doctor's account. Token authentication required.

response:
```json
{
    "message": "User with id `10745a74-bc69-4eea-b975-228f6ca6297a` has been deleted."
}
```

**POST api/admin/patient/registration/**

Details: API endpoint for creating a  patient's account. Token authentication required.

request:
```json

{
    "user_data": {
        "username": "patient3",
        "first_name": "patient3",
        "last_name": "three",
        "password":"patientaccess1234",
        "password2":"patientaccess1234"
    },
    "profile_data": {
        "age": "45",
        "address": "Rangpur",
        "mobile": "12312343424"
    }
}
```
response:
```json

{
    "user_data": {
        "username": "patient3",
        "first_name": "patient3",
        "last_name": "three",
    },
    "profile_data": {
        "age": "45",
        "address": "Rangpur",
        "mobile": "12312343424"
    }
}
```

**GET api/admin/patients/**

Details: API endpoint for getting all the patients account.  only approved patient will be available.  Token authentication required.

 response:
 ```json
{
    "patients": [
        {
            "id": "94d9debf-6c3b-48bb-98f6-1c8f0fbeae04",
            "username": "patient1",
            "first_name": "patient",
            "last_name": "one",
            "status": true,
            "patient": {
                "age": "25.5",
                "address": "Rajshahi",
                "mobile": "9999"
            }
        },
        {
            "id": "e48c322c-1221-43eb-8148-b28031870028",
            "username": "patient2",
            "first_name": "patien2",
            "last_name": "two",
            "status": true,
            "patient": {
                "age": "29.0",
                "address": "Dhaka",
                "mobile": "12312343"
            }
        },
        {
            "id": "b7d4a896-47d1-499d-be9b-ff5015c599b0",
            "username": "patient3",
            "first_name": "patient3",
            "last_name": "three",
            "status": true,
            "patient": {
                "age": "45.0",
                "address": "Rangpur",
                "mobile": "12312343424"
            }
        },
        {
            "id": "0046a58a-c52f-46dc-8a5a-4f598ed48f8a",
            "username": "patient10",
            "first_name": "patient10",
            "last_name": "ten",
            "status": true,
            "patient": {
                "age": "45.0",
                "address": "Rangpur",
                "mobile": "12312343424"
            }
        }
    ]
}
```

**Get api/admin/patient/:uuid/**

Details: API endpoint for getting detail of a patient account.Token authentication required.

response:
```json
{
    "patients": {
        "id": "94d9debf-6c3b-48bb-98f6-1c8f0fbeae04",
        "username": "patient1",
        "first_name": "patient",
        "last_name": "one",
        "status": true,
        "patient": {
            "age": "25.5",
            "address": "Rajshahi",
            "mobile": "9999"
        }
    }
}
```

**PUT api/admin/patient/:uuid/**

Details: API endpoint for updatig detail of a patient account.Token authentication required.

request:
```json
{
    "patients": {
        "id": "94d9debf-6c3b-48bb-98f6-1c8f0fbeae04",
        "username": "patient1",
        "first_name": "patient",
        "last_name": "one",
        "status": true,
        "patient": {
            "age": "25.5",
            "address": "Rajshahi",
            "mobile": "9999"
        }
    }
}
```
response:

```json
{
    "patients": {
        "id": "94d9debf-6c3b-48bb-98f6-1c8f0fbeae04",
        "username": "patient1",
        "first_name": "patient",
        "last_name": "one",
        "status": true,
        "patient": {
            "age": "25.5",
            "address": "Dhaka",
            "mobile": "9999"
        }
    }
}
```
**DELETE api/admin/patient/:uuid/**

Details: API endpoint for updating detail of a patient account.Token authentication required.

response:
```json
{
    "message": "User with id `94d9debf-6c3b-48bb-98f6-1c8f0fbeae04` has been deleted."
}
```


**GET api/admin/patient/:uuid/history/**

Details: API endpoint for getting all histories for specific patient.Token authentication required.

response:
```json
{
    "patient_history": [
        {
            "id": 8,
            "admit_date": "2021-07-07",
            "symptomps": "Fever,cough",
            "department": "EMC",
            "release_date": null,
            "assigned_doctor": 5,
            "costs": {
                "room_charge": 4500,
                "medicine_cost": 1500,
                "doctor_fee": 500,
                "other_charge": 100,
                "total_cost": "6600 tk"
            }
        }
    ]
}
```

**GET api/admin/patient/:uuid/history/:id/**

Details: API endpoint for getting speicific history for specific patient.Token authentication required.

response:
```json
{
    "patient_history": {
        "id": 8,
        "admit_date": "2021-07-07",
        "symptomps": "Fever,cough",
        "department": "EMC",
        "release_date": null,
        "assigned_doctor": 5,
        "costs": {
            "room_charge": 4500,
            "medicine_cost": 1500,
            "doctor_fee": 500,
            "other_charge": 100,
            "total_cost": "6600 tk"
        }
    }
}
```
**PUT api/admin/patient/:uuid/history/:id/**

Details: API endpoint for updating history for specific patient.Token authentication required.

request:

```json
{
    "patient_history": {
        "id": 8,
        "admit_date": "2021-07-07",
        "symptomps": "Fever,cough,toncil",
        "department": "EMC",
        "assigned_doctor": 5,
        "costs": {
            "room_charge": 4500,
            "medicine_cost": 1500,
            "doctor_fee": 500,
            "other_charge": 100,
            "total_cost": "6600 tk"
        }
    }
}
```

response:
```json
{
    "patient_history": {
        "id": 8,
        "admit_date": "2021-07-07",
        "symptomps": "Fever,cough,toncil",
        "department": "EMC",
        "release_date": null,
        "assigned_doctor": 5,
        "costs": {
            "room_charge": 4500,
            "medicine_cost": 1500,
            "doctor_fee": 500,
            "other_charge": 100,
            "total_cost": "6600 tk"
        }
    }
}
```

**DELETE api/admin/patient/:uuid/history/:id/**

Delete: API endpoint for deleting a patient history. Token authentication required.

response:

```json
{
    "message": "History with id `8` has been deleted."
}
```

**POST api/admin/appointments/**

Details: API endpoint for creating an appointment. Token authentication required.

request:
```json
{
    "appointments": {
        "appointment_date": "2021-07-06",
        "appointment_time": "05:51:59",
        "patient_history": 9,
        "doctor": 9
    }
}
```

**GET api/admin/appointments/**

Details: API endpoint for getting all appointments. Token authentication required.

response:
```json
{
    "appointments": [
        {
            "id": 13,
            "appointment_date": "2021-07-06",
            "appointment_time": "05:51:59",
            "status": true,
            "patient_history": 9,
            "doctor": 9
        }
    ]
}
```
**GET api/admin/appointment/:id/**

Details: API endpoint for getting details of an appointment. Token authentication required.

response:
```json
{
    "appointments": {
        "id": 13,
        "appointment_date": "2021-07-06",
        "appointment_time": "05:51:59",
        "status": true,
        "patient_history": 9,
        "doctor": 9
    }
}
```
**PUT api/admin/appointment/:id/**

Details: API endpoint for updating detail of an appointment. Token authentication required.

request:
```json
{
    "appointments": {
        "appointment_date": "2021-08-06",
        "appointment_time": "05:02:59",
        "status": true,
        "patient_history": 9,
        "doctor": 9
    }
}
```
response:
```json
{
    "appointments": {
        "id": 13,
        "appointment_date": "2021-08-06",
        "appointment_time": "05:02:59",
        "status": true,
        "patient_history": 9,
        "doctor": 9
    }
}
```

**DELETE api/admin/appointment/:id/**

Details:API endpoint for deleting an appointment. Token authentication required.

response:
```json
{
    "message": "Appointment with id `13` has been deleted."
}
```


**GET api/admin/approve/appointments/**

Details: API endpoint for getting all appointment requests. Token authentication required.

response:
```json
{
    "appointments": [
        {
            "id": 15,
            "appointment_date": "2021-07-24",
            "appointment_time": "06:00:00",
            "status": false,
            "patient_history": 9,
            "doctor": 8
        },
        {
            "id": 17,
            "appointment_date": "2021-07-18",
            "appointment_time": "16:33:27",
            "status": false,
            "patient_history": 9,
            "doctor": 5
        },
        {
            "id": 18,
            "appointment_date": "2021-07-18",
            "appointment_time": "16:33:27",
            "status": false,
            "patient_history": 9,
            "doctor": 5
        }
    ]
}
```

**GET api/admin/approve/appointments/:id**

Details: API endpoint for getting an appointment detail request. Token authentication required.

response:
```json
{
    "appointments": {
        "id": 15,
        "appointment_date": "2021-07-24",
        "appointment_time": "06:00:00",
        "status": false,
        "patient_history": 9,
        "doctor": 8
    }
}
```

**PUT api/admin/approve/appointments/:id**

Details: API endpoint for updating an appointment request. Token authentication required.

request:
```json
{
    "appointments": {
        "appointment_date": "2021-07-24",
        "appointment_time": "06:00:00",
        "status": true,
        "patient_history": 9,
        "doctor": 8
    }
}
```

response:
```json
{
    "appointments": {
        "id": 15,
        "appointment_date": "2021-07-24",
        "appointment_time": "06:00:00",
        "status": true,
        "patient_history": 9,
        "doctor": 8
    }
}
```

**DELETE api/admin/appointment/:id/**

Details:API endpoint for deleting an appointment request. Token authentication required.

response:
```json
{
    "message": "Appointment with id `15` has been deleted."
}
```

