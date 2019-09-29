from django.urls import path, include
from . import views

urlpatterns = [
	# toute requete '192.168.1.13/arriere_boutique/accueil' affichera ce qui est defini par la fonction home du fichier views
	path('',views.maison),
	path('maison', views.maison),
	path('maison/', views.maison),
	path('maison/memos_linux',include('memos_linux.urls')),
	path('maison/memos_linux/',include('memos_linux.urls')),
]