from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    CHOICES = [
        ('candidate', 'Candidate'),
        ('interviewer', 'Interviewer'),
        ('hr','HR Manager'),
    ]
