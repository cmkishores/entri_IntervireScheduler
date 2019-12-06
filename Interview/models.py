from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class InterviewSchedule(models.Model):

    class Meta:
        verbose_name = "Schedule"
    

    interview_date = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)



