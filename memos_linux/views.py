from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.utils import timezone
from .models import Memos
from .models import Contact
from .forms import MemosForm
from .forms import ContactForm

# Create your views here:

def memos_linux(request):
	articles=Memos.objects.all()
	return render(request,'memos_linux/memos.html',{'derniers_articles':articles})

def detail_memo(request,pk):
	article=get_object_or_404(Memos,pk=pk)
	return render(request,'memos_linux/detail_memo.html',{'article':article})

def editer_memo(request,pk):
	article=get_object_or_404(Memos, pk=pk)
	if request.method == "POST":
		form=MemosForm(request.POST, instance=article)
		if form.is_valid():
			article=form.save(commit=False)
			article.date=timezone.now()
			article.save()
			return redirect('detail_memo',pk=article.pk)
	else:
		form = MemosForm(instance=article)
	return render(request, 'memos_linux/editer_memo.html', {'form': form})

def nouveau_memo(request):
	if request.method == "POST":
		form=MemosForm(request.POST)
		if form.is_valid():
			article=form.save(commit=False)
			article.date=timezone.now()
			article.save()
			return redirect('detail_memo',pk=article.pk)
	else:
		form = MemosForm()
	return render(request, 'memos_linux/editer_memo.html', {'form': form})

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        texte = form.cleaned_data['texte']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'memos_linux/contact.html', locals())
