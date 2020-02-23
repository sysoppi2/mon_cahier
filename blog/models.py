from django.db import models
from django.utils import timezone

class Article(models.Model):
	titre = models.CharField(max_length=100)
	slug = models.SlugField()
	auteur = models.CharField(max_length=42)
	contenu = models.TextField(null=True)
	date = models.DateTimeField(verbose_name="Date de parution", auto_now_add=True, auto_now=False)
	is_visible = models.BooleanField(verbose_name="Article publié ?", default=False)
	categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

	def __str__(self):
		return self.titre

class Categorie(models.Model):
	titre = models.CharField(max_length=100)

	def __str__(self):
		return self.titre

class Commentaire(models.Model):
	commentaire = models.TextField(null=True)
	pseudo = models.CharField(blank=True, null=True, max_length=40)
	email = models.EmailField(max_length=100)
	date = models.DateTimeField(default=timezone.now,verbose_name="Date de parution")

	def __str__(self):
		return self.commentaire