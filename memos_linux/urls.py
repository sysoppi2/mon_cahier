from django.urls import path
from . import views

urlpatterns = [
	# toute requete '192.168.1.13/arriere_boutique/accueil' affichera ce qui est defini par la fonction home du fichier views
	path('', views.memos_linux),
	path('memos_linux/', views.memos_linux),
]