from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Profile
from .serializers import UserSerializer, ProfileSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []  # No authentication required

from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserProfileSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

