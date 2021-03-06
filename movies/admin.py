from django.contrib import admin

from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'imdb_score', 'director', 'popularity']
    search_fields = ['name', 'director']
    pass


admin.site.register(Movie, MovieAdmin)
