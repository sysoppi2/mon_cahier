from django import forms
from .models import Ressources, Categories

class RessourcesForm(forms.ModelForm):
	class Meta:
		model = Ressources
		fields = '__all__'

class CategoriesForm(forms.ModelForm):
	class Meta:
		model = Categories
		fields = '__all__'
