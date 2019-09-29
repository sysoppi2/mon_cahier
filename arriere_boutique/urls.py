from django.urls import path
from . import views

urlpatterns = [
	# toute requete '192.168.1.13/arriere_boutique/accueil' affichera ce qui est defini par la fonction home du fichier views
	path('accueil', views.home),
	# toute requete '192.168.1.13/arriere_boutique' affichera ce qui est defini par la fonction home du fichier views
	#path('', views.home),
	# toute requete '192.168.1.13/arriere_boutique/chapitre/'n°'' affichera ce qui est defini par la fonction view_chapitre du fichier views
	path('chapitre/<int:id_chapitre>',views.view_chapitre),
	path('redirection',views.view_redirection),
]