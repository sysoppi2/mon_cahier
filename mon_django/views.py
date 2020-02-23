from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.utils import timezone
from .models import MonDjango
from .models import Commentaire
from .forms import MonDjangoForm
from .forms import CommentaireForm

def mon_django(request):
	articles = MonDjango.objects.all()
	return render(request,'mon_django/mon_django.html',{'derniers_articles':articles})

def detail_sujet(request,pk):
	article=get_object_or_404(MonDjango,pk=pk)
	return render(request,'mon_django/detail_sujet.html',{'article':article})

def nouveau_sujet(request):
	if request.method == "POST":
		form=MonDjangoForm(request.POST)
		if form.is_valid():
			article=form.save(commit=False)
			article.date=timezone.now()
			article.save()
			return redirect('detail_sujet',pk=article.pk)
	else:
		form = MonDjangoForm()
	return render(request, 'mon_django/editer_sujet.html', {'form': form})

def editer_sujet(request,pk):
	article=get_object_or_404(MonDjango, pk=pk)
	if request.method == "POST":
		form=MonDjangoForm(request.POST, instance=article)
		if form.is_valid():
			article=form.save(commit=False)
			article.date=timezone.now()
			article.save()
			return redirect('detail_sujet',pk=article.pk)
	else:
		form = MonDjangoForm(instance=article)
	return render(request, 'mon_django/editer_sujet.html', {'form': form})

def nouveau_commentaire(request):
	if request.method == "POST":
		form=CommentaireForm(request.POST)
		if form.is_valid():
			article=form.save(commit=False)
			article.date=timezone.now()
			article.save()
			return redirect('mon_django/detail_sujet',{'article': article})
			#return redirect('detail_sujet',{'article': article})
		else:
			form=CommentaireForm()
		return render(request, 'mon_django/detail_sujet.html', {'form': form})
