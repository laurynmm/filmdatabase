
from catalog.models import Review
from django import forms

class NewFilmForm(forms.Form):
    title = forms.CharField(max_length=200)

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['film', 'date_watched']