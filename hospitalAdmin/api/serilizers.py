
from rest_framework.exceptions import ValidationError
from patient.models import Appointment
from rest_framework import serializers
from account.models import User
from doctor.models import doctor
from django.contrib.auth.models import Group



class doctorProfileSerializerAdmin(serializers.Serializer):
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
    
    


class doctorAccountSerializerAdmin(serializers.Serializer):
    id=serializers.UUIDField(read_only=True)
    username=serializers.CharField(label='Username:', read_only=True)
    first_name=serializers.CharField(label='First name:')
    last_name=serializers.CharField(label='Last name:', required=False)
    doctor=doctorProfileSerializerAdmin(label='User')


    def update(self, instance, validated_data):
        try:
            doctor_profile=validated_data.pop('doctor')
        except:
            raise serializers.ValidationError("Please enter data related to doctor's profile")

        profile_data=instance.doctor

        instance.first_name=validated_data.get('department', instance.first_name)
        instance.last_name=validated_data.get('address', instance.last_name)
        instance.save()

        profile_data.department=doctor_profile.get('department', profile_data.department)
        profile_data.address=doctor_profile.get('address', profile_data.address)
        profile_data.mobile=doctor_profile.get('mobile', profile_data.mobile)
        profile_data.save()

        return instance


