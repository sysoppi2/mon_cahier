from django import forms
from .models import Photo

class NouvellePhotoForm(forms.Form):
	nom=forms.CharField()
	lieu=forms.CharField(widget=forms.Textarea)
	photo=forms.ImageField()