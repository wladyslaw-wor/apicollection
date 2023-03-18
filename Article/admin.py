from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'discipline_id', 'discipline', 'subject', 'article', 'paragraphs', 'number_ext')
    list_display_links = ('id', 'subject')
    search_fields = ('id', 'subject', 'discipline', 'article')
    list_filter = ('discipline', 'paragraphs')

admin.site.register(Article, ArticleAdmin)