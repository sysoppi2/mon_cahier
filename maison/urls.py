from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.maison),
	path('nouvelle/',views.nouvelle_image),
]