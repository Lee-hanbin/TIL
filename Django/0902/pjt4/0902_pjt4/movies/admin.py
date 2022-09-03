from django.contrib import admin
from .models import Article
# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'audience', 'release_date', 'genre', 'score', 'poster_url', 'description')

admin.site.register(Article, MoviesAdmin)