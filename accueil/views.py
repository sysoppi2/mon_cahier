from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect 
from datetime import datetime
from django.utils import timezone
from .models import Accueil
from .forms import AccueilForm

def accueil(request):
	articles=Accueil.objects.all()
	return render(request,'accueil/accueil.html',{'tous_sujets':articles})

def detail_item(request,item):
	article=get_object_or_404(Accueil,item=item)
	return render(request,'accueil/detail_item.html',{'article':article})

def nouvel_element(request):
	if request.method == "POST":
		form=AccueilForm(request.POST)
		if form.is_valid():
			article=form.save(commit=False)
			article.date=timezone.now()
			article.save()
			return redirect('accueil')
	else:
		form = AccueilForm()
	return render(request, 'accueil/nouvel_element.html', {'form': form})