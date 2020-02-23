from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render_to_response
from datetime import datetime
from django.utils import timezone
from .models import Ressources
from .models import Categories
from .forms import RessourcesForm
from .forms import CategoriesForm

def arriere_boutique(request):
	return render_to_response('arriere_boutique/arriere_boutique.html',{'articles':Ressources.objects.all(),'categories':Categories.objects.all()})

	#return render(request,'arriere_boutique/arriere_boutique.html',{'tous_articles':articles})
	#return render(request,'arriere_boutique/arriere_boutique.html',locals())

#def voir_categorie(request,slug):
#	categorie=get_object_or_404(Categories,slug=slug)
#	return render(request,'arriere_boutique/arriere_boutique.html',{'categorie':categorie})

def detail_ressource(request,id):
	article=get_object_or_404(Ressources,id=id)
	return render(request,'arriere_boutique/detail_ressource.html',{'article':article})

def editer_ressource(request,id):
	article=get_object_or_404(Ressources, id=id)
	if request.method == "POST":
		form=RessourcesForm(request.POST, instance=article)
		if form.is_valid():
			article=form.save(commit=False)
			article.date=timezone.now()
			article.save()
			return redirect('detail_ressource',id=article.id)
	else:
		form = RessourcesForm(instance=article)
	return render(request, 'arriere_boutique/editer_ressource.html', {'form': form})

def nouvelle_ressource(request):
	if request.method == "POST":
		form=RessourcesForm(request.POST)
		if form.is_valid():
			article=form.save(commit=False)
			article.date=timezone.now()
			article.save()
			return redirect('arriere_boutique')
	else:
		form = RessourcesForm()
	return render(request, 'arriere_boutique/nouvelle_ressource.html', {'form': form})

		