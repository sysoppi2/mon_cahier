from django import forms
from .models import Accueil

# création du formulaire à partir du modèle
class AccueilForm(forms.ModelForm):
	class Meta:
		model = Accueil
		fields = '__all__'