from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('nom','photo')
#	list_filter = ('nom')

admin.site.register(Photo,PhotoAdmin)
