from calendar import c

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('recruiter', 'Recruiter'),
    )

    phone = models.CharField(max_length=15, unique=True)
    profile_image = models.ImageField(upload_to = 'profile/', null = True, blank = True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,)


class RecruiterProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_website = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"RecruiterProfile: {self.user.username}"

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    skills = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"JobSeekerProfile: {self.user.username}"