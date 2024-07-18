from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile_images', blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Lesons(models.Model):
    title = models.CharField(max_length=200)
    src = models.FileField(upload_to='lesons/audio/')
    img = models.ImageField(upload_to='lesons/images/')

    def __str__(self):
        return self.title


class CourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.IntegerField()  # Adjust based on your course identification logic
    current_lesson = models.IntegerField(default=0)
    progress = models.FloatField(default=0.0)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name            
    

    