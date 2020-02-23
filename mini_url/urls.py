from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('', views.liste_url,name='liste_url'),
	path('nouvelle/',views.nouvelle_url,name='nouvelle_url'),
	# (?P<code>\w{6}) capturera 6 caractères alphanumériques. 
	url(r'^(?P<code>\w{6})/$', views.redirection, name='url_redirection'),
]