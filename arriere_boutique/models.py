from django.db import models
from django.utils import timezone

class Ressources(models.Model):
	#sujet = models.CharField(max_length=200) remplacé par categorie
	theme = models.TextField(null=True)
	application = models.CharField(max_length=100)
	date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
	categorie = models.ForeignKey('Categories', on_delete=models.CASCADE)
    
	class Meta:
		verbose_name = "article"
		ordering = ['date']
    
	def __str__(self):
		return self.theme

class Categories(models.Model):
	titre = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)

	def __str__(self):
		return self.titre
