from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class InterviewSchedule(models.Model):

    class Meta:
        verbose_name = "Schedule"
    

    interview_date = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

