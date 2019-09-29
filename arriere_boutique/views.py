from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime

# Create your views here

def home(request):
	return render(request,'arriere_boutique/post_list.html',{'date':datetime.now()})

def view_chapitre(request, id_chapitre):
	if id_chapitre < 1:
		raise Http404
	elif id_chapitre > 10 and id_chapitre < 100:
		return redirect("http://192.168.1.13/arriere_boutique/accueil")
	elif id_chapitre >= 100:
		return redirect(view_redirection)
	else:	
		return HttpResponse(
			"vous avez demande le chapitre n° {0} !".format(id_chapitre)
		)

def view_redirection(request):
	return render(request,'base.html')