from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    index_number = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=100, default="Unnamed User")

    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'index_number']

class CompatibilityProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    music_choice = models.CharField(max_length=100)
    favorite_color = models.CharField(max_length=50)
    cleanliness = models.CharField(max_length=50)
    sleep_schedule = models.CharField(max_length=50)
    noise_level = models.CharField(max_length=50)
    study_preference = models.CharField(max_length=50)
    health_issues = models.TextField(blank=True, null=True)
    religion = models.CharField(max_length=100)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.full_name}'s compatibility profile"