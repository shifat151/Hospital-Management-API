
from rest_framework.exceptions import ValidationError
from patient.models import Appointment
from rest_framework import serializers
from account.models import User
from doctor.models import doctor
from django.contrib.auth.models import Group


class doctorAccountSerializerAdmin(serializers.Serializer):
    username=serializers.CharField(label='Username:', read_only=True)
    first_name=serializers.CharField(label='First name:')
    last_name=serializers.CharField(label='Last name:', required=False)


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
    user=doctorAccountSerializerAdmin()


    def validate_mobile(self, mobile):
        if mobile.isdigit()==False:
            raise serializers.ValidationError('Please Enter a valid mobile number!')
        return mobile
    
    
    def update(self, instance, validated_data):
        try:
            user_data=validated_data.pop('user')
        except:
            raise serializers.ValidationError('Please enter data related to user')

        user=instance.user

        instance.department=validated_data.get('department', instance.department)
        instance.address=validated_data.get('address', instance.address)
        instance.mobile=validated_data.get('mobile', instance.mobile)
        instance.save()

        user.first_name=user_data.get('first_name', user.first_name)
        user.last_name=user_data.get('last_name', user.last_name)
        user.save

        return instance