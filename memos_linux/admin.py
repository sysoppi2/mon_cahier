from django.contrib import admin
from .models import Memos

class MemosAdmin(admin.ModelAdmin):
	list_display = ('sujet','texte')
	list_filter = ('sujet','texte')

admin.site.register(Memos,MemosAdmin)