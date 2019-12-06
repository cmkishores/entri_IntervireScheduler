from django.urls import path
from .views import InterviewScheduleView,SchedulerView,ResultView

urlpatterns = [
		path('submit/', InterviewScheduleView.as_view(),name='submit'),
		path('schedule/', SchedulerView.as_view(),name='schedule'),
		path('result/', ResultView.as_view(),name='result'),

		

	]