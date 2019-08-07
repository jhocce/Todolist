from django.shortcuts import render
from django.views.generic import CreateView, FormView, RedirectView, UpdateView, DetailView
from rest_framework import generics
from .serialisers import UserSerializers
from .forms import CreateUserForms, UpdateUserForms
from .models import User
from django.contrib.auth import logout
from braces.views import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponseRedirect

class user_create(CreateView):


	form_class = CreateUserForms
	template_name = "users/user_create.html"
	model = User
	success_url= "/user/login/"
	login_url = "/user/login/"

	def form_valid(self, form, **kwargs):
		context = super(user_create, self).get_context_data(**kwargs)
		return super(user_create, self).form_valid(form)

	def form_invalid(self, form, **kwargs):
		context = super(user_create, self).get_context_data(**kwargs)
		return super(user_create, self).form_invalid(form)


class login_view(FormView):

	form_class = AuthenticationForm
	template_name = "users/login_user.html"
	success_url = "/tareas/agenda/"

	def dispatch(self, request, *args, **kwargs):
		context = super(login_view, self).get_context_data(**kwargs)
		if request.user.is_authenticated:
			return HttpResponseRedirect(self.get_success_url())
		else:
			return super(login_view, self).dispatch(request,*args, **kwargs )

	def form_valid(self, form):

		login(self.request, form.get_user())
		return super(login_view, self).form_valid(form)


	def form_invalid(self, form, **kwargs):

		context = super(login_view, self).get_context_data(**kwargs)
		return super(login_view, self).form_invalid(form)


class LogoutView(RedirectView):

	pattern_name = 'user:login'

	def get(self, request, *args, **kwargs):
		logout(request)
		return super(LogoutView, self).get(request, *args, **kwargs)


class user_detail(LoginRequiredMixin, DetailView):

	# form_class = CreateUserForms
	template_name = "users/user_detail.html"
	model = User
	success_url= "/tareas/agenda/"
	login_url = "/user/login/"


	def get_context_data(self, **kwargs):
		context = super(user_detail, self).get_context_data(**kwargs)
		return context


class user_update(LoginRequiredMixin, UpdateView):


	form_class = UpdateUserForms
	template_name = "users/user_update.html"
	model = User
	success_url= "/user/logout/"
	login_url = "/user/login/"
	