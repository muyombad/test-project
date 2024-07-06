from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserProfileSerializer

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

