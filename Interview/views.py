from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import CreateView,DeleteView,UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin,PermissionRequiredMixin
from .forms import ScheduleAddForm,SearchScheduleForm

from django.contrib.auth.models import Permission
from django.urls import reverse_lazy
from .models import InterviewSchedule

from django.conf import settings

class InterviewScheduleView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	form_class = ScheduleAddForm
	login_url = 'login'
	success_url = reverse_lazy('home')
	template_name = 'addschedule.html'
	redirect_field_name = 'redirect_to'

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		return (self.request.user.user_type == "candidate" or self.request.user.user_type == "interviewer" )


class SchedulerView(LoginRequiredMixin, UserPassesTestMixin, FormView):
	form_class = SearchScheduleForm
	login_url = 'login'
	template_name = 'search.html'
	redirect_field_name = 'redirect_to'
	success_url = reverse_lazy('home')


	def form_valid(self,form):
		interviewer = form.cleaned_data.get('interviewer_id')
		candidate = form.cleaned_data.get('candidate_id')
		candidate_list_of_hours = []
		interviewer_list_of_hours = []

		for objects in InterviewSchedule.objects.all():
				
			if objects.owner.username == interviewer:
				for i in range(objects.start_time.hour,objects.end_time.hour+1):
					interviewer_list_of_hours.append(i)
				print(interviewer_list_of_hours)

			elif objects.owner.username == candidate:
		
				for i in range(objects.start_time.hour,objects.end_time.hour+1):
					candidate_list_of_hours.append(i)			
				print(candidate_list_of_hours)

			else : 
					print()
					print("not found")
					print()
		
		

		return super().form_valid(form)
	
	def test_func(self):
		return (self.request.user.user_type == 'hr')
	
	