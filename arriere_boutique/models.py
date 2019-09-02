from django.conf import settings
from django.db import models
from django.utils import timezone

# definir modele 'Post' 
class Post(models.Model):
	# definir proprietes associees au modele
	auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	titre = models.CharField(max_length=200)
	texte = models.TextField()
	date_creation = models.DateTimeField(default=timezone.now)
	date_publication = models.DateTimeField(blank=True, null=True)
	
	# definir methode 'publication' 
	def publication(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.titre