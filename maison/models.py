from django.db import models

class Photo(models.Model):
# nom de la table dans bd sql : maison_photo
# noms des champs : nom, lieu, photo
	nom=models.CharField(max_length=50)
	lieu=models.TextField()
	photo=models.ImageField(upload_to="photos/")
   
	def __str__(self):
		return self.nom
