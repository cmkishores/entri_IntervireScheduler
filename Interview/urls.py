from django.urls import path
from .views import InterviewScheduleView

urlpatterns = [
		path('submit/', InterviewScheduleView.as_view(),name='submit'),
	]