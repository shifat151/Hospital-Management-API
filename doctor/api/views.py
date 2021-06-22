from rest_framework.views import APIView
from .serializers import doctorRegistrationSerializer, doctorProfileSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from doctor.models import doctor

class registrationView(APIView):
    permission_classes=[]

    # def get(self, request):
    #     try:
    #         user=request.user
    #     except user.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     profile=doctor.objects.filter(user=user)
    #     registrationSerializer = doctorRegistrationSerializer(user)
    #     profileSerializer=doctorProfileSerializer(profile)
    #     return Response({
    #             'registration':registrationSerializer.data,
    #             'profile':profileSerializer.data
    #     })
        

    
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
    


    