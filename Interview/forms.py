from .models import InterviewSchedule
from django import forms

class DateInput(forms.DateTimeInput):
    input_type = 'date'


class TimeInput(forms.DateTimeInput):
    input_type = 'time'

class ScheduleAddForm(forms.ModelForm):
    class Meta:
        model = InterviewSchedule
        fields = ['interview_date', 'start_time', 'end_time']
        widgets = {
             'interview_date':DateInput(),
             'start_time':TimeInput(),
             'end_time':TimeInput(),
         }

class SearchScheduleForm(forms.Form):
    interviewer_id = forms.CharField(label= "Enter interviewer username", max_length=100)
    candidate_id = forms.CharField(label= "Enter candidate username", max_length=100)
