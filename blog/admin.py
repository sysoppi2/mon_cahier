from django.contrib import admin

from .models import Article, Categorie, Commentaire

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'categorie', 'date', 'is_visible', )
    list_filter = ('categorie', )
    search_fields = ('title', 'auteur', )

    prepopulated_fields = {'slug': ('titre', )}

admin.site.register(Article, ArticleAdmin)

class CategorieAdmin(admin.ModelAdmin):
	list_display = ('titre', )

admin.site.register(Categorie,CategorieAdmin)

class CommentaireAdmin(admin.ModelAdmin):
	list_display = ('commentaire', 'date', )

admin.site.register(Commentaire,CommentaireAdmin)