from django.contrib import admin
from .models import Ressources, Categories

class RessourcesAdmin(admin.ModelAdmin):
	list_display = ('theme','application')
	list_filter = ('theme','date')

class CategoriesAdmin(admin.ModelAdmin):
	prepolated_fields={'slug':('titre',)}	

admin.site.register(Ressources,RessourcesAdmin)
admin.site.register(Categories,CategoriesAdmin)