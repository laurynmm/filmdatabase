
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Film, Person, Review

class FilmSearchForm(forms.Form):
    title = forms.CharField(max_length=200, label='')

class FilmTitleForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title']

class ReviewRatingForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating']

class PersonNameForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name']
