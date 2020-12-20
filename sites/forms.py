from django.forms import ModelForm
from .models import *

class CalculateForm(ModelForm):
	class Meta:
		model = Calculate
		fields = '__all__'
