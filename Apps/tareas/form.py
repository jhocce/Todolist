from django import forms
from .models import tarea
from datetime import datetime, date, timedelta
# from django.contrib.auth.models import User


# RadioSelect
class CreatetareaForms(forms.ModelForm):

	class Meta:

		model = tarea
		fields = ['Status', 'Titulo', 'Description', 'Fecha', 'Hora', 'user']
		widgets = {
			'Fecha':forms.DateInput(format='%Y-%m-%d %H:%M:%S', attrs={'type':'date'}),
			'Hora':forms.TimeInput(format='%H:%M:%S', attrs={'type':'time'})
		}

	def clean_Fecha(self):
		date = self.cleaned_data['Fecha']
		if str(date) < str(datetime.now().date()):
			raise forms.ValidationError("La fecha no puede estar en el pasado")
		return date