from django.contrib import admin

from .models import Genre, Language, Person, Film, Review

admin.site.register(Genre)
admin.site.register(Language)

class FilmActorsInline(admin.TabularInline):
    model = Film.actors.through
    extra = 0

class FilmDirectorInline(admin.TabularInline):
    model = Film.director.through
    extra = 0

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [FilmActorsInline, FilmDirectorInline]

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'imdb_id')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('rating', 'private', 'date_watched')
    list_display = ('user', 'film', 'rating', 'date_watched')
