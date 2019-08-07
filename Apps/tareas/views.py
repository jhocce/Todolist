import time
from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework import Response
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin
from rest_framework.response import Response
from .form import CreatetareaForms
from .models import tarea



# Create your views here.
class createtarea(LoginRequiredMixin, CreateView):

	form_class = CreatetareaForms
	template_name = "tareas/tareas_create.html"
	model = tarea
	success_url="/tareas/agenda/"
	login_url = "/user/login/"

	def get_context_data(self, **kwargs):
		context = super(createtarea, self).get_context_data(**kwargs)
		return context

	def form_valid(self, form):
		print("formulario valido")
		form.instance.user = self.request.user
		return super(createtarea, self).form_valid(form)

	def form_invalid(self, form):
		return super(createtarea, self).form_invalid(form)
	

class agenda(LoginRequiredMixin, ListView):
	
	template_name = 'tareas/listtareas.html'
	queryset = tarea.objects.all()
	login_url = "/user/login/"

	def get_queryset(self):
		self.query=tarea.objects.filter(user=self.request.user)
		if self.query.count()==0:
			self.va=True
		else:
			self.va=False
		descripcion = [des.Description[0:15]+"..."  for des in  self.query ]
		
		return zip(descripcion, self.query)

	def get_context_data(self, **kwargs):
		context = super(agenda, self).get_context_data(**kwargs)
		if self.va:
			context['vacio']=True
		return context




class tarea_detail( LoginRequiredMixin, DetailView):
	
	model=tarea
	template_name="tareas/tareas_detail.html"
	login_url = "/user/login/"


	def get_context_data(self, **kwargs):
		context = super(tarea_detail, self).get_context_data(**kwargs)
		# context['tarea'] = tarea.objects.filter(user=self.request.user, pk= pk )
		fecha = datetime.now().date()
		if (str(context['object'].Fecha ) < str(fecha)) and context['object'].Status==False:
			context['vencimiento'] = True
			context['sms'] = "Ops esta actividad ya vencio :("
		if (str(context['object'].Fecha ) > str(fecha)) and context['object'].Status==False:
			context['vencimiento'] = False
			context['sms'] = "Todavia estas a tiempo :D"
		if (str(context['object'].Fecha ) < str(fecha)) and context['object'].Status==True:
			context['vencimiento'] = False
			context['sms'] = "Esta actividad esta lista y ya vencio el plazo! :D"
		if (str(context['object'].Fecha ) < str(fecha)) and context['object'].Status==False:
			context['vencimiento'] = True
			context['sms'] = "Ops esta actividad ya vencio :("
		if (str(context['object'].Fecha ) > str(fecha)) and context['object'].Status==True:
			context['vencimiento'] = False
			context['sms'] = "Esta actividad esta lista y con tiempo de sobra :D"
		return context


def tarea_update_status(request):
	
	tarea2 = tarea.objects.get(pk=request.GET['pk'])
	if tarea2.status()==False:
		tarea_mod = tarea.objects.filter(pk=request.GET['pk']).update(Status=True)
	else:
		tarea_mod = tarea.objects.filter(pk=request.GET['pk']).update(Status=False)
	return HttpResponse("True", content_type="application/json")

class tarea_eliminar(LoginRequiredMixin, DeleteView):

	model=tarea
	success_url="/tareas/agenda/"
	login_url = "/user/login/"


class tarea_editar(LoginRequiredMixin, UpdateView):

	form_class = CreatetareaForms
	template_name="tareas/tareas_edit.html"
	model = tarea
	success_url="/tareas/agenda/"
	login_url = "/user/login/"
		

	def get_context_data(self, **kwargs):
		context = super(tarea_editar, self).get_context_data(**kwargs)
		return context

	def form_valid(self, form):
		print("formulario valido")
		form.instance.user = self.request.user
		return super(tarea_editar, self).form_valid(form)

	def form_invalid(self, form):
		print("formulario invalido")
		# form.instance.User = self.request.User
		return super(tarea_editar, self).form_invalid(form)