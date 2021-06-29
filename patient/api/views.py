from rest_framework.views import APIView
from .serializers import (patientRegistrationSerializer,
 patientProfileSerializer,
  patientHistorySerializer)

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from patient.models import patient, patient_history
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import BasePermission, IsAuthenticated

from patient.models import patient




class IsPatient(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name='patient').exists())
        

class registrationView(APIView):
    permission_classes = []

    def post(self, request, format=None):
        registrationSerializer = patientRegistrationSerializer(
            data=request.data.get('user_data'))
        profileSerializer = patientProfileSerializer(
            data=request.data.get('profile_data'))
        checkregistration = registrationSerializer.is_valid()
        checkprofile = profileSerializer.is_valid()
        if checkregistration and checkprofile:
            patient = registrationSerializer.save()
            profileSerializer.save(user=patient)
            return Response({
                'user_data': registrationSerializer.data,
                'profile_data': profileSerializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'user_data': registrationSerializer.errors,
                'profile_data': profileSerializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        account_approval = patient.objects.filter(user=user, status=False)
        if account_approval:
            return Response(
                {
                    'message': "Your account is not approved by admin yet!"
                },
                status=status.HTTP_403_FORBIDDEN
            )
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key
        },status=status.HTTP_200_OK)


class patientProfileView(APIView):
    permission_classes = [IsPatient]


    def get(self, request, format=None):
        user = request.user
        profile = patient.objects.filter(user=user).get()
        userSerializer=patientRegistrationSerializer(user)
        profileSerializer = patientProfileSerializer(profile)
        return Response({
            'user_data':userSerializer.data,
            'profile_data':profileSerializer.data

        }, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        user = request.user
        profile = patient.objects.filter(user=user).get()
        profileSerializer = patientProfileSerializer(
            instance=profile, data=request.data.get('profile_data'), partial=True)
        if profileSerializer.is_valid():
            profileSerializer.save()
            return Response({
                'profile_data':profileSerializer.data
            }, status=status.HTTP_200_OK)
        return Response({
                'profile_data':profileSerializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class patientHistoryView(APIView):

    def get(self, request, format=None):
        user = request.user
        print(user.username)
        user_patient = patient.objects.filter(user=user).get()
        history = patient_history.objects.filter(patient=user_patient)
        print('new history boys {}'.format(history))
        historySerializer=patientHistorySerializer(history, many=True)
        return Response(historySerializer.data, status=status.HTTP_200_OK)

