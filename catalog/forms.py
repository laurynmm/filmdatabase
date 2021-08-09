
from django import forms

class NewFilmForm(forms.Form):
    title = forms.CharField(max_length=200)
