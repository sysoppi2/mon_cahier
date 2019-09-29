from django.db import models
from django.utils import timezone

# Create your models here:

class Memos(models.Model):
	sujet=models.CharField(max_length=200)
	texte=models.TextField(null=True)
	date=models.DateTimeField(default=timezone.now,verbose_name="Date de parution")

	class Meta:
		verbose_name="article"
		ordering=['date']

def __str__(self):
        return self.sujet
