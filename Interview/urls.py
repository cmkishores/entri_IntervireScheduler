from django.urls import path
from .views import InterviewScheduleView,SchedulerView

urlpatterns = [
		path('submit/', InterviewScheduleView.as_view(),name='submit'),
		path('schedule/', SchedulerView.as_view(),name='schedule'),

	]