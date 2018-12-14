from django.forms import ModelForm
from .models import Tipo

class TipoForm(ModelForm):
	class Meta:
		model = Tipo
		fields = ['tipo', 'palavras_chaves']