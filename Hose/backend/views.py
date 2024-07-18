from rest_framework import generics, permissions, status
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserProfileSerializer, LesonsSerializer, CourseProgressSerializer
from .models import Lesons, CourseProgress
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.conf import settings
from django.http import JsonResponse
from django.views import View
import json
import stripe

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []  # No authentication required



class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated] # authentication required

    def get_object(self):
        return self.request.user

class LesonsList(generics.ListAPIView):
    queryset = Lesons.objects.all()
    serializer_class = LesonsSerializer
    permission_classes = []  # No authentication required


class CourseProgressView(APIView):
    permission_classes =[permissions.IsAuthenticated]

    def get(self, request, format=None):
        progress = CourseProgress.objects.filter(user=request.user).first()
        if progress:
            serializer = CourseProgressSerializer(progress)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        progress = CourseProgress.objects.filter(user=request.user).first()
        if progress:
            serializer = CourseProgressSerializer(progress, data=request.data)
        else:
            serializer = CourseProgressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    
class UserIDView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return HttpResponse(request.user.id)


# views.py
# views.py

# myapp/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import ContactFormSerializer
from django.core.mail import send_mail

@api_view(['POST'])
@permission_classes([AllowAny])
def contact_form(request):
    serializer = ContactFormSerializer(data=request.data)
    if serializer.is_valid():
        

        # Send email
        subject = serializer.validated_data['subject']
        message = serializer.validated_data['message']
        from_email = serializer.validated_data['email']
        recipient_list = ['info@hoseconsultsugandaltd.com']  # Replace with your recipient email(s)

        try:
            send_mail(subject, message, from_email, recipient_list)
            return Response({'status': 'success', 'message': 'Your message has been sent.'})
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=500)

    return Response(serializer.errors, status=400)





