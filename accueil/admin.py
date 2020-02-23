from django.contrib import admin
from .models import Accueil

class AccueilAdmin(admin.ModelAdmin):
	list_display = ('sujet','description')
	list_display = ('sujet','date')

admin.site.register(Accueil,AccueilAdmin)