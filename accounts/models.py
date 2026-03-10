from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('job_seeker', 'Job Seeker'),
        ('recruiter', 'Recruiter'),
    )

    phone = models.CharField(max_length=15, unique=True)
    profile_image = models.ImageField(upload_to='profile/', null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='job_seeker')

    def __str__(self):
        return self.username