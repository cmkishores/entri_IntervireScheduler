from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView,View
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
	success_url = reverse_lazy('result')


	def form_valid(self,form):
		interviewer = form.cleaned_data.get('interviewer_id')
		candidate = form.cleaned_data.get('candidate_id')
		candidate_list_of_hours = []
		interviewer_list_of_hours = []

		for objects in InterviewSchedule.objects.all():
				
			if objects.owner.username == interviewer:
				for i in range(objects.start_time.hour,objects.end_time.hour):
					interviewer_list_of_hours.append(i)

			elif objects.owner.username == candidate:
		
				for i in range(objects.start_time.hour,objects.end_time.hour):
					candidate_list_of_hours.append(i)			

			else : 
					print()
					print("not found")
					print()
		
		
		print("Possible hours for interviewer is ",set(interviewer_list_of_hours))
		print("Possible hours for candidate is ",set(candidate_list_of_hours))

		list_times = []
		#if(set(interviewer_list_of_hours) & set(candidate_list_of_hours)):
			#list_times.append( (set(interviewer_list_of_hours) & set(candidate_list_of_hours)) )
		#lists = list(list_times)
		
		for item in interviewer_list_of_hours:
			if item in candidate_list_of_hours:
				list_times.append((item,item+1))
		self.request.session['list_items'] = list_times
		return super().form_valid(form)
	
	def test_func(self):
		return (self.request.user.user_type == 'hr')

class ResultView(LoginRequiredMixin,TemplateView):
	template_name = 'result.html'

	
	