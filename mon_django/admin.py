from django.contrib import admin
from .models import MonDjango, Commentaire

class MonDjangoAdmin(admin.ModelAdmin):
	list_display = ('date','concerne')
admin.site.register(MonDjango,MonDjangoAdmin)
	
class CommentaireAdmin(admin.ModelAdmin):
	list_display = ('date','commentaire')
admin.site.register(Commentaire,CommentaireAdmin)

