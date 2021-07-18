from django.db.models import fields
from django.db.models.query import QuerySet
from rest_framework import serializers
from account.models import User
from patient.models import patient, patient_history, Appointment
from django.contrib.auth.models import Group
from doctor.models import doctor



class patientRegistrationSerializer(serializers.Serializer):

    username=serializers.CharField(label='Username:')
    first_name=serializers.CharField(label='First name:')
    last_name=serializers.CharField(label='Last name:', required=False)
    password = serializers.CharField(label='Password:',style={'input_type': 'password'}, write_only=True,min_length=8,
    help_text="Your password must contain at least 8 characters and should not be entirely numeric."
    )
    password2=serializers.CharField(label='Confirm password:',style={'input_type': 'password'},  write_only=True)
    

    
    def validate_username(self, username):
        username_exists=User.objects.filter(username__iexact=username)
        if username_exists:
            raise serializers.ValidationError({'username':'This username already exists'})
        return username

        
    def validate_password(self, password):
        if password.isdigit():
            raise serializers.ValidationError('Your password should contain letters!')
        return password  

 

    def validate(self, data):
        password=data.get('password')
        password2=data.pop('password2')
        if password != password2:
            raise serializers.ValidationError({'password':'password must match'})
        return data


    def create(self, validated_data):
        user= User.objects.create(
                username=validated_data['username'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                status=False
            )
        user.set_password(validated_data['password'])
        user.save()
        group_patient, created = Group.objects.get_or_create(name='patient')
        group_patient.user_set.add(user)
        return user


class patientProfileSerializer(serializers.Serializer):
    age=serializers.DecimalField(label="Age:", max_digits=4,decimal_places=1)
    address= serializers.CharField(label="Address:")
    mobile=serializers.CharField(label="Mobile Number:", max_length=20)


    def validate_mobile(self, mobile):
        if mobile.isdigit()==False:
            raise serializers.ValidationError('Please Enter a valid mobile number!')
        return mobile
    
    def create(self, validated_data):
        new_patient= patient.objects.create(
            age=validated_data['age'],
            address=validated_data['address'],
            mobile=validated_data['mobile'],
            user=validated_data['user']
        )
        return new_patient
    
    def update(self, instance, validated_data):
        instance.age=validated_data.get('age', instance.age)
        instance.address=validated_data.get('address', instance.address)
        instance.mobile=validated_data.get('mobile', instance.mobile)
        instance.save()
        return instance


class patientCostSerializer(serializers.Serializer):
    room_charge=serializers.IntegerField(label="Room Charge:")
    medicine_cost=serializers.IntegerField(label="Medicine Cost:")
    doctor_fee=serializers.IntegerField(label="Doctor Fee:")
    other_charge=serializers.IntegerField(label="Other Charge:")
    total_cost=serializers.CharField(label="Total Cost:")


class appointmentSerializerPatient(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    appointment_date = serializers.DateField(label='Appointment date')
    appointment_time = serializers.TimeField(label='Appointement time')
    status = serializers.BooleanField(required=False, read_only=True)
    doctor = serializers.PrimaryKeyRelatedField(queryset=doctor.objects.all(), required=False)


    def create(self, validated_data):
        new_appointment= Appointment.objects.create(
            appointment_date=validated_data['appointment_date'],
            appointment_time=validated_data['appointment_time'],
            status=False,
            patient_history=validated_data['patient_history'],
            doctor=validated_data['doctor']
        )
        return new_appointment



class patientHistorySerializer(serializers.Serializer):
    Cardiologist='CL'
    Dermatologists='DL'
    Emergency_Medicine_Specialists='EMC'
    Immunologists='IL'
    Anesthesiologists='AL'
    Colon_and_Rectal_Surgeons='CRS'
    admit_date=serializers.DateField(label="Admit Date:", read_only=True)
    symptomps=serializers.CharField(label="Symptomps:", style={'base_template': 'textarea.html'})
    department=serializers.ChoiceField(label='Department: ', choices=[(Cardiologist,'Cardiologist'),
        (Dermatologists,'Dermatologists'),
        (Emergency_Medicine_Specialists,'Emergency Medicine Specialists'),
        (Immunologists,'Immunologists'),
        (Anesthesiologists,'Anesthesiologists'),
        (Colon_and_Rectal_Surgeons,'Colon and Rectal Surgeons')
    ])
    #required=False; if this field is not required to be present during deserialization.
    release_date=serializers.DateField(label="Release Date:", required=False)
    assigned_doctor=serializers.StringRelatedField(label='Assigned Doctor:')
    patient_appointments=appointmentSerializerPatient(label="Appointments",many=True)
    costs=patientCostSerializer()



    


    


    