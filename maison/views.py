from django.shortcuts import render
from django.core.files import File
from datetime import datetime
from .models import Photo
from .forms import NouvellePhotoForm

def maison(request):
	return render(request,'maison/voir_photo.html',{'photos':Photo.objects.all()})

def nouvelle_image(request):
	sauvegarde = False
	form = NouvellePhotoForm(request.POST or None, request.FILES)
	if form.is_valid():
		image=Photo()
		image.nom=form.cleaned_data["nom"]
		image.lieu=form.cleaned_data["lieu"]
		image.photo=form.cleaned_data["photo"]
		image.save()
		sauvegarde=True
	else:
		form=NouvellePhotoForm()

	return render(request, 'maison/nouvelle_photo.html', {
		'form': form,
		'sauvegarde': sauvegarde
	})
