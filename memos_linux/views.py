from django.shortcuts import render

# Create your views here:

from datetime import datetime
from .models import Memos

# Create your views here.

def memos_linux(request):
	articles=Memos.objects.all()
	return render(request,'memos_linux/memos.html',{'derniers_articles':articles})
