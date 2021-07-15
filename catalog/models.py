import uuid
import datetime

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Genre(models.Model):
    """Model representing a film genre."""
    name = models.CharField(max_length=200, help_text='Enter a film genre (e.g. Noir)')

    def __str__(self):
        """String for representing the Model object"""
        return self.name

class Language(models.Model):
    """Model representing the primary language of a film."""
    name = models.CharField(max_length=100, help_text='Enter primary language of film (e.g. French)')

    def __str__(self):
        """String for representing the Model object"""
        return self.name

class Person(models.Model):
    """Model representing a person involved in a film."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance"""
        return reverse('person-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing Model object"""
        return f'{self.last_name}, {self.first_name}'

class Film(models.Model):
    """Model representing a film."""
    title = models.CharField(max_length=200)
    plot = models.TextField(max_length=1000, help_text='Enter a brief description of the film')
    year = models.IntegerField(validators=[MinValueValidator(1890), MaxValueValidator(datetime.date.today().year)])
    imdb_id = models.CharField('IMDb id', max_length=200, unique=True)

    # ManyToMany Field for genre
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this film')

    # Foreign Key used for language
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    # ManyToMany used for director(s)
    director = models.ManyToManyField(Person, help_text='Select person or people who directed this film', related_name='director')

    # ManyToMany used for actors
    actors = models.ManyToManyField(Person, help_text='Select people who performed in this film', related_name='actors')

    def get_absolute_url(self):
        """Returns the url to access a detail record for this film"""
        return reverse('film-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing this film"""
        return self.title

class Review(models.Model):
    """Model representing a review of a film by a user."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this review in entire database')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    private = models.BooleanField(default=False)
    date_watched = models.DateField(null=True, blank=True)
    
    class Reviews(models.IntegerChoices):
        NOT_RATED = 0
        BAD = 1
        OKAY = 2
        GOOD = 3
        GREAT = 4
        AMAZING = 5

    rating = models.IntegerField(choices=Reviews.choices, blank=False)

    class Meta:
        ordering = ['rating', 'film', 'date_watched']

    def __str__(self):
        """String for representing the Model object"""
        return self.get_rating_display() + ' rating of ' + self.film.title + ' by ' + self.user.get_username()
