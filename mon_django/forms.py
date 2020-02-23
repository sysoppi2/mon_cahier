from django import forms
from .models import MonDjango, Commentaire

class MonDjangoForm(forms.ModelForm):
	class Meta:
		model = MonDjango
		fields = '__all__'

class CommentaireForm(forms.ModelForm):
	class Meta:
		model = Commentaire
		fields = '__all__'