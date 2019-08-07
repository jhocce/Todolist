from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User

# RadioSelect
class CreateUserForms(forms.ModelForm):


	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'password', 'email']


	def clean_username(self):
		username = self.cleaned_data['username']

		try:
			User.objects.get(username=username)
			raise forms.ValidationError("Ya existe un usuario similar.")
		except User.DoesNotExist:
			return username

	def clean_email(self):
		email = self.cleaned_data['email']

		try:
			User.objects.get(email=email)
			raise forms.ValidationError("Este correo ya esta registrado.")
		except User.DoesNotExist:
			return email

	def clean_password(self):
		password = self.cleaned_data['password']
		return make_password(password)


class UpdateUserForms(forms.ModelForm):


	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'password', 'email']


	def clean_username(self):
		username = self.cleaned_data['username']

		user = User.objects.filter(username=username)
		if user.count()>1:
			raise forms.ValidationError("Ya existe un usuario similar.")
		return username

	def clean_email(self):
		email = self.cleaned_data['email']

		user = User.objects.filter(email=email)
		if user.count()>1:
			raise forms.ValidationError("Este correo ya esta registrado.")
		return email

	def clean_password(self):
		password = self.cleaned_data['password']
		return make_password(password)