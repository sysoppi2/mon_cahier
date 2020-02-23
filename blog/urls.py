from django.urls import path
from . import views

urlpatterns = [
	path('', views.blog,name='blog'),
	path('<slug>/',views.lire_article,name='lire_article'),
]
