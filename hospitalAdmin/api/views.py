from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from patient.models import (patient,
                            patient_history,
                            Appointment)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group
from patient.models import Appointment
from account.models import User
from . serializers import (doctorAccountSerializerAdmin,
                           doctorRegistrationSerializerAdmin,
                           doctorRegistrationProfileSerializerAdmin,
                           appointmentSerializerAdmin)
from doctor.models import doctor



class IsAdmin(BasePermission):
    """custom Permission class for Admin"""

    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name='admin').exists())


#Custom Auth token for Admin
class CustomAuthToken(ObtainAuthToken):

    """This class returns custom Authentication token only for admin"""

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        account_approval = user.groups.filter(name='admin').exists()
        if account_approval == False:
            return Response(
                {
                    'message': "You are not authorised to login as an admin"
                },
                status=status.HTTP_403_FORBIDDEN
            )
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key
        }, status=status.HTTP_200_OK)



class docregistrationViewAdmin(APIView):

    """API endpoint for creating doctors account- only accessible by Admin"""


    permission_classes = [IsAdmin]

    def post(self, request, format=None):
        registrationSerializer = doctorRegistrationSerializerAdmin(
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



class doctorAccountViewAdmin(APIView):

    """API endpoint for getiing info of all/particular doctor,
     update/delete doctor's info
     - only accessible by Admin"""

    permission_classes = [IsAdmin]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):

        if pk:
            doctor_detail = self.get_object(pk)
            serializer = doctorAccountSerializerAdmin(doctor_detail)
            return Response({'doctors': serializer.data}, status=status.HTTP_200_OK)
        all_doctor = User.objects.filter(groups=1, status=True)
        serializer = doctorAccountSerializerAdmin(all_doctor, many=True)
        return Response({'doctors': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        saved_user = self.get_object(pk)
        serializer = doctorAccountSerializerAdmin(
            instance=saved_user, data=request.data.get('doctors'), partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'doctors': serializer.data}, status=status.HTTP_200_OK)
        return Response({
            'doctors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        saved_user = self.get_object(pk)
        saved_user.delete()
        return Response({"message": "User with id `{}` has been deleted.".format(pk)}, status=status.HTTP_204_NO_CONTENT)


class approveDoctorViewAdmin(APIView):
    """API endpoint for getiing new doctor approval request, update approval  request.
     - only accessible by Admin"""

    permission_classes = [IsAdmin]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):

        if pk:
            doctor_detail = self.get_object(pk)
            serializer = doctorAccountSerializerAdmin(doctor_detail)
            return Response({'doctors': serializer.data}, status=status.HTTP_200_OK)
        all_doctor = User.objects.filter(groups=1, status=False)
        serializer = doctorAccountSerializerAdmin(all_doctor, many=True)
        return Response({'doctors': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        saved_user = self.get_object(pk)
        serializer = doctorAccountSerializerAdmin(
            instance=saved_user, data=request.data.get('doctors'), partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'doctors': serializer.data}, status=status.HTTP_200_OK)
        return Response({
            'doctors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        saved_user = self.get_object(pk)
        saved_user.delete()
        return Response({"message": "Doctor approval request with id `{}` has been deleted.".format(pk)}, status=status.HTTP_204_NO_CONTENT)



class appointmentmentViewAdmin(APIView):

    """API endpoint for getiing info of all/particular appointment,
     update/delete appointment - only accessible by Admin"""

    permission_classes = [IsAdmin]

    def get_object(self, pk):
        try:
            return Appointment.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):

        if pk:
            appointment_detail = self.get_object(pk)
            serializer = appointmentSerializerAdmin(appointment_detail)
            return Response({'appointments': serializer.data}, status=status.HTTP_200_OK)
        all_appointment = Appointment.objects.all()
        serializer = appointmentSerializerAdmin(all_appointment, many=True)
        return Response({'appointments': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = appointmentSerializerAdmin(
            data=request.data.get('appointments'))
        if serializer.is_valid():
            serializer.save()
            return Response({
                'appointments': serializer.data,
            }, status=status.HTTP_201_CREATED)
        return Response({
            'appointments': serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        saved_appointment= self.get_object(pk)
        serializer = appointmentSerializerAdmin(
            instance=saved_appointment, data=request.data.get('appointments'), partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'appointments': serializer.data}, status=status.HTTP_200_OK)
        return Response({
            'appointments': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)    

    def delete(self, request, pk):
        saved_appointment= self.get_object(pk)
        saved_appointment.delete()
        return Response({"message": "Appointment with id `{}` has been deleted.".format(pk)}, status=status.HTTP_204_NO_CONTENT)



class approveAppointmentViewAdmin(APIView):
    def get_object(self, pk):
        try:
            return Appointment.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk=None, format=None):

        if pk:
            appointment_detail = self.get_object(pk)
            serializer = appointmentSerializerAdmin(appointment_detail)
            return Response({'appointments': serializer.data}, status=status.HTTP_200_OK)
        all_appointment = Appointment.objects.filter(status=False)
        serializer = appointmentSerializerAdmin(all_appointment, many=True)
        return Response({'appointments': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
            saved_appointment= self.get_object(pk)
            serializer = appointmentSerializerAdmin(
                instance=saved_appointment, data=request.data.get('appointments'), partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'appointments': serializer.data}, status=status.HTTP_200_OK)
            return Response({
                'appointments': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        saved_appointment= self.get_object(pk)
        saved_appointment.delete()
        return Response({"message": "Appointment with id `{}` has been deleted.".format(pk)}, status=status.HTTP_204_NO_CONTENT)

