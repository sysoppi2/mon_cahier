from django import forms
from .models import Article, Categorie, Commentaire

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = '__all__'

class CategorieForm(forms.ModelForm):
	class Meta:
		model = Categorie
		fields = '__all__'

class CommentaireForm(forms.ModelForm):
	class Meta:
		model = Commentaire
		fields = '__all__'