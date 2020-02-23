from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.arriere_boutique,name='arriere_boutique'),
	path('<int:id>/',views.detail_ressource,name='detail_ressource'),
	path('nouvelle/',views.nouvelle_ressource,name='nouvelle_ressource'),
	path('<int:id>/editer/', views.editer_ressource,name='editer_ressource'),		
]