
from django import forms

class FilmSearchForm(forms.Form):
    title = forms.CharField(max_length=200, label='')
