from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Lesons, CourseProgress, Contact

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_img', 'city', 'state', 'country', 'phone_number', 'zip_code', 'active']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        profile.profile_img = profile_data.get('profile_img', profile.profile_img)
        profile.city = profile_data.get('city', profile.city)
        profile.state = profile_data.get('state', profile.state)
        profile.country = profile_data.get('country', profile.country)
        profile.phone_number = profile_data.get('phone_number', profile.phone_number)
        profile.zip_code = profile_data.get('zip_code', profile.zip_code)
        profile.save()

        return instance
    



class UserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        # Update user fields
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        # Update profile fields
        profile.profile_img = profile_data.get('profile_img', profile.profile_img)
        profile.city = profile_data.get('city', profile.city)
        profile.state = profile_data.get('state', profile.state)
        profile.country = profile_data.get('country', profile.country)
        profile.phone_number = profile_data.get('phone_number', profile.phone_number)
        profile.zip_code = profile_data.get('zip_code', profile.zip_code)
        profile.save()

        return instance
    
class LesonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesons
        fields = ['id', 'title', 'src', 'img']    

class CourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseProgress
        fields = [ 'course_id', 'current_lesson', 'progress']  


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)             

