
from rest_framework.exceptions import ValidationError
from patient.models import (Appointment,patient_history)
from rest_framework import serializers
from account.models import User
from doctor.models import doctor
from django.contrib.auth.models import Group

class doctorRegistrationSerializerAdmin(serializers.Serializer):

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
                status=True,
            )
        user.set_password(validated_data['password'])
        user.save()
        group_doctor, created = Group.objects.get_or_create(name='doctor')
        group_doctor.user_set.add(user)
        return user

class doctorRegistrationProfileSerializerAdmin(serializers.Serializer):
    Cardiologist='CL'
    Dermatologists='DL'
    Emergency_Medicine_Specialists='EMC'
    Immunologists='IL'
    Anesthesiologists='AL'
    Colon_and_Rectal_Surgeons='CRS'
    department=serializers.ChoiceField(label='Department:', choices=[(Cardiologist,'Cardiologist'),
        (Dermatologists,'Dermatologists'),
        (Emergency_Medicine_Specialists,'Emergency Medicine Specialists'),
        (Immunologists,'Immunologists'),
        (Anesthesiologists,'Anesthesiologists'),
        (Colon_and_Rectal_Surgeons,'Colon and Rectal Surgeons')
    ])
    address= serializers.CharField(label="Address:")
    mobile=serializers.CharField(label="Mobile Number:", max_length=20)


    def validate_mobile(self, mobile):
        if mobile.isdigit()==False:
            raise serializers.ValidationError('Please Enter a valid mobile number!')
        return mobile
    
    def create(self, validated_data):
        new_doctor= doctor.objects.create(
            department=validated_data['department'],
            address=validated_data['address'],
            mobile=validated_data['mobile'],
            user=validated_data['user']
        )
        return new_doctor


class doctorProfileSerializerAdmin(serializers.Serializer):
    Cardiologist='CL'
    Dermatologists='DL'
    Emergency_Medicine_Specialists='EMC'
    Immunologists='IL'
    Anesthesiologists='AL'
    Colon_and_Rectal_Surgeons='CRS'
    id=serializers.IntegerField(read_only=True)
    department=serializers.ChoiceField(label='Department:', choices=[(Cardiologist,'Cardiologist'),
        (Dermatologists,'Dermatologists'),
        (Emergency_Medicine_Specialists,'Emergency Medicine Specialists'),
        (Immunologists,'Immunologists'),
        (Anesthesiologists,'Anesthesiologists'),
        (Colon_and_Rectal_Surgeons,'Colon and Rectal Surgeons')
    ])
    address= serializers.CharField(label="Address:")
    mobile=serializers.CharField(label="Mobile Number:", max_length=20)


    def validate_mobile(self, mobile):
        if mobile.isdigit()==False:
            raise serializers.ValidationError('Please Enter a valid mobile number!')
        return mobile
    
    
    


class doctorAccountSerializerAdmin(serializers.Serializer):
    id=serializers.UUIDField(read_only=True)
    username=serializers.CharField(label='Username:', read_only=True)
    first_name=serializers.CharField(label='First name:')
    last_name=serializers.CharField(label='Last name:', required=False)
    status=serializers.BooleanField(label='status')
    doctor=doctorProfileSerializerAdmin(label='User')


    def update(self, instance, validated_data):
        try:
            doctor_profile=validated_data.pop('doctor')
        except:
            raise serializers.ValidationError("Please enter data related to doctor's profile")

        profile_data=instance.doctor

        instance.first_name=validated_data.get('department', instance.first_name)
        instance.last_name=validated_data.get('address', instance.last_name)
        instance.status=validated_data.get('status', instance.status)
        instance.save()

        profile_data.department=doctor_profile.get('department', profile_data.department)
        profile_data.address=doctor_profile.get('address', profile_data.address)
        profile_data.mobile=doctor_profile.get('mobile', profile_data.mobile)
        profile_data.save()

        return instance


class appointmentSerializerAdmin(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    appointment_date = serializers.DateField(label='Appointment date')
    appointment_time = serializers.TimeField(label='Appointement time')
    status = serializers.BooleanField(required=False)
    patient_history = serializers.PrimaryKeyRelatedField(queryset=patient_history.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=doctor.objects.all(), required=False)


    def create(self, validated_data):
        new_appointment= Appointment.objects.create(
            appointment_date=validated_data['appointment_date'],
            appointment_time=validated_data['appointment_time'],
            status=True,
            patient_history=validated_data['patient_history'],
            doctor=validated_data['doctor']
        )
        return new_appointment
    

    def update(self, instance, validated_data):
 

        instance.appointment_date=validated_data.get(' appointment_date', instance.appointment_date)
        instance.appointment_time=validated_data.get('appointment_time', instance.appointment_time)
        instance.status=validated_data.get('status', instance.status)
        instance.patient_history=validated_data.get('patient_history', instance.patient_history)
        instance.doctor=validated_data.get('doctor', instance.doctor)
        instance.save()


        return instance
