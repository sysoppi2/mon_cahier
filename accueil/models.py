from django.db import models
from django.utils import timezone

class Accueil(models.Model):
	# champs du modèle
	sujet = models.CharField(max_length=50)
	slug = models.SlugField()
	description = models.CharField(max_length=200)
	date = models.DateTimeField(default=timezone.now, verbose_name="Date de mise à jour")
	
	# + comportement propre au modèle	
	class Meta:
		verbose_name = "article"
		ordering = ['sujet']	