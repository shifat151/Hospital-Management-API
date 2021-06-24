from rest_framework.views import APIView
from .serializers import doctorRegistrationSerializer, doctorProfileSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from doctor.models import doctor
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class registrationView(APIView):
    permission_classes=[]

    def post(self, request, format=None):
        registrationSerializer = doctorRegistrationSerializer(data=request.data.get('registration'))
        profileSerializer=doctorProfileSerializer(data=request.data.get('profile'))
        checkregistration=registrationSerializer.is_valid()
        checkprofile=profileSerializer.is_valid()
        if checkregistration and checkprofile:
            doctor=registrationSerializer.save()
            print(doctor.id)
            profileSerializer.save(user=doctor)
            return Response({
                'registration':registrationSerializer.data,
                'profile':profileSerializer.data
             }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                    'registration':registrationSerializer.errors,
                    'profile':profileSerializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
    

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        account_approval=doctor.objects.filter(user=user, status=False)
        if account_approval:
            return Response({
                'status':"Your account is not approved by admin yet!"
            })
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key
        })



# class doctorProfileView(APIView):


#     def get(self, request, format=None):
#         try:
#             user=request.user
#         except user.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         profile=doctor.objects.filter(user=user)
#         profileSerializer=doctorProfileSerializer(profile)
#         return Response({
#                 'profile':profileSerializer.data
#         })

    # def put(self, request, format=None):

        


