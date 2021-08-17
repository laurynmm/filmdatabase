import datetime

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Film(models.Model):
    """Model representing a film."""
    title = models.CharField(max_length=200)
    year = models.IntegerField()

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        """Returns the url to access a detail record for this film"""
        return reverse('film-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing this film"""
        return self.title

class Review(models.Model):
    """Model representing a review of a film by a user."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    date_watched = models.DateField()
    
    class Meta:
        ordering = ['-date_watched']

    def __str__(self):
        """String for representing the Model object"""
        date = str(self.date_watched)
        return self.film.title + '; ' + date + '; ' + self.user.get_username()
