from django import forms
from .models import *


class TaskForm(forms.ModelForm):
	a= forms.TextInput(attrs={'placeholder': 'TODO'})
	title = forms.CharField(widget=a)

	class Meta:
		model = Task
		fields = '__all__'

