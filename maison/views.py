from django.shortcuts import render
from datetime import datetime

# Create your views here.

def maison(request):
	return render(request,'maison/ressources.html',{'date':datetime.now()})
