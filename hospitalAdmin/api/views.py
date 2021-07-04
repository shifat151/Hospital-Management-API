from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from patient.models import patient, patient_history
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group
from patient.models import Appointment
from account.models import User
from . serilizers import (doctorAccountSerializerAdmin,
    doctorRegistrationSerializerAdmin,
    doctorRegistrationProfileSerializerAdmin)
from doctor.models import doctor





class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name='admin').exists())


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        account_approval = user.groups.filter(name='admin').exists()
        if account_approval==False:
            return Response(
                {
                    'message': "You are not authorised to login as an admin"
                },
                status=status.HTTP_403_FORBIDDEN
            )
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key
        },status=status.HTTP_200_OK)

#Doctor Registration view for admin
class docregistrationViewAdmin(APIView):
    permission_classes = [IsAdmin]

    def post(self, request, format=None):
        registrationSerializer =  doctorRegistrationSerializerAdmin(
            data=request.data.get('user_data'))
        profileSerializer = doctorRegistrationProfileSerializerAdmin(
            data=request.data.get('profile_data'))
        checkregistration = registrationSerializer.is_valid()
        checkprofile = profileSerializer.is_valid()
        if checkregistration and checkprofile:
            doctor = registrationSerializer.save()
            profileSerializer.save(user=doctor)
            return Response({
                'user_data': registrationSerializer.data,
                'profile_data': profileSerializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'user_data': registrationSerializer.errors,
                'profile_data': profileSerializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

#Doctor profile view for admin
class doctorAccountViewAdmin(APIView):
    permission_classes = [IsAdmin]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request,pk=None, format=None):
        
        if pk:
            doctor_detail=self.get_object(pk)
            serializer=doctorAccountSerializerAdmin(doctor_detail)
            return Response({'doctors':serializer.data}, status=status.HTTP_200_OK)
        all_doctor=User.objects.filter(groups=1)
        serializer=doctorAccountSerializerAdmin(all_doctor, many=True)
        return Response({'doctors':serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        saved_user=self.get_object(pk)
        serializer=doctorAccountSerializerAdmin(instance=saved_user,data=request.data.get('doctors'), partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'doctors':serializer.data}, status=status.HTTP_200_OK)
        return Response({
                'doctors':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        saved_user=self.get_object(pk)
        saved_user.delete()
        return Response({"message": "User with id `{}` has been deleted.".format(pk)},status=status.HTTP_204_NO_CONTENT)













