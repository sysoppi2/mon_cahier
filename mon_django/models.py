from django.db import models
from django.utils import timezone

class MonDjango(models.Model):
	concerne = models.CharField(max_length=100)
	description = models.TextField(null=True)
	date = models.DateTimeField(default=timezone.now,verbose_name="Date de parution")
	is_visible = models.BooleanField(verbose_name="Article publié ?", default=False)

	def __str__(self):
		return self.concerne

class Commentaire(models.Model):
	commentaire = models.TextField(null=True)
	pseudo = models.CharField(blank=True, null=True, max_length=40)
	email = models.EmailField(max_length=100)
	date = models.DateTimeField(default=timezone.now,verbose_name="Date de parution")

	def __str__(self):
		return self.commentaire