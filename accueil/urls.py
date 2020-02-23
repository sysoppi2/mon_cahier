from django.urls import path
from . import views

urlpatterns = [
	path('', views.accueil,name='accueil'),
	path('<int:item>/',views.detail_item,name='detail_item'),
	path('nouvel/',views.nouvel_element,name='nouvel_element'),
]