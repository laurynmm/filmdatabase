from django.contrib import admin

from .models import Film, Review

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'film', 'date_watched')
