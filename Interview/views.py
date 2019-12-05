from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin,PermissionRequiredMixin
from .forms import ScheduleAddForm

from django.contrib.auth.models import Permission
from django.urls import reverse_lazy
from .models import InterviewSchedule

from django.conf import settings

class InterviewScheduleView(CreateView):
	form_class = ScheduleAddForm
	success_url = reverse_lazy('home')
	template_name = 'addschedule.html'
	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)
