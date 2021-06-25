from rest_framework.views import APIView
from .serializers import doctorRegistrationSerializer, doctorProfileSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from doctor.models import doctor
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class registrationView(APIView):
    permission_classes = []

    def post(self, request, format=None):
        registrationSerializer = doctorRegistrationSerializer(
            data=request.data.get('user_data'))
        profileSerializer = doctorProfileSerializer(
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


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        account_approval = doctor.objects.filter(user=user, status=False)
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


class doctorProfileView(APIView):

    def get(self, request, format=None):
        try:
            user = request.user
        except user.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        profile = doctor.objects.filter(user=user).get()
        userSerializer=doctorRegistrationSerializer(user)
        profileSerializer = doctorProfileSerializer(profile)
        return Response({
            'user_data':userSerializer.data,
            'profile_data':profileSerializer.data

        }, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        try:
            user = request.user
        except user.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        profile = doctor.objects.filter(user=user).get()
        profileSerializer = doctorProfileSerializer(
            instance=profile, data=request.data.get('profile_data'), partial=True)
        if profileSerializer.is_valid():
            profileSerializer.save()
            return Response({
                'profile_data':profileSerializer.data
            }, status=status.HTTP_200_OK)
        return Response({
                'profile_data':profileSerializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
